# Workflow and layout reference

Use this reference whenever producing or materially revising a report with `professional-research-html`.

## 1. Establish an evidence ledger

Before composing, create a compact working list of:

| Field | Capture |
|---|---|
| Claim | The exact proposition the report will make |
| Source | Primary source or clearly labeled secondary source |
| Date | Publication or update date if stated; otherwise access date |
| Status | Current feature, planned feature, case-study observation, or analysis |
| Citation | Bibliography number or stable internal key |

This prevents a polished layout from obscuring an unverified statement. Omit unsupported detail or label it as an inference.

## 2. Use a paper-shaped information architecture

Use this sequence when it fits the topic. Merge or omit sections when evidence or scope does not justify them.

1. Title, subtitle, research date, material type, and scope.
2. Abstract: research question, method or material basis, central finding, and limit; usually 180–300 Chinese characters unless the user specifies otherwise.
3. Keywords: 4–7 discriminating terms.
4. Background and research question.
5. Conceptual framework, analytical method, or case boundary.
6. Main mechanism, evidence, or case analysis.
7. Risks, limitations, and unresolved questions.
8. Comparative analysis when at least two comparable approaches are materially relevant.
9. Product, policy, or practice implications. Mark recommendations as recommendations.
10. Conclusion.
11. Glossary and references.

## 3. Write for academic readability

- Begin paragraphs with the point they establish, then give evidence and implication.
- Prefer concrete terms: write the actor, resource, action, and boundary rather than abstract claims about “empowerment” or “transformation.”
- Use quoted English terminology only where it improves precision. Provide Chinese explanation on first use.
- Separate what a cited source says from the report's synthesis with phrases such as “该文档说明…”, “据此可推断…”, and “本文建议…”.
- Use tables for repeated comparisons and diagrams for chains, boundaries, or relationships involving at least three elements.

## 4. Citation and glossary pattern

Place citations immediately after the supported sentence or paragraph, using stable numeric links such as:

```html
<sup><a href="#ref-4">[4]</a></sup>
```

For a term with a definition, use one link with an informative title:

```html
<a class="term-ref" href="#term-service-account" title="查看术语解释">服务账户</a>
```

Give the glossary definition a matching destination:

```html
<tr>
  <td id="term-service-account">服务账户（Service Account）</td>
  <td>为程序或智能体设置的非个人账户，用于持续访问指定系统。</td>
</tr>
```

Use unique `id` values. Verify every `href="#term-…"` resolves to exactly one document element. Do not nest glossary links inside reference links, headings, navigation, or existing anchors.

Each web reference should use this minimum form:

```html
<li id="ref-4">机构或作者. <a href="https://…">文献标题</a>[EB/OL].
2026-01-15. 访问日期：2026-10-08.</li>
```

For living documentation with no reliable release date, write “动态更新文档。访问日期：…” rather than fabricate a date.

## 5. Standalone HTML design baseline

Keep markup semantic (`main`, `nav`, `section`, `figure`, `figcaption`, `table`, `ol`). Build desktop-first reading at roughly 900–1100px content width and include a narrow-screen breakpoint.

Recommended visual hierarchy:

- A modest journal masthead; a high-contrast title; compact metadata.
- A muted abstract panel and restrained section markers.
- One accent color plus neutral body colors; avoid decorative gradients and excessive effects.
- Tables with clear headers, modest striping, and horizontal scrolling only on small screens.
- Captions, notes, and references in a visibly smaller but readable style.
- Understated dotted term links; retain clear keyboard focus states.
- `@media print` rules that remove screen-only effects, preserve legibility in grayscale, set A4 margins, and avoid splitting headings, figures, and tables when possible.

Inline SVG is suitable for a compact architecture or flow diagram. Add a caption explaining whether it is an author synthesis or an adapted source diagram.

## 6. Completion checklist

- The title, abstract, and conclusion answer the same research question.
- All dates and product-status assertions were verified or marked as uncertain.
- Factual claims have nearby references and all reference anchors work.
- First-use terms are explained; selected terms link to glossary entries.
- Every term anchor resolves, without duplicate IDs.
- Tables fit desktop reading; narrow screens retain access through responsive styling.
- Print rules make the report usable on A4.
- The final file is self-contained and opens without a build step.
- When local command execution is available, run `scripts/validate_html_report.py <report.html>`. Resolve all reported errors; review warnings against the report's intended scope.
