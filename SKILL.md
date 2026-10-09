---
name: professional-research-html
description: Create or revise a Chinese journal-style HTML research report from a topic, draft, or sources. Use when the result needs verified citations, academic prose, professional desktop and print layout, a glossary, and in-text links to term definitions.
---

# Professional Research HTML

## Portability

This skill follows the Agent Skills directory convention: `SKILL.md` and the
supporting `references/` directory form its portable core. It can therefore be
used by skills-compatible agents beyond Codex. `agents/openai.yaml` is optional
Codex interface metadata; hosts that do not recognize it may ignore it. Use the
target host's own file, browser, and permission tools when carrying out the
workflow.

Create one self-contained, directly openable `.html` report that is useful as both a research paper and a polished reading artifact. Use this skill for research reports, product studies, market analyses, technology briefs, and policy analyses when scholarly Chinese presentation and source traceability matter. It is not a substitute for a genuine peer-reviewed publication process.

## Start from the material available

- If the user provides a draft or an earlier conversation, extract its propositions, cited sources, dates, and factual claims before rewriting. Treat prior conversation text as source material, not authority.
- If freshness, facts, source URLs, or dates can affect the report, verify them against primary sources. Prefer official announcements, product documentation, standards, filings, and original research. Keep the claim narrower when a primary source does not support the earlier wording.
- Clearly distinguish published functionality, announced plans, observed deployment practices, and the report's own inference or design recommendation. Do not write a planned feature as a present capability.
- When a source is a living documentation page without a stated publication date, record an access date rather than inventing a date.

Read [workflow-and-layout.md](references/workflow-and-layout.md) before drafting or substantially revising a report. It contains the report structure, citation conventions, term-link pattern, and checks that make this skill reusable.

## Deliverable rules

- Use restrained academic Chinese: define scope, attribute claims, avoid conversational filler and marketing language, and reserve conclusions for evidence supported in the report.
- Adapt headings to the research question. For a full paper, normally include title, abstract, keywords, background, analytical framework or method, analysis, risks or limitations, comparison where useful, implications, conclusion, glossary, and references.
- Explain a specialized term at first meaningful use in concise Chinese. When a glossary is included, make the in-text term clickable and point it to its corresponding glossary entry. Link only terms that improve comprehension; do not turn ordinary words into a dense field of links.
- Give every external factual claim a nearby numbered citation. Include a bibliography with title, publisher or author, stable direct URL, date when verified, and access date for web material.
- Use CSS and semantic HTML within the file. Make tables readable, figures captioned, links keyboard-accessible, and print rules suitable for A4. Diagrams may use HTML/CSS or inline SVG when they communicate a relationship better than prose.
- Preserve clear visual separation between citations, term links, figure captions, notes, and ordinary body text. Avoid JavaScript unless the user asks for interactive behavior.
- Save final deliverables in the user-facing output location established for the task. Do not overwrite an existing deliverable unless the user asks to revise it.

## Quality check before handoff

Confirm the file opens as a standalone HTML document; internal anchors resolve; every glossary destination has at least one intended source link; citations map to bibliography entries; tables and figure labels are complete; and no draft placeholders remain. For visual work, inspect the rendered page when a browser or preview is available, paying special attention to desktop width, mobile overflow, and print styles.

When the host can run local commands, run `scripts/validate_html_report.py <report.html>` before handoff. It checks document structure, duplicate and unresolved anchors, and common violations of standalone delivery. Treat its warnings as items to review rather than automatic failure.
