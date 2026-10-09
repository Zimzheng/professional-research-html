# 跨 Agent 安装与使用

本技能以 `SKILL.md` 作为入口，以 `references/` 提供补充规范。复制或安装时，请保留以下层级：

```text
professional-research-html/
├── SKILL.md
├── README.md
├── references/
│   └── workflow-and-layout.md
└── agents/
    └── openai.yaml          # 可选；仅 Codex 使用
```

`SKILL.md` 与 `references/` 是跨 Agent 的必需内容。`agents/openai.yaml` 不包含执行规则；不支持该文件的环境可直接忽略。

## 安装来源

```bash
git clone https://github.com/Zimzheng/professional-research-html.git
```

将克隆所得的 `professional-research-html` 目录完整复制到对应产品的 Skills 目录。对受版本影响的目录和入口，应以产品当前文档为准。

## 各环境接入

### Codex

将目录放入 `$CODEX_HOME/skills/professional-research-html`（通常为 `~/.codex/skills/professional-research-html`）。可在对话中写 `$professional-research-html`，或直接描述要生成的研究报告。

### Claude Code 与 Claude

Claude Skills 将带 YAML 前言的 `SKILL.md` 作为技能入口，并可同时携带参考文件和脚本。将该目录复制到当前 Claude 环境配置的 Skills 目录，随后以技能名称或自然语言研究任务调用。具体的安装入口会随 Claude 产品形态而变化，请参阅 [Claude Skills 基础文档](https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/fundamentals)。

### Qoder CLI

可选位置：

```text
~/.qoder/skills/professional-research-html/
<project>/.qoder/skills/professional-research-html/
```

安装或修改后在 Qoder CLI 执行 `/skills reload`。Qoder CLI 会按 `SKILL.md` 的 `name` 和 `description` 识别技能，支持自动匹配和显式调用。详见 [Qoder CLI Skills 文档](https://docs.qoder.com/cli/Skills)。

### QoderWork

将目录放入：

```text
~/.qoderwork/skills/professional-research-html/
```

也可使用 QoderWork 的 Skills 管理能力载入。QoderWork 可以根据技能描述自动调用，也支持在任务中明确指定技能；详见 [QoderWork Skills 文档](https://docs.qoder.com/qoderwork/skills)。

### WorkBuddy

部分 WorkBuddy 接入方式要求上传 ZIP，且压缩包的根目录必须直接包含 `SKILL.md`。仓库的 GitHub “Download ZIP” 通常会额外包一层仓库目录，因此建议从已克隆的仓库生成导入包：

```bash
scripts/package-skill.sh
```

生成的 `dist/professional-research-html.zip` 包含入口、参考规范和验证、打包脚本，可用于此类导入器。该脚本打包当前 Git 提交的内容；修改技能后，请先提交修改再生成发布包。若所在 WorkBuddy 实例有自定义 Skills 目录或企业策略，请以该实例的管理说明为准。

## 调用建议

以下提示在各环境中均适用：

```text
使用 professional-research-html：围绕“[主题]”制作中文专业期刊风格 HTML 研究报告。
核验时效性事实，给出文内引文和参考文献；在术语首次出现处作简释，
并将术语链接到文末术语表。输出一个可直接打开并适合 A4 打印的独立 HTML 文件。
```

运行 Agent 仍需具备研究所需的网页访问能力和目标目录写入权限；缺少其中任一能力时，应明确标注未核验事实或无法写入的输出位置。

## 交付验证

在生成报告的同一环境中，可运行以下零依赖检查：

```bash
python3 scripts/validate_html_report.py /path/to/report.html
```

该命令会失败于缺少基本文档结构、重复或失效的内部锚点，以及外部脚本、样式或媒体资源等常见非自包含交付问题；版式和事实准确性仍需由生成 Agent 结合浏览器预览与来源核验判断。
