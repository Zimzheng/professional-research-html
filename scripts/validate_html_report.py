#!/usr/bin/env python3
"""Validate structural invariants of a standalone research-report HTML file.

The validator intentionally uses only the Python standard library so a copied
skill remains usable in constrained agent environments. It validates mechanical
delivery invariants; it does not judge source accuracy or visual quality.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


class ReportParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = Counter()
        self.ids = Counter()
        self.fragment_links = []
        self.external_resources = []
        self.h1_count = 0

    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1
        if tag == "h1":
            self.h1_count += 1
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if element_id:
            self.ids[element_id] += 1

        href = attributes.get("href")
        if href and href.startswith("#") and href != "#":
            self.fragment_links.append(href[1:])

        for attribute_name in ("src", "poster", "data"):
            resource = attributes.get(attribute_name)
            if resource and re.match(r"^(https?:)?//", resource, re.IGNORECASE):
                self.external_resources.append(
                    f"<{tag} {attribute_name}=\"{resource}\">"
                )

        if tag == "link" and "stylesheet" in attributes.get("rel", "").lower():
            if href and re.match(r"^(https?:)?//", href, re.IGNORECASE):
                self.external_resources.append(f"<link href=\"{href}\">")


def validate(path):
    raw = path.read_text(encoding="utf-8")
    parser = ReportParser()
    parser.feed(raw)
    parser.close()

    errors = []
    warnings = []

    if not re.match(r"\s*<!doctype\s+html", raw, re.IGNORECASE):
        errors.append("缺少 HTML5 doctype（<!doctype html>）。")

    for tag in ("html", "head", "body"):
        if parser.tags[tag] != 1:
            errors.append(f"<{tag}> 应恰好出现一次，当前为 {parser.tags[tag]} 次。")

    duplicates = sorted(name for name, count in parser.ids.items() if count > 1)
    if duplicates:
        errors.append("存在重复 id：" + "、".join(duplicates) + "。")

    unresolved = sorted({target for target in parser.fragment_links if target not in parser.ids})
    if unresolved:
        errors.append("存在无法解析的内部锚点：" + "、".join(f"#{name}" for name in unresolved) + "。")

    if parser.external_resources:
        errors.append("存在外部脚本、样式或媒体资源：" + "；".join(parser.external_resources) + "。")

    if re.search(r"@import\s+(?:url\()?\s*['\"]?(?:https?:)?//", raw, re.IGNORECASE):
        errors.append("CSS 使用了外部 @import，文件不再是自包含交付物。")
    if re.search(r"url\(\s*['\"]?(?:https?:)?//", raw, re.IGNORECASE):
        errors.append("CSS 使用了外部 url(...) 资源，文件不再是自包含交付物。")

    if parser.tags["main"] == 0:
        warnings.append("未使用 <main> 语义容器。")
    if parser.h1_count != 1:
        warnings.append(f"建议全文使用一个 <h1> 标题，当前为 {parser.h1_count} 个。")
    if not re.search(r"<meta\s+[^>]*charset\s*=", raw, re.IGNORECASE):
        warnings.append("未声明字符集；中文报告建议使用 UTF-8。")
    if "@media print" not in raw.lower():
        warnings.append("未发现 @media print；请确认 A4 打印样式是否另有实现。")
    if not any(re.fullmatch(r"(?:ref-|r)\d+", target) for target in parser.fragment_links):
        warnings.append("未发现编号参考文献锚点；请确认引用需求是否适用。")

    return errors, warnings


def main():
    argument_parser = argparse.ArgumentParser(
        description="验证独立研究报告 HTML 的结构、内部锚点与自包含资源。"
    )
    argument_parser.add_argument("report", type=Path, help="待验证的 HTML 文件")
    args = argument_parser.parse_args()

    if not args.report.is_file():
        print(f"ERROR: 找不到 HTML 文件：{args.report}")
        return 2

    try:
        errors, warnings = validate(args.report)
    except UnicodeDecodeError:
        print("ERROR: 文件必须以 UTF-8 编码读取。")
        return 2

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")

    if errors:
        return 1
    print("OK: HTML 结构、内部锚点和自包含资源检查通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
