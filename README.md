# AI Governance Framework + Self-Assessment Tool

> A ready-to-adopt AI governance framework (NIST AI RMF, NHS AI Lab, ICO, EU AI Act)
> and a self-assessment tool that scores your organisation against it.

Part of the [Data to Decisions](https://github.com/kenechukwuagbodike) portfolio by
Kene Agbodike, Data and AI Decision Systems Consultant.

---

## Overview

NHS Trusts, Civil Service departments, and regulated organisations are under
pressure to demonstrate AI governance before deploying algorithmic systems, and
most don't know where to start. This project delivers two linked assets:

1. **A governance framework document**, structured around NIST AI RMF's four
   functions (GOVERN, MAP, MEASURE, MANAGE) and covering 8 dimensions: AI
   inventory, risk classification, impact assessment, bias and fairness testing,
   data governance, human oversight, incident response, and audit trail.
2. **A Streamlit self-assessment tool** that scores an organisation across all
   8 dimensions, renders a maturity radar chart against sector benchmarks, and
   generates a downloadable PDF gap analysis report with prioritised
   recommendations.

Every clause in the framework document traces back to a primary source: the
EU AI Act, NIST AI RMF, UK GDPR, the Equality Act 2010, NHS DCB0129/DCB0160,
DTAC, the MHRA, and ICO guidance, drawn from a 33-document reference library,
not summarised secondhand. The 40 assessment questions are written directly
against those same clauses, not a generic maturity-model template.

Sector benchmark scores in the assessment tool are illustrative reference
points built to show directional gaps, not figures from a published industry
survey. That distinction is stated on the chart itself and in the PDF report,
not hidden in a footnote.

## Stack

`Python · Streamlit · python-docx · ReportLab · Plotly · pandas`

## Demo

<!-- Add links after deployment -->
- **Live demo:** Streamlit Community Cloud, link coming soon
- **Framework document:** downloadable from the live app

## Getting started

```bash
# Clone the repo
git clone https://github.com/kenechukwuagbodike/ai-governance-framework.git
cd ai-governance-framework

# Create virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1      # Windows PowerShell
# source .venv/bin/activate       # macOS / Linux

# Install dependencies
pip install -r requirements.txt
```

## Project structure

```
ai-governance-framework/
├── framework/       Framework document content + python-docx generator
├── assessment/      Question bank, scoring logic, PDF report generator
├── dashboard/       Streamlit app (app.py)
├── data/            Sector benchmark scores
├── requirements.txt
└── README.md
```

## Running the dashboard

```bash
streamlit run dashboard/app.py
```

## Generating the framework document

```bash
cd framework
python generate_framework.py
```

Renders `framework_content.py` into `ai_governance_framework.docx`. The
`.docx` itself is gitignored, regenerate it from source rather than editing
the output file directly.

## About

**Kene Agbodike**, Data and AI Decision Systems Consultant

Certifications: Microsoft Fabric Data Engineer Associate, Fabric Analytics
Engineer Associate, Azure Solutions Architect Expert, Azure AI Engineer,
Azure Data Scientist

[GitHub](https://github.com/kenechukwuagbodike) · [Upwork](https://www.upwork.com/freelancers/~01ffe0a90179159b67)
