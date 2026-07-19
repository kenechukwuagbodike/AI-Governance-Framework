"""
ReportLab PDF gap analysis report for the AI governance self-assessment.

Structure follows the workspace's consulting pack convention: state, then
cause and implication, then action, for each top gap, backed by a full
RAG-coloured scores table and the same radar chart shown in the dashboard.

Typography uses ReportLab's built-in Times-Roman family rather than
Georgia/Cambria. Those are Microsoft-licensed fonts: fine for the Word
document, where python-docx just names them and Word renders using
whatever's licensed on the reader's own machine, but not safe to bundle
as font files in a public repo, and not present at all on the Linux
containers Streamlit Community Cloud deploys to. Times-Roman ships with
ReportLab itself, so this renders identically everywhere without any
font file dependency.
"""

import io
import logging
from datetime import date

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,
)

from charts import build_radar_chart
from scoring import rag_band

logger = logging.getLogger(__name__)

NAVY = colors.HexColor("#14213D")
GREY = colors.HexColor("#666666")
LIGHT_GREY = colors.HexColor("#EEEEEE")
DARK = colors.HexColor("#1A1A1A")
RAG_COLOURS = {
    "red": colors.HexColor("#B3261E"),
    "amber": colors.HexColor("#B8860B"),
    "green": colors.HexColor("#2E7D32"),
}

HEADING_FONT = "Times-Bold"
BODY_FONT = "Times-Roman"

# One recommended action per dimension, grounded in the framework document's
# own content, not generic advice. Used whichever dimensions land in a given
# assessment's top gaps.
RECOMMENDED_ACTIONS = {
    "AI Inventory and Asset Register": (
        "Stand up a single register capturing ATRS-aligned fields, owner, "
        "purpose, deployment status, data sources, for every AI system in "
        "use, and assign a named owner to keep it current."
    ),
    "Risk Classification": (
        "Apply the EU AI Act's four-tier test to every system before "
        "deployment, and route anything touching patient care through "
        "DCB0160's severity and likelihood matrix in a Clinical Safety "
        "Case Report."
    ),
    "Impact Assessment": (
        "Complete a Data Protection Impact Assessment before build begins "
        "for any system meeting UK GDPR's high-risk triggers, and for "
        "health systems, close out all five DTAC domains with named "
        "accountable officers."
    ),
    "Bias and Fairness": (
        "Test outcomes against all nine Equality Act protected "
        "characteristics before deployment, watch for proxy variables "
        "rather than relying on removing protected fields, and document a "
        "proportionality case for any disparity found."
    ),
    "Data Governance": (
        "Document the lawful basis, minimisation rationale, and retention "
        "period before training data is collected, and assess AI-specific "
        "security risks, model inversion and membership inference, as part "
        "of the standard security review."
    ),
    "Human Oversight": (
        "Name and train a human overseer, distinct from the system owner, "
        "for every high-risk system, and actually test the stop or "
        "override procedure rather than leaving it as a written policy."
    ),
    "Incident Response": (
        "Stand up a live post-deployment monitoring process, and confirm "
        "in advance which of the EU AI Act's four serious incident "
        "categories would trigger an Article 73 report, and on what "
        "deadline."
    ),
    "Audit Trail and Reporting": (
        "Separate log retention, six months minimum, from technical "
        "documentation retention, ten years, and confirm records can "
        "actually be retrieved on request, not just claimed to exist."
    ),
}

# The consequence of leaving each dimension unaddressed, stated concretely
# enough that the recommended action reads as necessary, not optional.
CAUSE_AND_IMPLICATION = {
    "AI Inventory and Asset Register": (
        "Without a complete register, every other control in this "
        "framework has no reliable list of systems to apply to. A gap "
        "here is a gap everywhere else, even where the underlying "
        "practice is otherwise strong."
    ),
    "Risk Classification": (
        "An unclassified system defaults to being treated as low-risk by "
        "omission, exactly the failure mode that lets a genuinely "
        "high-risk system go live without the scrutiny the law requires."
    ),
    "Impact Assessment": (
        "Deploying a system without a completed impact assessment is "
        "itself a UK GDPR compliance failure the moment high-risk "
        "processing begins, not a paperwork delay that can be caught up "
        "on later."
    ),
    "Bias and Fairness": (
        "This is what turns into a Section 19 Equality Act discrimination "
        "claim, not just an internal audit finding, and the law does not "
        "require intent for that claim to succeed."
    ),
    "Data Governance": (
        "Undocumented lawful basis and retention decisions are exactly "
        "what a regulator asks for first, and exactly what is hardest to "
        "reconstruct convincingly after the fact."
    ),
    "Human Oversight": (
        "A high-risk system without a named, trained overseer fails "
        "Article 14 by design, regardless of how well the system itself "
        "performs technically."
    ),
    "Incident Response": (
        "Without a live post-deployment monitoring process, a two-day "
        "reporting deadline is unreachable in practice, the organisation "
        "will not know an incident happened in time to meet it."
    ),
    "Audit Trail and Reporting": (
        "Without retrievable records, none of the other seven dimensions "
        "can actually be evidenced when a regulator or a client asks for "
        "proof, however well they are actually being run day to day."
    ),
}


def build_styles() -> dict:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "ReportTitle", parent=base["Title"], fontName=HEADING_FONT,
            fontSize=22, textColor=NAVY, spaceAfter=4,
        ),
        "subtitle": ParagraphStyle(
            "ReportSubtitle", parent=base["Normal"], fontName=BODY_FONT,
            fontSize=11, textColor=GREY, spaceAfter=16,
        ),
        "h2": ParagraphStyle(
            "ReportH2", parent=base["Heading2"], fontName=HEADING_FONT,
            fontSize=14, textColor=NAVY, spaceBefore=16, spaceAfter=8,
        ),
        "body": ParagraphStyle(
            "ReportBody", parent=base["Normal"], fontName=BODY_FONT,
            fontSize=10, textColor=DARK, leading=14, spaceAfter=8,
            alignment=TA_JUSTIFY,
        ),
        "gap_state": ParagraphStyle(
            "GapState", parent=base["Normal"], fontName=HEADING_FONT,
            fontSize=11, textColor=DARK, spaceBefore=10, spaceAfter=4,
        ),
        "caption": ParagraphStyle(
            "Caption", parent=base["Normal"], fontName=BODY_FONT,
            fontSize=8, textColor=GREY, spaceAfter=4, alignment=TA_JUSTIFY,
        ),
    }


def build_scores_table(dimension_scores: dict, benchmark_scores: dict) -> Table:
    header = ["Dimension", "Your score", "Sector reference", "Gap"]
    rows = [header]
    rag_cells = []  # (row_index, band) for the "Your score" column
    for row_index, (dimension, score) in enumerate(dimension_scores.items(), start=1):
        benchmark = benchmark_scores.get(dimension, 0)
        gap = round(benchmark - score, 2)
        rows.append([dimension, f"{score:.1f}", f"{benchmark:.1f}", f"{gap:+.1f}"])
        rag_cells.append((row_index, rag_band(score)))

    table = Table(rows, colWidths=[8.5 * cm, 2.5 * cm, 3 * cm, 2 * cm])
    style_commands = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), HEADING_FONT),
        ("FONTNAME", (0, 1), (-1, -1), BODY_FONT),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.white),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    for row_index, band in rag_cells:
        style_commands.append(("TEXTCOLOR", (1, row_index), (1, row_index), RAG_COLOURS[band]))
        style_commands.append(("FONTNAME", (1, row_index), (1, row_index), HEADING_FONT))
    table.setStyle(TableStyle(style_commands))
    return table


def build_radar_image(dimension_scores: dict, benchmark_scores: dict, sector: str) -> Image:
    fig = build_radar_chart(dimension_scores, benchmark_scores, sector)
    png_bytes = fig.to_image(format="png", width=900, height=600, scale=2)
    return Image(io.BytesIO(png_bytes), width=15 * cm, height=10 * cm)


def generate_report(
    org_name: str,
    sector: str,
    dimension_scores: dict,
    overall_score: float,
    maturity_label: str,
    gaps: list[dict],
) -> bytes:
    styles = build_styles()
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        topMargin=2 * cm, bottomMargin=2 * cm,
        leftMargin=2 * cm, rightMargin=2 * cm,
    )
    from scoring import get_benchmark_scores
    benchmark_scores = get_benchmark_scores(sector)

    overall_band = rag_band(overall_score)
    story = []
    story.append(Paragraph("AI Governance Gap Analysis", styles["title"]))
    story.append(Paragraph(
        f"{org_name}  |  Benchmarked against {sector}  |  {date.today():%d %B %Y}",
        styles["subtitle"],
    ))

    overall_style = ParagraphStyle(
        "OverallScore", parent=styles["h2"], textColor=RAG_COLOURS[overall_band],
    )
    story.append(Paragraph(
        f"Overall maturity: {overall_score:.1f} out of 5, {maturity_label}.",
        overall_style,
    ))
    story.append(Paragraph(
        "This score reflects self-reported answers against the AI Governance "
        "Framework's 8 dimensions. It is a starting point for prioritising "
        "governance work, not a certification or a regulator's assessment.",
        styles["body"],
    ))

    story.append(build_radar_image(dimension_scores, benchmark_scores, sector))
    story.append(Paragraph(
        f"{sector} reference points are illustrative, built to show directional "
        "gaps, not drawn from a published industry survey.",
        styles["caption"],
    ))

    story.append(Paragraph("Scores by dimension", styles["h2"]))
    story.append(build_scores_table(dimension_scores, benchmark_scores))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Top gaps and recommended actions", styles["h2"]))
    for gap in gaps:
        dimension = gap["dimension"]
        band = rag_band(gap["org_score"])
        state_style = ParagraphStyle(
            "GapStateBand", parent=styles["gap_state"], textColor=RAG_COLOURS[band],
        )
        story.append(Paragraph(
            f"{dimension}: scoring {gap['org_score']:.1f} against a "
            f"{gap['target_score']:.1f} reference point, a gap of {gap['gap']:.1f}.",
            state_style,
        ))
        cause = CAUSE_AND_IMPLICATION.get(dimension)
        if cause:
            story.append(Paragraph(cause, styles["body"]))
        action = RECOMMENDED_ACTIONS.get(
            dimension, "Review this dimension against the framework document's relevant section."
        )
        story.append(Paragraph(f"Recommended action: {action}", styles["body"]))

    story.append(Spacer(1, 16))
    story.append(Paragraph(
        "See the AI Governance Framework document for the full detail, source "
        "references, and ownership model behind each of the 8 dimensions above.",
        styles["caption"],
    ))

    doc.build(story)
    logger.info("Generated PDF report for %s (%s)", org_name, sector)
    return buffer.getvalue()
