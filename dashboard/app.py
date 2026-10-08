"""
AI Governance Readiness Assessment: Streamlit self-assessment tool.

Scores an organisation across the 8 dimensions of the AI Governance
Framework, compares against an illustrative sector benchmark, and
produces a downloadable PDF gap analysis report.
"""

import logging
import sys
from pathlib import Path
from urllib.parse import urlencode

import streamlit as st

sys.path.insert(0, str(Path(__file__).parent.parent / "assessment"))
import scoring  # noqa: E402
from charts import build_radar_chart  # noqa: E402
from report_generator import generate_report  # noqa: E402

P10_APP_URL = "https://keni-data-maturity-tool.streamlit.app"

# P9 and P10 score different sector benchmark sets with different naming.
# Maps a P9 sector onto its closest P10 equivalent so the cross-link can
# pre-fill the other tool's sector selector.
SECTOR_MAP_P9_TO_P10 = {
    "Healthcare / NHS": "NHS / Public Sector",
    "Financial Services": "Financial Services",
    "Retail / E-commerce": "Retail / E-commerce",
}


def build_p10_link(org_name: str, sector: str) -> str:
    params = {}
    if org_name:
        params["org"] = org_name
    mapped_sector = SECTOR_MAP_P9_TO_P10.get(sector)
    if mapped_sector:
        params["sector"] = mapped_sector
    query = f"?{urlencode(params)}" if params else ""
    return f"{P10_APP_URL}{query}"

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="AI Governance Readiness Assessment",
    page_icon="\U0001F9ED",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def get_questions_data() -> dict:
    return scoring.load_questions()


@st.cache_data
def get_benchmark_sectors() -> list[str]:
    return scoring.load_benchmarks()["sector"].tolist()


def init_session_state(questions_data: dict) -> None:
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "org_name" not in st.session_state:
        st.session_state.org_name = st.query_params.get("org", "")
    if "sector" not in st.session_state:
        st.session_state.sector = st.query_params.get("sector", "")


def render_assessment_tab(questions_data: dict) -> None:
    st.subheader("Answer each question on the 1 to 5 maturity scale")
    with st.expander("What do the scores mean?"):
        for level, label in questions_data["maturity_scale"].items():
            st.write(f"**{level}**: {label}")

    for dimension in questions_data["dimensions"]:
        st.markdown(f"### {dimension['number']}. {dimension['name']}")
        for question in dimension["questions"]:
            key = f"q_{question['id']}"
            default = st.session_state.answers.get(question["id"], 3)
            score = st.slider(
                question["text"],
                min_value=1,
                max_value=5,
                value=default,
                key=key,
            )
            st.session_state.answers[question["id"]] = score
        st.divider()

    answered = len(st.session_state.answers)
    total = sum(len(d["questions"]) for d in questions_data["dimensions"])
    st.progress(answered / total, text=f"{answered} of {total} questions answered")


def render_results_tab(questions_data: dict, sector: str) -> None:
    total_questions = sum(len(d["questions"]) for d in questions_data["dimensions"])
    if len(st.session_state.answers) < total_questions:
        st.info("Answer every question in the Assessment tab to see your results.")
        return

    result = scoring.score_all(st.session_state.answers)
    dimension_scores = result["dimension_scores"]
    overall = result["overall_score"]
    label = scoring.maturity_label(overall)
    benchmark_scores = scoring.get_benchmark_scores(sector)
    gaps = scoring.rank_gaps(dimension_scores, benchmark_scores, top_n=3)

    rag_colour = {"red": "red", "amber": "orange", "green": "green"}
    overall_colour = rag_colour[scoring.rag_band(overall)]
    st.markdown(f"## Overall maturity: :{overall_colour}[{overall} out of 5], {label}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Overall score", f"{overall} / 5", label)
    weakest = min(dimension_scores, key=dimension_scores.get)
    col2.metric("Weakest dimension", weakest, f"{dimension_scores[weakest]} / 5")
    strongest = max(dimension_scores, key=dimension_scores.get)
    col3.metric("Strongest dimension", strongest, f"{dimension_scores[strongest]} / 5")

    fig = build_radar_chart(dimension_scores, benchmark_scores, sector)
    st.plotly_chart(fig, width="stretch")
    st.caption(
        f"Source: self-reported assessment scores against the AI Governance Framework's "
        f"8 dimensions. {sector} benchmark is an illustrative reference point, not a "
        f"published industry survey."
    )

    st.markdown("### Scores by dimension")
    st.caption("Colour flags where the risk actually sits, not just the raw number.")
    for dimension, score in dimension_scores.items():
        colour = rag_colour[scoring.rag_band(score)]
        st.markdown(f"**{dimension}**: :{colour}[{score} / 5]")

    st.markdown("### Your top 3 gaps")
    for gap in gaps:
        colour = rag_colour[scoring.rag_band(gap["org_score"])]
        st.markdown(
            f"**{gap['dimension']}**: scoring :{colour}[{gap['org_score']}] against a "
            f"{gap['target_score']} reference point, a gap of {gap['gap']}."
        )

    st.markdown("### Download your report")
    org_name = st.session_state.org_name or "Your organisation"
    pdf_bytes = generate_report(org_name, sector, dimension_scores, overall, label, gaps)
    st.download_button(
        "Download PDF gap analysis report",
        data=pdf_bytes,
        file_name="ai_governance_gap_analysis.pdf",
        mime="application/pdf",
    )

    st.divider()
    p10_link = build_p10_link(st.session_state.org_name, sector)
    st.markdown(
        "### Before this, a prior question\n"
        "This score assumes a data foundation already exists for AI systems "
        "to run on. If that is not yet confirmed, the companion "
        f"[Data Maturity Assessment]({p10_link}) scores whether it does, "
        "the question to answer before this one."
    )


def main() -> None:
    st.title("AI Governance Readiness Assessment")
    st.caption(
        "Companion tool to the AI Governance Framework. Score your organisation "
        "across the same 8 dimensions the framework document is built on."
    )

    questions_data = get_questions_data()
    init_session_state(questions_data)

    st.sidebar.header("Your details")
    st.session_state.org_name = st.sidebar.text_input(
        "Organisation name (for your report)", value=st.session_state.org_name
    )
    sectors = get_benchmark_sectors()
    default_sector = st.session_state.sector if st.session_state.sector in sectors else sectors[0]
    sector = st.sidebar.selectbox(
        "Compare against sector", sectors, index=sectors.index(default_sector)
    )
    st.session_state.sector = sector

    tab1, tab2 = st.tabs(["Assessment", "Results & Report"])
    with tab1:
        render_assessment_tab(questions_data)
    with tab2:
        render_results_tab(questions_data, sector)


if __name__ == "__main__":
    main()
