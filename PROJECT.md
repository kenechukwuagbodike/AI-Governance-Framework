# Project 9: AI Governance Framework + Self-Assessment Tool
**Status:** 🟢 Live, including the P10 cross-link (redeployed ahead of the original joint-release plan, verified working on the live URL)
**Last Updated:** 2026-10-08
**Live Demo:** https://keni-ai-governance-framework.streamlit.app/
**GitHub:** https://github.com/kenechukwuagbodike/AI-Governance-Framework

---

## Vision
NHS Trusts and regulated organisations are under pressure to demonstrate AI
governance before deploying algorithmic systems, and most don't know where to
start. This project positions Kene as the person called at the start of an AI
programme, not after it has already gone wrong. Two linked assets: a governance
framework document an organisation can adopt directly, and a Streamlit
self-assessment tool that scores the organisation against it and generates a
PDF gap analysis, turning the framework into a lead generation asset.

---

## Scope
**In scope:**
- Framework document (python-docx), 8 sections, structured on NIST AI RMF's
  GOVERN/MAP/MEASURE/MANAGE functions
- References: NIST AI RMF 1.0 + Playbook, UK ICO AI guidance, NHS AI Lab
  algorithmic tools guidance, EU AI Act risk tiers, ISO/IEC 42001
- 40-question self-assessment (5 per dimension x 8 dimensions), scored 1-5
- Plotly radar chart: organisation score vs sector benchmark
- ReportLab PDF gap analysis report with prioritised recommendations
- Deploy to Streamlit Community Cloud

**Out of scope:**
- Any training dataset or ML model (this is a document + rules-based scoring tool)
- LLM/API integration (no .env keys required)
- Multi-tenant or persistent user accounts (single-session assessment only)

---

## Planned Architecture
See CLAUDE.md for the full folder structure and build order.

**Data flow:**
`framework_content.py` → `generate_framework.py` → `ai_governance_framework.docx`
`questions.json` → `app.py` (session_state) → `scoring.py` → radar chart + `report_generator.py` → PDF

---

## Decisions Log
- Each of the 8 framework sections has exactly one backbone source, chosen
  for being the most sector-neutral, legally binding option available, with
  sector-specific standards (DCB0129/0160, DTAC, MHRA) kept in clearly
  bounded "supporting reference" subsections rather than blended into the
  backbone prose. This makes a later per-client template (swap the health
  overlay for a finance or retail one) a trim, not a rewrite.
- Section 8's backbone is EU AI Act Articles 12, 18, and 19 (record-keeping,
  documentation retention, log retention), not ISO/IEC 42001. ISO 42001 was
  always meant to be the optional certification layer on top, confirmed by
  re-reading the placeholder note written when the reference library was
  built, not the legally binding spine.
- Assessment tool PDF uses ReportLab's built-in Times-Roman family, not
  Georgia/Cambria. Those are Microsoft-licensed fonts: fine for the Word
  document (python-docx just names them, Word renders using the reader's
  own licensed install), not safe to bundle as font files in a public repo,
  and unavailable on the Linux containers Streamlit Community Cloud deploys
  to.
- Top-gap ranking is pure numeric (benchmark minus score), not weighted by
  regulatory severity. The fintech test persona showed this can bury a
  narratively critical dimension (Bias and Fairness) behind others that
  are numerically larger but less urgent. Fixed by RAG-colouring the full
  8-dimension table, not just the top 3, so nothing red stays invisible.
- P9 and P10 (Data Maturity Assessment Tool) stay as two separately
  deployed apps rather than merging into one, since their scoring engines
  don't overlap and P9 is already live at a bookmarked URL. Added a
  lightweight cross-link instead: `init_session_state()` now reads `org`
  and `sector` from `st.query_params` so a link from P10 (or anywhere
  else) can pre-fill the sidebar. With no query params, behaviour is
  unchanged from before this change. Combined-report feature scoped
  separately as a later v2 idea, not built here.

---

## Assumptions
- The Playbook's suggested actions can be adapted into NHS/Civil Service-flavoured
  framework language without losing NIST's structural rigor.
- Sector benchmark scores in `sector_benchmarks.csv` are estimated/illustrative
  (no public dataset of AI governance maturity by sector exists) and should be
  labelled as such in the tool.
- 5 questions per dimension is enough resolution for a self-assessment without
  making the questionnaire too long to complete in one sitting.

---

## Open Questions
- [x] Where do the EU AI Act risk tier definitions come from? Extracted
      directly from the Regulation's own PDF (Articles 5, 6, 50), not a
      secondary summary. NHS clinical safety requirements come from
      DCB0129/DCB0160, not a generic "NHS AI Lab" source, that name was
      imprecise in the original brief.
- [x] Radar chart: user picks their sector from a sidebar selectbox,
      benchmark redraws against `data/sector_benchmarks.csv`.

---

## Blockers
- `gh` (GitHub CLI) is not installed on this machine, so the GitHub repo
  cannot be created and pushed to without either installing it or Kene
  creating the empty repo manually and sharing the remote URL.

---

## Discoveries During Build
- DTAC is a procurement checklist, not a risk classification scheme, it
  asks a supplier to attach a DPIA and clinical safety evidence, it doesn't
  score risk itself. Nearly became Section 2's backbone twice before this
  was caught by reading the actual document instead of assuming from its
  reputation.
- The `.gitignore` written at scaffold time had two live bugs: it excluded
  `.venv/` when the actual folder is `venv/` (would have committed the
  whole virtual environment), and it excluded `data/*.csv` (would have
  silently broken the deployed app, which loads `sector_benchmarks.csv`
  straight from the repo). Both caught and fixed before the first commit.
- DCB0160's severity scale starts at "Minor," not "Negligible" as assumed
  from memory before checking the actual implementation guidance PDF.

---

## Next Actions
- [x] Get the empty GitHub repo's remote URL from Kene (gh CLI still not
      installed on this machine, pushed via plain git instead)
- [x] Push local repo to `github.com/kenechukwuagbodike/AI-Governance-Framework`
- [x] Deploy `dashboard/app.py` to Streamlit Community Cloud
- [x] Fill in the live demo link in this file and in README.md
- [x] Fix deployment crash: kaleido 1.x needs Chrome, which Streamlit
      Cloud's container doesn't have by default. Added `packages.txt`
      (installs system Chromium) rather than downgrading kaleido, since
      the older 0.2.x line is deprecated and hung on this local machine
      when tested as an alternative. Verified fixed on the live app via
      a real browser session: downloaded an actual PDF, not just checked
      that the page loaded.
- [x] Both components of P9 are now built and live in one session: the
      framework document and the self-assessment tool.
- [x] Cross-link with P10 (query param pre-fill) built and verified
      locally with Streamlit's `AppTest` harness (no query params:
      unchanged behaviour; valid params: correct pre-fill; unmapped
      sector: safe fallback, no crash). Pushed and redeployed to
      Streamlit Community Cloud earlier than the original joint-release
      plan (Kene pushed directly rather than waiting on P10). Confirmed
      working on the live URL: base app loads normally, and
      `?org=Test+Org&sector=Healthcare+%2F+NHS` correctly pre-fills the
      sidebar. No functional risk since P10 isn't live yet to link to it,
      the feature is just sitting dormant slightly ahead of schedule.
- [ ] Deploy P10 to Streamlit Community Cloud, the one piece still
      outstanding before the pair is fully live together
      until that's done deliberately.

---

## Changelog
| Date | What shipped |
|------|-------------|
| 2026-07-13 | Project scaffolded, added to workspace |
| 2026-07-19 | Reference library built (33 sources, docs-extractor skill). All 8 framework sections written and cross-checked, two internal consistency gaps found and fixed (undefined "governance sponsor" role, missing Clinical Safety Case Report link). `generate_framework.py` renderer built, `.docx` generated. Full assessment tool built: `questions.json` (40 questions), `scoring.py`, `charts.py`, `report_generator.py`, `dashboard/app.py`. Navy/serif redesign applied to both deliverables: action titles instead of descriptive labels, RAG-coloured scores, state/cause/implication/action structure in the PDF gap section. Pressure-tested against 3 realistic client personas (FMCG, fintech startup, healthtech vendor), meaningfully differentiated results. `.gitignore` bugs fixed before first commit. Local git repo initialised. |
