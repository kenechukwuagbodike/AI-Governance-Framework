# P9: AI Governance Framework + Self-Assessment Tool

## What this project does
Two linked deliverables for NHS Trusts, Civil Service departments, and regulated
industries adopting AI without a governance structure: (1) a governance framework
document generated with python-docx, structured around NIST AI RMF's four functions
(GOVERN, MAP, MEASURE, MANAGE) and referencing UK ICO guidance, NHS AI Lab standards,
EU AI Act risk tiers, and ISO/IEC 42001; (2) a Streamlit self-assessment tool scoring
an organisation across 8 dimensions matching the framework's sections, producing a
Plotly radar chart and a ReportLab PDF gap analysis report.

This project does not use a training dataset. There is no model to build. The
framework content is derived from the five standards named above, not from data.

## Folder structure
```
ai-governance-framework/
├── framework/
│   ├── generate_framework.py       python-docx: generates the framework .docx
│   ├── framework_content.py        All section text and tables as Python data
│   └── ai_governance_framework.docx  Output document (gitignored)
├── assessment/
│   ├── questions.json              40 questions across 8 dimensions, scored 1-5
│   ├── scoring.py                  Maturity scoring logic + benchmark lookup
│   └── report_generator.py         ReportLab: PDF gap analysis report
├── dashboard/
│   └── app.py                      Streamlit: multi-page self-assessment UI
├── data/
│   └── sector_benchmarks.csv       NHS/finance/retail benchmark scores per dimension
├── .env.example
├── requirements.txt
└── README.md
```

## The 8 framework sections (map to the 8 assessment dimensions)
1. AI Inventory and Asset Register
2. Risk Classification (EU AI Act tiers)
3. Impact Assessment
4. Bias and Fairness Testing
5. Data Governance Requirements
6. Human Oversight Model
7. Incident Response Playbook
8. Audit Trail and Reporting

## Build order
1. `framework/framework_content.py`: write all 8 sections' content, drawing on
   NIST AI RMF 1.0 (structure, subcategory wording, trustworthiness characteristics)
   and the AI RMF Playbook (suggested actions per subcategory). Add EU AI Act risk
   tiers and NHS AI Lab clinical safety requirements where the NIST material doesn't
   cover them (Sections 2 and 4).
2. `framework/generate_framework.py`: python-docx script that renders
   `framework_content.py` into the 20-25 page .docx.
3. `assessment/questions.json`: 40 questions, 5 per dimension, scored 1 (not started)
   to 5 (fully embedded).
4. `assessment/scoring.py`: dimension scores, overall maturity score, gap list.
5. `dashboard/app.py`: multi-page Streamlit, session_state question tracking,
   Plotly radar chart (org vs sector benchmark from `data/sector_benchmarks.csv`).
6. `assessment/report_generator.py`: ReportLab PDF, embeds the radar chart, scores
   table, top 3 gaps, recommended actions.
7. Deploy to Streamlit Community Cloud. Write README. Commit.

## Writing style (mandatory)
- No em dashes anywhere: not in code comments, dashboard text, insight panels,
  PDF exports, framework document text, README, or any client-facing copy.
- Use a colon, comma, or rewrite the sentence instead.
- This rule applies to every file generated or edited in this project.

## Session start checklist
1. Read this file
2. Read PROJECT.md: current status, open questions, next actions
3. Activate venv: `.venv\Scripts\Activate.ps1`
4. Check which build step is next in PROJECT.md → Next Actions
5. Build → run → commit
