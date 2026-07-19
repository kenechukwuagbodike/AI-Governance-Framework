"""
Content for the AI Governance Framework document.

FRAMEWORK_SECTIONS is a list of section dicts, built up one at a time, not
generated in bulk. Each section names its own backbone source (the one
primary reference that gives it teeth) plus supporting references. One
backbone per section, everything else is a footnote, not a co-author.

Section 1 sources: ATRS guidance for public sector bodies (the field
taxonomy) and NIST AI RMF GOVERN 1.6 / 1.7 (the case for having an
inventory at all). Full source list: library/references.json.

Sections 2-8 come next, one at a time.
"""

FRAMEWORK_TITLE = "AI Governance Framework"
FRAMEWORK_SUBTITLE = (
    "A structured approach to AI risk management, aligned to NIST AI RMF, "
    "UK ICO guidance, NHS AI Lab standards, the EU AI Act, and ISO/IEC 42001"
)

INTRODUCTION = {
    "big_idea": (
        "NHS Trusts and Civil Service departments are being asked to prove AI "
        "governance before they have any internal capability to build it. This "
        "framework is that capability, ready to adopt on day one of an AI "
        "programme, not reconstructed after an incident has already happened."
    ),
    "body": [
        (
            "This framework gives an organisation a working structure for governing "
            "AI systems across their lifecycle: what exists, what risk it carries, "
            "who is accountable, and how the organisation responds when something "
            "goes wrong. It is built around the four functions of the NIST AI Risk "
            "Management Framework (AI RMF 1.0): Govern, Map, Measure, and Manage. "
            "Govern sets the policies and accountability structures the other three "
            "functions depend on. Map establishes context and identifies risk before "
            "deployment. Measure tests systems against defined criteria. Manage "
            "prioritises and responds to what Measure finds."
        ),
        (
            "Eight sections follow. Each one is built on a single primary source, "
            "not a blend of everything available: the Algorithmic Transparency "
            "Recording Standard for the asset register, the EU AI Act and the NHS "
            "Digital Technology Assessment Criteria for risk classification, the "
            "Equality Act 2010 for bias testing, UK GDPR for data governance, the "
            "ICO's guidance on explaining AI decisions for human oversight, and so "
            "on. NIST provides the skeleton underneath all eight. Where a section "
            "draws on more than its backbone source, that is named explicitly, not "
            "implied."
        ),
        (
            "This is a working document, not a compliance certificate. Adopting it "
            "does not, by itself, satisfy any regulator. It gives an organisation "
            "the structure to demonstrate, when asked, that AI risk is being "
            "managed deliberately, not discovered after an incident."
        ),
    ],
}

FRAMEWORK_SECTIONS = [
    {
        "number": 1,
        "title": "AI Inventory and Asset Register",
        "nist_function": "GOVERN",
        "backbone": "Algorithmic Transparency Recording Standard (ATRS), UK Government",
        "supporting_refs": "NIST AI RMF GOVERN 1.6, GOVERN 1.7",
        "big_idea": (
            "An organisation that cannot list its AI systems cannot govern them. "
            "The register is the foundation every other section depends on, and "
            "its fields come from the UK government's own public transparency "
            "standard, not from a blank page."
        ),
        "subsections": [
            {
                "heading": "Purpose",
                "body": [
                    (
                        "The AI asset register answers the question every "
                        "governance review starts with: what AI do we use, and "
                        "where? Without it, risk classification, impact assessment, "
                        "and incident response all have no starting point. A system "
                        "that is not on the register is a system nobody is "
                        "governing, whether or not anyone intended that."
                    ),
                    (
                        "This register is not the same document as an Algorithmic "
                        "Transparency Recording Standard (ATRS) record. ATRS is a "
                        "public-facing publication, required for central government "
                        "departments and recommended more widely, built once a tool "
                        "is live and its governance is already understood. This "
                        "register comes first: it is how an organisation works out "
                        "which systems will need an ATRS record, a Data Protection "
                        "Impact Assessment, or a specific risk tier, before any of "
                        "that work begins. Its fields are drawn from ATRS's own "
                        "structure on purpose, so that completing this register "
                        "early makes the later public record faster to produce, not "
                        "a second exercise starting from nothing."
                    ),
                ],
            },
            {
                "heading": "What to capture per system",
                "body": [
                    "Each entry in the register should record:",
                ],
                "bullets": [
                    "System name and a plain-language description of what it does (ATRS Tier 1 fields: name, description)",
                    "Senior responsible owner, recorded as a role title rather than a named individual, for continuity when staff change (ATRS's own convention for its SRO field)",
                    "Third parties or suppliers involved in building or operating the system, and their role in the supply chain (ATRS Tier 2, third party involvement)",
                    "Purpose and intended users (ATRS Tier 2, detailed description)",
                    "Deployment status: in development, piloting, live, or decommissioned",
                    "Risk tier (see Section 2), assigned before deployment and reviewed on the schedule below",
                    "Data sources feeding the system, and whether any of them contain personal or special category data",
                    "Whether the system falls within the mandatory scope of the ATRS policy, and if so, the date its public ATRS record was published or is due",
                    "Date of last impact assessment and date of next scheduled review",
                ],
            },
            {
                "heading": "Ownership and review cadence",
                "body": [
                    (
                        "One named individual or team owns the register itself, "
                        "distinct from the owners of individual systems. That owner "
                        "keeps entries current and chases outstanding reviews. They "
                        "do not approve what goes into production, that decision "
                        "belongs to the governance sponsor named in Section 6."
                    ),
                    (
                        "High-risk systems are reviewed at least every six months. "
                        "Limited-risk systems annually. Minimal-risk systems on "
                        "addition and whenever their use case changes. A system that "
                        "changes purpose, changes its training data source, or "
                        "starts processing a new category of data is treated as a "
                        "new entry requiring a fresh risk classification, not an "
                        "update to the old one."
                    ),
                ],
            },
            {
                "heading": "Decommissioning",
                "body": [
                    (
                        "Removing a system from production does not remove it from "
                        "the register. Decommissioned systems are marked as such "
                        "and retained for the organisation's standard data "
                        "retention period, because a decommissioned system can "
                        "still be the subject of a complaint, a subject access "
                        "request, or a regulatory inquiry about a decision it made "
                        "while live."
                    ),
                    (
                        "Before decommissioning, the system owner documents where "
                        "its outputs are still relied upon downstream and confirms "
                        "that removing it will not silently break another process."
                    ),
                ],
            },
        ],
    },
    {
        "number": 2,
        "title": "Risk Classification",
        "nist_function": "MAP",
        "backbone": "EU AI Act, Regulation (EU) 2024/1689, Articles 5, 6, and 50",
        "supporting_refs": "NHS DCB0160 clinical risk matrix (Implementation Guidance v4.2, Table 9); NIST AI RMF MAP 1.1",
        "big_idea": (
            "Risk classification is the decision every later section depends on. "
            "Get it wrong and a chatbot inherits the compliance programme built "
            "for a triage system, or a triage system gets waved through like a "
            "chatbot. The EU AI Act gives a defensible four-tier structure that "
            "holds outside healthcare as well as inside it. DCB0160 gives the "
            "precision a Trust needs once a system lands in the high-risk tier."
        ),
        "subsections": [
            {
                "heading": "Purpose",
                "body": [
                    (
                        "Section 1 gave every AI system a place on the register. "
                        "This section gives it a risk tier, because an FAQ "
                        "chatbot and a system dispatching emergency ambulances "
                        "do not belong under the same governance regime, and "
                        "treating them as though they do wastes effort on the "
                        "first and under-protects the second."
                    ),
                    (
                        "The risk tier field added to the register in Section 1 "
                        "is filled in here, before deployment, not after."
                    ),
                ],
            },
            {
                "heading": "The four tiers",
                "body": [],
                "bullets": [
                    (
                        "Unacceptable risk: prohibited outright. Article 5 lists "
                        "eight practices banned regardless of context, among "
                        "them social scoring of people over time, emotion "
                        "inference in workplaces or schools, and real-time "
                        "remote biometric identification in public spaces for "
                        "law enforcement, permitted only in narrow, listed "
                        "circumstances such as searching for a missing person or "
                        "a specific terrorist threat. A system in this tier is "
                        "not built, not piloted, not procured."
                    ),
                    (
                        "High-risk: permitted, inside a formal compliance "
                        "regime. Article 6 sets two routes in. The first: the "
                        "system is a safety component of a product already "
                        "regulated under EU law and needs third-party conformity "
                        "assessment, medical device software is the clearest "
                        "healthcare example. The second: the use case appears on "
                        "Annex III's list, which includes recruitment and worker "
                        "evaluation, access to essential public services and "
                        "benefits including healthcare, credit scoring, and "
                        "emergency call triage and dispatch. A system in this "
                        "tier triggers the full impact assessment in Section 3, "
                        "not an optional version of it."
                    ),
                    (
                        "Limited risk: permitted, with a duty to disclose. "
                        "Article 50 covers systems that interact directly with "
                        "people or generate synthetic content. A chatbot has to "
                        "make clear it's a chatbot, unless that's already "
                        "obvious. Deepfakes have to be labelled as artificially "
                        "generated. The obligation here is honesty with the "
                        "person on the other end of the interaction, not a "
                        "safety case."
                    ),
                    (
                        "Minimal risk: the residual category. Anything not "
                        "caught by Articles 5, 6, or 50 carries no obligation "
                        "under the Act itself. That is not the same as no "
                        "governance: it still needs the register entry and named "
                        "owner from Section 1, and it moves to a higher tier the "
                        "moment its purpose or data sources change."
                    ),
                ],
            },
            {
                "heading": "The clinical layer, for systems touching patient care",
                "body": [
                    (
                        "Landing in the EU AI Act's high-risk tier because a "
                        "system touches healthcare tells a Trust that heavier "
                        "obligations apply. It does not tell a Clinical Safety "
                        "Officer how severe a specific hazard is, or whether a "
                        "specific failure mode is tolerable. That is what "
                        "DCB0160 adds underneath the Act's tier, not instead of "
                        "it."
                    ),
                    (
                        "DCB0160's implementation guidance scores each "
                        "identified hazard on two scales: severity, from Minor "
                        "to Catastrophic, and likelihood, from Very Low to Very "
                        "High. The two scores combine on a five-by-five matrix "
                        "into a risk rating of 1 to 5. A rating of 4 or 5 is "
                        "treated as unacceptable and needs mitigation before "
                        "deployment; a rating of 3 is undesirable and needs a "
                        "documented reason if it isn't reduced further; 1 and 2 "
                        "are acceptable."
                    ),
                    (
                        "NHS Digital is explicit that this particular scale is "
                        "an example, not a mandate: \"It is for the Health "
                        "Organisation to decide on the classifications to use "
                        "for the deployment of a Health IT System.\" Where a "
                        "Trust already has its own Clinical Risk Management Plan "
                        "with an established scale, that scale governs, not this "
                        "one. Where it doesn't, this framework adopts DCB0160's "
                        "example matrix as the default."
                    ),
                    (
                        "This scoring doesn't stay in a spreadsheet. DCB0160 "
                        "requires it recorded in a Clinical Safety Case "
                        "Report, produced for each lifecycle phase and "
                        "approved by the Clinical Safety Officer. That report "
                        "is the artefact Section 3's DTAC assessment draws on "
                        "for its clinical safety domain, and the one Section "
                        "7's post-deployment monitoring checks against when a "
                        "safety concern is reported."
                    ),
                ],
            },
            {
                "heading": "Who assigns it, and when",
                "body": [
                    (
                        "The system owner named in the register proposes a tier "
                        "before build begins, using the criteria above. The "
                        "governance sponsor named in Section 6 confirms it "
                        "before deployment, or the Data Protection Officer where "
                        "personal data is involved. Re-classification follows "
                        "the same triggers set in Section 1: a change of "
                        "purpose, a new data source, or a new category of data "
                        "processed all mean the tier gets reassessed, not "
                        "assumed to still be correct."
                    ),
                ],
            },
            {
                "heading": "What this classification does not do",
                "body": [
                    (
                        "Assigning a tier is not compliance. It is the decision "
                        "that determines which later sections apply, and how "
                        "heavily. Unacceptable means stop. High-risk means "
                        "Section 3's impact assessment and Section 6's human "
                        "oversight duties are mandatory, not advisory. Limited "
                        "risk means only the disclosure duties in Section 6 "
                        "apply. Minimal risk means the register entry from "
                        "Section 1 is enough on its own, for now."
                    ),
                ],
            },
        ],
    },
    {
        "number": 3,
        "title": "Impact Assessment",
        "nist_function": "MAP",
        "backbone": "ICO Guidance on AI and Data Protection, Data Protection Impact Assessments chapter",
        "supporting_refs": "NHS DTAC, 5 assessment criteria (Digital Technology Assessment Criteria); UK GDPR Article 35; NIST AI RMF MAP 5.1",
        "big_idea": (
            "A risk tier tells you how much scrutiny a system needs. The impact "
            "assessment is where that scrutiny actually happens. UK GDPR already "
            "requires one the moment AI processing is likely to create high risk "
            "to people's rights, in any sector. DTAC turns the same discipline "
            "into an NHS procurement gate, with a named officer accountable for "
            "each domain."
        ),
        "subsections": [
            {
                "heading": "Purpose",
                "body": [
                    (
                        "Section 2 decided which systems carry enough risk to "
                        "need close scrutiny before deployment. This section is "
                        "that scrutiny. Under Article 35(3)(a) of UK GDPR, a "
                        "Data Protection Impact Assessment is legally required "
                        "wherever AI use involves systematic and extensive "
                        "evaluation of personal aspects that produces legal or "
                        "similarly significant effects, large-scale processing "
                        "of special category data, or systematic monitoring of "
                        "public areas at scale. Most systems that land in "
                        "Section 2's high-risk tier will meet one of these "
                        "conditions anyway, but the DPIA duty is triggered by "
                        "the processing itself, not by the EU AI Act tier, so "
                        "the two assessments run on separate legal grounds even "
                        "when they cover the same system."
                    ),
                    (
                        "Do it at the start of the project, not once the system "
                        "is built. A DPIA written after deployment is a "
                        "retrospective justification, not a risk assessment."
                    ),
                ],
            },
            {
                "heading": "What the assessment has to cover",
                "body": [
                    (
                        "Describe the processing first: what data moves where, "
                        "how much of it, where it came from, and how much "
                        "human involvement sits in the decision-making step, "
                        "including whether a human can actually overturn the "
                        "system's output or just rubber-stamps it. Then assess "
                        "necessity and proportionality: what problem the system "
                        "solves, why a less intrusive approach wasn't enough, "
                        "and what trade-off was made between accuracy and data "
                        "minimisation."
                    ),
                    (
                        "Then identify the risks to people, and here the ICO "
                        "draws a distinction worth keeping separate rather than "
                        "folding into one generic \"bias\" line: allocative "
                        "harm is a system distributing opportunity unfairly, "
                        "a recruitment tool that rates male candidates as "
                        "suitable more often than equally qualified women is "
                        "an allocative harm, someone loses a job opportunity. "
                        "Representational harm is a system reinforcing "
                        "stereotypes without allocating anything: an image "
                        "recognition system labelling someone's holiday photos "
                        "with racist tropes causes no financial loss and no "
                        "denied opportunity, but it is still a documented harm "
                        "under this guidance, and the assessment has to name it "
                        "as one."
                    ),
                    (
                        "For each risk identified, record what mitigates it, "
                        "whether the mitigation reduces the risk or eliminates "
                        "it, and what residual risk remains after the "
                        "mitigation is applied. If residual risk is still high "
                        "and can't be reduced further, the organisation must "
                        "consult the ICO before the processing goes ahead. That "
                        "is not optional and not a formality."
                    ),
                ],
            },
            {
                "heading": "The procurement gate, for health systems",
                "body": [
                    (
                        "DTAC does not replace the DPIA. It is the checklist "
                        "that confirms one exists and is attached before a "
                        "Trust buys the product. DTAC assesses across five "
                        "domains, each with its own named accountable officer: "
                        "clinical safety (chief clinical information officer or "
                        "equivalent, drawing on the Clinical Safety Officer's "
                        "DCB0129/DCB0160 case from Section 2), data protection "
                        "(the DPO, evidenced by the DPIA itself), technical "
                        "security (chief information security officer), "
                        "interoperability (chief information officer), and "
                        "usability and accessibility (chief technology "
                        "officer)."
                    ),
                    (
                        "A supplier who cannot produce a DPIA when the DTAC "
                        "form asks for one has failed the assessment, not left "
                        "a field blank."
                    ),
                ],
            },
            {
                "heading": "Who owns it, and when",
                "body": [
                    (
                        "The system owner from the register drafts the DPIA "
                        "before build begins, not the DPO, though the DPO must "
                        "be involved early enough that their opinion isn't a "
                        "surprise at the point of sign-off. In a health "
                        "setting, each DTAC domain gets signed off by the "
                        "accountable officer named above, not by whoever filled "
                        "in the form. The assessment is reviewed on the same "
                        "trigger conditions as the register and the risk tier: "
                        "a change of purpose, a new data source, or a new "
                        "category of data processed all mean the DPIA is "
                        "revisited, not assumed to still hold."
                    ),
                ],
            },
            {
                "heading": "What this does not do",
                "body": [
                    (
                        "A completed DPIA is not permission to skip the EU AI "
                        "Act obligations that came with the tier assigned in "
                        "Section 2, and a completed DTAC form is not a "
                        "substitute for either. The three run in parallel and "
                        "cover different legal grounds. A high-risk system "
                        "still needs all three before it goes live."
                    ),
                ],
            },
        ],
    },
    {
        "number": 4,
        "title": "Bias and Fairness",
        "nist_function": "MEASURE",
        "backbone": "Equality Act 2010, Sections 13, 19, and 149",
        "supporting_refs": "ICO Guidance on AI and Data Protection, fairness/bias/Article 22 chapter; NIST AI RMF MEASURE 2.11",
        "big_idea": (
            "An AI system does not need to use a protected characteristic as an "
            "input to discriminate against the people who share it. Section 19 "
            "of the Equality Act catches any provision, criterion or practice, "
            "an algorithm's decision logic included, that puts a protected "
            "group at a disadvantage, whether or not anyone intended that. "
            "Testing for it means proxy-aware bias testing, not a checklist "
            "confirming race and sex were dropped from the training data."
        ),
        "subsections": [
            {
                "heading": "Purpose",
                "body": [
                    (
                        "The Equality Act gives two routes to discrimination. "
                        "Direct discrimination, Section 13, is treating someone "
                        "less favourably because of a protected characteristic: "
                        "age, disability, gender reassignment, marriage and "
                        "civil partnership, pregnancy and maternity, race, "
                        "religion or belief, sex, sexual orientation. Most AI "
                        "systems never do this deliberately, so it's rarely the "
                        "one that catches them."
                    ),
                    (
                        "Indirect discrimination, Section 19, is the one that "
                        "does. It applies to \"a provision, criterion or "
                        "practice\" that disadvantages people who share a "
                        "protected characteristic compared to those who don't, "
                        "unless the organisation can show it's a proportionate "
                        "means of achieving a legitimate aim. A scoring model, "
                        "a filtering rule, a ranking algorithm: each of those "
                        "is a provision, criterion or practice. The Act does "
                        "not require intent, and it does not require the "
                        "system to have used the protected characteristic at "
                        "all. It only requires the outcome to land unevenly."
                    ),
                ],
            },
            {
                "heading": "Why removing protected characteristics doesn't fix this",
                "body": [
                    (
                        "The instinct is to strip race, sex, and age out of "
                        "the training data and call the model fair. The ICO "
                        "calls this fairness through unawareness, and it "
                        "doesn't work. Discrimination can occur even when the "
                        "training data contains no protected characteristics "
                        "at all, because other features correlate with them in "
                        "non-obvious ways. Occupation correlates with sex. "
                        "Postcode correlates with race. These proxy variables "
                        "let a model reproduce the same discriminatory pattern "
                        "a protected characteristic would have produced, "
                        "without ever touching the characteristic itself. "
                        "Removing the obvious fields and stopping there is "
                        "the failure mode, not the fix."
                    ),
                    (
                        "This is also where Section 3 connects back in: "
                        "testing for discriminatory impact by ethnic origin "
                        "processes special category data, and needs to be "
                        "accounted for in the DPIA. Testing by age does not, "
                        "since age is a protected characteristic under the "
                        "Equality Act but not special category data under UK "
                        "GDPR. The two lists overlap, they aren't the same "
                        "list."
                    ),
                ],
            },
            {
                "heading": "What to test, and how often",
                "body": [
                    (
                        "Test outcomes against each of the nine protected "
                        "characteristics before deployment, not just the ones "
                        "that seem obviously relevant to the use case. A "
                        "hiring model gets tested for age and disability "
                        "impact even if nobody expected either to matter. If "
                        "a disparity turns up, the organisation needs a "
                        "documented, evidenced case that the system is a "
                        "proportionate means of achieving a legitimate aim, "
                        "not an assertion that the model is accurate. "
                        "Accuracy and fairness are different questions; a "
                        "highly accurate model can still be systematically "
                        "unfair to a protected group."
                    ),
                    (
                        "Where a system makes a solely automated decision with "
                        "a legal or similarly significant effect on someone, "
                        "Article 22 of UK GDPR adds its own layer: the person "
                        "has a right to meaningful information about the "
                        "logic involved and a route to contest the decision. "
                        "Build that route before deployment, not after the "
                        "first complaint."
                    ),
                    (
                        "Retest on the same triggers as everything else in "
                        "this framework: retraining, a new data source, or a "
                        "change in what the system is used for. A bias test "
                        "result has a shelf life. It describes the model as "
                        "it existed on the day it was tested, not as it "
                        "exists after the next retrain."
                    ),
                ],
            },
            {
                "heading": "The public sector duty",
                "body": [
                    (
                        "For NHS Trusts, government departments, and any "
                        "supplier delivering a public function under "
                        "contract, Section 149 adds an obligation that goes "
                        "beyond not discriminating. A public authority must "
                        "have \"due regard\" to eliminating discrimination, "
                        "advancing equality of opportunity, and fostering "
                        "good relations between people who share a protected "
                        "characteristic and those who don't. This is a "
                        "positive duty to show the equality impact was "
                        "actively considered before the system went live, not "
                        "just a defence to raise if someone complains "
                        "afterwards. A private-sector client only has to "
                        "avoid discriminating. A public-sector one has to "
                        "show its working."
                    ),
                ],
            },
            {
                "heading": "Who owns it, and when",
                "body": [
                    (
                        "The system owner commissions the bias test before "
                        "deployment, using the protected characteristics list "
                        "above as the minimum scope. Results, including any "
                        "disparity found and the proportionality case made "
                        "for it, are recorded alongside the DPIA from Section "
                        "3, not as a separate, disconnected exercise. For "
                        "public-sector deployments, the Section 149 due "
                        "regard assessment is signed off by the same "
                        "governance sponsor named in Section 6."
                    ),
                ],
            },
            {
                "heading": "What this does not do",
                "body": [
                    (
                        "A clean bias test at launch is not a permanent "
                        "clearance. Proxy relationships shift as data drifts, "
                        "and a model retrained on six months of new data can "
                        "develop a disparity the original test never saw. "
                        "The proportionate-means defence is not automatic "
                        "either: it has to be evidenced with a genuine "
                        "comparison against less discriminatory alternatives, "
                        "not asserted because the deployer believes the "
                        "system is fair."
                    ),
                ],
            },
        ],
    },
    {
        "number": 5,
        "title": "Data Governance",
        "nist_function": "GOVERN",
        "backbone": "UK GDPR, Article 5 (data protection principles)",
        "supporting_refs": (
            "ICO Guidance on AI and Data Protection, minimisation/accuracy/"
            "security chapters; Data Protection Act 2018; NIST AI RMF "
            "GOVERN 4.1, MAP 2.3"
        ),
        "big_idea": (
            "Data governance for AI is not a data quality checklist bolted "
            "onto a machine learning project once. It is UK GDPR's six data "
            "protection principles applied continuously across the AI "
            "lifecycle, training, inference, and every prediction made about "
            "someone who was never in the training set to begin with."
        ),
        "subsections": [
            {
                "heading": "Purpose",
                "body": [
                    (
                        "Six principles govern how personal data is handled "
                        "under UK GDPR: lawfulness, fairness and transparency; "
                        "purpose limitation; data minimisation; accuracy; "
                        "storage limitation; and security and accountability. "
                        "None of them are AI-specific. All of them get harder "
                        "to satisfy once the data is feeding a model instead "
                        "of a spreadsheet."
                    ),
                    (
                        "The principle that catches people out: a model built "
                        "from training data continues to process personal "
                        "data every time it makes a prediction, even about "
                        "someone who was never part of that training data. "
                        "Data protection law doesn't stop applying once "
                        "training finishes and deployment begins, it applies "
                        "again, to a different set of people, on every "
                        "inference the live system makes."
                    ),
                ],
            },
            {
                "heading": "Minimisation and storage limitation",
                "body": [
                    (
                        "Collect what the system needs, not what might be "
                        "useful later. Data kept on the chance it could "
                        "become valuable is processing without a purpose, "
                        "and processing without a purpose isn't lawful "
                        "regardless of how carefully it's stored. The same "
                        "logic applies to retention: keeping training data "
                        "or inference logs past the point the system needs "
                        "them is unnecessary processing, not caution."
                    ),
                    (
                        "This doesn't mean an AI system can't process "
                        "personal data at all, that reading of minimisation "
                        "makes the principle unworkable and gets ignored. It "
                        "means being able to say, for this specific use case, "
                        "why this field is adequate, relevant, and limited to "
                        "what the system actually needs, and for how long."
                    ),
                ],
            },
            {
                "heading": "Accuracy, and why it means two different things here",
                "body": [
                    (
                        "Data accuracy is the ordinary meaning: the record "
                        "reflects the real, current fact. Statistical "
                        "accuracy is a separate question: whether the "
                        "model's output is correct often enough, on average, "
                        "across the population it was tested on. A model can "
                        "be statistically accurate and still be wrong about a "
                        "specific person in a way that harms them, average "
                        "correctness doesn't guarantee correctness for the "
                        "individual in front of it. Both kinds of inaccuracy "
                        "need documenting, and they need different fixes: bad "
                        "input data gets corrected, a model with an "
                        "acceptable aggregate error rate that's still wrong "
                        "too often for one group gets retrained or scoped "
                        "differently, which is where this section meets "
                        "Section 4's bias testing rather than duplicating it."
                    ),
                ],
            },
            {
                "heading": "Security: the training data can leak back out",
                "body": [
                    (
                        "AI introduces a security risk that a normal database "
                        "doesn't have: the trained model itself can expose "
                        "the data it learned from. In a model inversion "
                        "attack, an attacker who already holds some personal "
                        "data about people in the training set can query the "
                        "model and infer more, a documented case involved a "
                        "clinical dosage-prediction model where an attacker "
                        "with partial demographic data could infer patients' "
                        "genetic biomarkers, without ever touching the "
                        "underlying training data. In a membership inference "
                        "attack, an attacker doesn't learn new facts about a "
                        "person, only whether that person's data was in the "
                        "training set at all, inferred from how confidently "
                        "the model responds to them. A documented facial "
                        "recognition case reconstructed training-set faces "
                        "from confidence scores alone, matched to real "
                        "individuals with 95% accuracy by human reviewers."
                    ),
                    (
                        "This means the model file is part of what needs "
                        "securing, not just the database it was trained "
                        "from. Treating a trained model as a harmless "
                        "artefact because it \"only contains weights\" is the "
                        "mistake both of these attacks exploit."
                    ),
                ],
            },
            {
                "heading": "Accountability and individual rights",
                "body": [
                    (
                        "Where a system involves more than one organisation, "
                        "a supplier and a Trust, for instance, accountability "
                        "for each part of the processing needs allocating "
                        "explicitly between them. An accountability gap, "
                        "where neither party is clearly responsible for a "
                        "specific piece of processing, tends to surface at "
                        "the worst moment: when someone tries to exercise a "
                        "right and nobody is sure whose job it is to respond."
                    ),
                    (
                        "Individual rights, erasure, restriction, objection, "
                        "apply throughout the AI lifecycle, not just to the "
                        "original dataset. Build the process for handling "
                        "these requests before the system goes live. The "
                        "route to contest a decision, required under Section "
                        "4's Article 22 discussion, depends on this same "
                        "underlying capability."
                    ),
                ],
            },
            {
                "heading": "Who owns it, and when",
                "body": [
                    (
                        "The system owner documents the lawful basis, the "
                        "minimisation rationale, and the retention period "
                        "before data collection for training begins, not "
                        "after a model already exists trained on it. The DPO "
                        "signs off before that data is assembled. Every new "
                        "data source added to a live system re-triggers this "
                        "section's questions, adding a field to a database "
                        "is not exempt just because the system it feeds was "
                        "already governed."
                    ),
                ],
            },
            {
                "heading": "What this does not do",
                "body": [
                    (
                        "Signing off the training data once does not cover "
                        "what gets added later. A system that starts "
                        "processing a new category of data, or draws from a "
                        "new source, needs this section run again for that "
                        "addition specifically, not folded quietly into the "
                        "existing sign-off because the system as a whole was "
                        "already approved."
                    ),
                ],
            },
        ],
    },
    {
        "number": 6,
        "title": "Human Oversight",
        "nist_function": "MANAGE",
        "backbone": "EU AI Act, Regulation (EU) 2024/1689, Article 14 (Human oversight)",
        "supporting_refs": (
            "ICO + The Alan Turing Institute, Explaining Decisions Made with "
            "AI (six explanation types); NIST AI RMF MANAGE 2.2, MANAGE 4.1"
        ),
        "big_idea": (
            "A stop button nobody's been trained to use isn't oversight, and "
            "neither is a reviewer who can't correctly interpret what the "
            "system just told them. Article 14 sets the legal floor for what "
            "oversight has to look like on a high-risk system. The ICO's "
            "explanation types are what turn Article 14's requirement to "
            "\"correctly interpret the output\" into something a reviewer can "
            "actually do."
        ),
        "subsections": [
            {
                "heading": "Purpose",
                "body": [
                    (
                        "This section applies to systems that landed in "
                        "Section 2's high-risk tier, not to every system on "
                        "the register. Article 14 requires those systems to "
                        "be built so they \"can be effectively overseen by "
                        "natural persons during the period in which they are "
                        "in use.\" The aim is to prevent or minimise risks "
                        "that persist even after every other safeguard in "
                        "this framework has been applied, oversight is the "
                        "last line, not the only one, and it exists because "
                        "the other lines aren't assumed to be perfect."
                    ),
                ],
            },
            {
                "heading": "What oversight actually requires",
                "body": [
                    (
                        "Article 14(4) sets out five things a named human "
                        "overseer has to be able to do, not just be told they "
                        "can do:"
                    ),
                ],
                "bullets": [
                    "Understand the system's capacities and limitations well enough to monitor it, including spotting anomalies, dysfunction, or performance that's drifted from what was expected",
                    "Stay alert to automation bias, the well-documented tendency to over-rely on a system's output simply because it came from the system, particularly where the AI is producing recommendations for a human to act on",
                    "Correctly interpret the output, not just receive it",
                    "Decide, in a specific situation, not to use the system, or to disregard, override, or reverse what it produced",
                    "Intervene or stop the system through a stop button or equivalent procedure that brings it to a safe halt",
                ],
            },
            {
                "heading": "The two-person rule for biometric identification",
                "body": [
                    (
                        "For remote biometric identification systems "
                        "specifically, Article 14(5) goes further than the "
                        "general requirements above: no action may be taken "
                        "on the strength of an identification the system "
                        "produced unless it has been separately verified and "
                        "confirmed by at least two people with the necessary "
                        "competence, training, and authority. One trained "
                        "reviewer is not enough for this category, by design. "
                        "The exception is narrow: certain law enforcement, "
                        "migration, border control, and asylum uses, where "
                        "the law itself treats the two-person requirement as "
                        "disproportionate."
                    ),
                    (
                        "Oversight measures generally are supposed to be "
                        "commensurate with the risk, autonomy, and context of "
                        "the system, not maximal by default. The two-person "
                        "rule is the exception that proves that principle: "
                        "it exists specifically because a wrong biometric "
                        "match carries consequences a single reviewer's "
                        "judgement isn't trusted to catch alone."
                    ),
                ],
            },
            {
                "heading": "Making \"correctly interpret the output\" real",
                "body": [
                    (
                        "Article 14 requires correct interpretation but "
                        "doesn't say how to achieve it. The ICO and the Alan "
                        "Turing Institute's joint guidance does: it sets out "
                        "six explanation types, rationale (the reasons "
                        "behind a decision, in plain language), "
                        "responsibility (who built and manages the system, "
                        "and who to contact for a human review), data (what "
                        "data fed a specific decision), fairness (what steps "
                        "were taken to keep the system unbiased, and whether "
                        "this person was treated equitably), safety and "
                        "performance (accuracy, reliability, and robustness), "
                        "and impact (what effect the system's use has on the "
                        "individual and on wider society)."
                    ),
                    (
                        "These were written primarily for explaining a "
                        "decision to the person it affects, but a human "
                        "overseer needs the same clarity, just aimed inward "
                        "instead of outward. Which explanation matters most "
                        "depends on context: a safety-critical system needs "
                        "its safety and performance explanation prioritised, "
                        "a system operating where bias is a live concern "
                        "needs the fairness explanation foregrounded, and a "
                        "medical diagnosis context tends to need the impact "
                        "and safety explanations ahead of the rationale. An "
                        "overseer trained to expect the wrong explanation "
                        "type for the context they're working in is no more "
                        "equipped than one given no explanation at all."
                    ),
                ],
            },
            {
                "heading": "Who owns it, and when",
                "body": [
                    (
                        "The human overseer is a named, trained, authorised "
                        "role, not \"whoever is free to check it.\" Naming "
                        "the role happens before deployment, alongside the "
                        "system owner from Section 1, and the two are not "
                        "necessarily the same person: the system owner is "
                        "accountable for the system existing responsibly, "
                        "the overseer is the person actually watching it "
                        "run. For the two-person biometric rule, both named "
                        "reviewers need to be independently competent, not "
                        "one expert and one nominal sign-off."
                    ),
                    (
                        "A third role sits above both of these, and it's the "
                        "one the rest of this framework leans on repeatedly: "
                        "the governance sponsor. This is the senior, named "
                        "individual who confirms risk tiers under Section 2, "
                        "signs off Section 4's public sector equality duty "
                        "assessments, and gets told the moment Section 7's "
                        "incident-reporting clock starts running. The system "
                        "owner runs a system. The overseer watches it "
                        "operate. The governance sponsor is accountable for "
                        "the AI governance programme as a whole, and is the "
                        "single point everyone above escalates to when a "
                        "decision needs authority the other two roles don't "
                        "carry."
                    ),
                ],
            },
            {
                "heading": "What this does not do",
                "body": [
                    (
                        "A stop button that exists on paper is not oversight "
                        "if nobody has been trained to use it under pressure. "
                        "A provider building oversight measures into the "
                        "system under Article 14(3)(a) does not discharge the "
                        "deployer's own obligation to implement the "
                        "complementary measures under 14(3)(b), the two are "
                        "meant to work together, not substitute for each "
                        "other. And no amount of oversight rigour fixes a "
                        "system that was misclassified in Section 2, "
                        "oversight manages risk in a correctly tiered system, "
                        "it doesn't correct the tiering."
                    ),
                ],
            },
        ],
    },
    {
        "number": 7,
        "title": "Incident Response",
        "nist_function": "MANAGE",
        "backbone": "EU AI Act, Regulation (EU) 2024/1689, Article 73 (Reporting of serious incidents)",
        "supporting_refs": (
            "NHS DCB0160, Specification v3.2, Section 7.2 (post-deployment "
            "monitoring, Safety Incident Management Log); MHRA Yellow Card "
            "scheme; NIST AI RMF MANAGE 4.1, MANAGE 4.3"
        ),
        "big_idea": (
            "A serious incident doesn't wait for the next governance "
            "committee meeting. Article 73 starts a clock the moment one "
            "happens, graded by severity: fifteen days for most, two for "
            "critical infrastructure or widespread harm, ten if someone "
            "died. DCB0160 supplies the thing that has to already exist "
            "before that clock is even readable: a live log that catches "
            "the incident in the first place."
        ),
        "subsections": [
            {
                "heading": "Purpose",
                "body": [
                    (
                        "Article 73 applies to high-risk systems, the tier "
                        "assigned in Section 2, and only to what the Act "
                        "defines as a serious incident: death or serious harm "
                        "to a person's health, a serious and irreversible "
                        "disruption to the management or operation of "
                        "critical infrastructure, an infringement of EU law "
                        "protecting fundamental rights, or serious harm to "
                        "property or the environment. Not every malfunction "
                        "qualifies. A model producing a wrong but low-stakes "
                        "recommendation is a defect to fix, not a serious "
                        "incident to report, the four categories above are "
                        "the actual test, not a general sense that something "
                        "went badly."
                    ),
                ],
            },
            {
                "heading": "The reporting clock",
                "body": [
                    (
                        "Once a provider has established a causal link "
                        "between the AI system and the incident, or judges "
                        "one reasonably likely, the report goes in. The "
                        "default deadline is fifteen days from becoming "
                        "aware of the incident. That shrinks to two days for "
                        "a widespread infringement or a critical "
                        "infrastructure disruption, and extends slightly, to "
                        "ten days, where someone has died, reflecting how "
                        "much more there usually is to establish before the "
                        "causal picture is clear."
                    ),
                    (
                        "The Act does not expect a finished report inside "
                        "that window. An incomplete initial report, followed "
                        "by a complete one, is explicitly allowed, the clock "
                        "measures when the regulator gets told, not when the "
                        "investigation finishes. After reporting, the "
                        "provider still has to investigate without delay: a "
                        "risk assessment of the incident, corrective action, "
                        "and cooperation with the competent authority. One "
                        "constraint matters more than it looks: the system "
                        "cannot be altered in a way that would affect the "
                        "investigation before the authorities have been told "
                        "about that change. Fixing the problem before "
                        "reporting it is not a shortcut, it's evidence "
                        "tampering under this Article."
                    ),
                ],
            },
            {
                "heading": "What has to exist before the clock starts",
                "body": [
                    (
                        "A two-day deadline is meaningless if nobody notices "
                        "the incident for three weeks. DCB0160's Section 7.2 "
                        "is what makes Article 73's clock achievable for a "
                        "health system: it requires a Health Organisation to "
                        "establish, document, and maintain a process for "
                        "collecting and reviewing safety concerns after "
                        "deployment, not just before it. Every incident "
                        "collected this way gets assessed against the "
                        "Clinical Safety Case built in Section 2, and where "
                        "it undermines that case, corrective action is "
                        "mandatory, recorded in a Safety Incident Management "
                        "Log kept separately from the pre-deployment Hazard "
                        "Log."
                    ),
                    (
                        "DCB0160 doesn't put a day-count on this the way "
                        "Article 73 does, it requires incidents to be "
                        "\"reported and resolved in a timely manner,\" which "
                        "is a judgement call, not a deadline. The two "
                        "standards operate at different levels on purpose: "
                        "DCB0160 makes sure the organisation is actually "
                        "watching, Article 73 tells it exactly how fast to "
                        "move once something serious turns up."
                    ),
                ],
            },
            {
                "heading": "External reporting channels for health systems",
                "body": [
                    (
                        "A single incident involving a medical device or "
                        "software as a medical device can trigger more than "
                        "one reporting duty at once, and none of them "
                        "substitutes for the others. Healthcare professionals "
                        "report device-related adverse incidents to the MHRA "
                        "through the Yellow Card scheme, that's the external, "
                        "regulator-facing channel, separate from the "
                        "Trust's own Safety Incident Management Log and "
                        "separate again from any Article 73 report the "
                        "system's provider owes because it's classified as "
                        "high-risk under the Act. A Trust that files a "
                        "Yellow Card report and stops there has not met an "
                        "Article 73 obligation the provider might still owe, "
                        "and logging the incident internally satisfies "
                        "neither external duty on its own."
                    ),
                ],
            },
            {
                "heading": "Who owns it, and when",
                "body": [
                    (
                        "The human overseer from Section 6 is usually the "
                        "first person positioned to notice a candidate "
                        "incident, that's what their duty to monitor for "
                        "anomalies and dysfunction is for. They flag it. The "
                        "system owner from Section 1 then owns the "
                        "assessment against the four-category test above, "
                        "the Safety Incident Management Log entry, and "
                        "initiating whichever external report applies, "
                        "inside whichever deadline applies. Once a causal "
                        "link is established or looks reasonably likely, the "
                        "governance sponsor named in Section 6 gets told "
                        "before the clock runs out, not after the report has "
                        "already gone."
                    ),
                ],
            },
            {
                "heading": "What this does not do",
                "body": [
                    (
                        "Filing the Article 73 report does not close the "
                        "incident, the investigation, risk assessment, and "
                        "corrective action obligations continue afterward. "
                        "And a serious incident is not a closed line item "
                        "once it's logged, it's one of the triggers from "
                        "Section 2 that forces the system's risk "
                        "classification to be reassessed, not assumed to "
                        "still hold."
                    ),
                ],
            },
        ],
    },
    {
        "number": 8,
        "title": "Audit Trail and Reporting",
        "nist_function": "GOVERN",
        "backbone": (
            "EU AI Act, Regulation (EU) 2024/1689, Articles 12, 18, and 19 "
            "(Record-keeping, Documentation keeping, Automatically "
            "generated logs)"
        ),
        "supporting_refs": (
            "ISO/IEC 42001:2023 PDCA structure, via ISO's public explainer "
            "and BSI's certification brochure; NIST AI RMF GOVERN 1.2, "
            "MANAGE 4.1"
        ),
        "big_idea": (
            "An audit trail is not a ninth document invented at the end of "
            "a build. It is Sections 1 through 7's own outputs, retained "
            "for however long the law actually requires, and that turns "
            "out to be two very different numbers depending on what's being "
            "kept."
        ),
        "subsections": [
            {
                "heading": "Purpose",
                "body": [
                    (
                        "This section has two jobs. The first: when a "
                        "regulator, a board, or a client asks an "
                        "organisation to prove its AI governance was real "
                        "and not retrospective, the audit trail is the "
                        "evidence. The second: when something does go wrong, "
                        "the trail is what makes Section 7's investigation "
                        "possible instead of speculative, root-cause analysis "
                        "needs a record of what the system actually did, not "
                        "a memory of what someone thinks it did."
                    ),
                ],
            },
            {
                "heading": "Two different clocks",
                "body": [
                    (
                        "Article 12 requires high-risk systems to technically "
                        "support automatic recording of events over their "
                        "lifetime. The logging has to capture enough to "
                        "identify a situation where the system is presenting "
                        "a risk, support the post-market monitoring duty, and, "
                        "closing the loop back to Section 6, record the "
                        "identity of the people who carried out the "
                        "two-person verification under Article 14(5) where "
                        "that applies."
                    ),
                    (
                        "Article 19 then sets the retention floor for those "
                        "logs: at least six months, longer if other law, "
                        "including data protection law, requires it. Article "
                        "18 covers a different artefact entirely, the "
                        "technical documentation itself: the system's "
                        "specification, its quality management system "
                        "records, its conformity assessment decisions. That "
                        "gets kept for ten years after the system reaches "
                        "market. Six months for the logs, ten years for the "
                        "documentation. Treating those as the same "
                        "obligation, or assuming one retention period covers "
                        "both, is the most common way this section gets got "
                        "wrong in practice."
                    ),
                ],
            },
            {
                "heading": "What actually goes in the trail",
                "body": [
                    (
                        "Nothing here is produced from scratch. The trail is "
                        "what Sections 1 through 7 already generated, kept "
                        "and made accessible: the register entry and "
                        "assigned risk tier, the DPIA and any DTAC evidence, "
                        "the bias test results and the proportionality case "
                        "made for any disparity found, the data governance "
                        "sign-off, the named human oversight role and its "
                        "interpretation records, and the Safety Incident "
                        "Management Log together with any Article 73 reports "
                        "filed. If a section of this framework didn't "
                        "produce a record, this section has nothing to "
                        "retain for it, which is itself a sign that section "
                        "wasn't actually followed."
                    ),
                ],
            },
            {
                "heading": "The optional layer: certification",
                "body": [
                    (
                        "Nothing in this framework requires ISO/IEC 42001 "
                        "certification. Sections 1 through 7 satisfy the "
                        "underlying legal obligations on their own. "
                        "Certification is a credibility layer on top, useful "
                        "for an organisation that wants third-party "
                        "assurance to show customers or regulators, not a "
                        "compliance requirement in itself. For organisations "
                        "that do want it, ISO 42001's Plan-Do-Check-Act "
                        "structure gives a recognised wrapper around "
                        "everything above: policy and leadership commitment, "
                        "implementing the management system requirements, "
                        "performance evaluation, and continual improvement. "
                        "BSI's own certification journey, assess, plan, "
                        "train, implement, certify, maintain, is one "
                        "practical route through it."
                    ),
                ],
            },
            {
                "heading": "Who owns it, and when",
                "body": [
                    (
                        "Retention and access are owned centrally, distinct "
                        "from whoever produced each individual record, "
                        "because the trail only works if someone can "
                        "actually find the DPIA from eighteen months ago "
                        "when a regulator asks for it. The trail itself "
                        "needs securing under Section 5's principles, not "
                        "just retaining, a hazard log and a DPIA both "
                        "contain exactly the kind of sensitive information "
                        "Section 5 already said the model's training data "
                        "needs protecting."
                    ),
                ],
            },
            {
                "heading": "What this does not do",
                "body": [
                    (
                        "Keeping records for the legal minimum does not "
                        "automatically satisfy Section 5's storage "
                        "limitation principle if the personal data inside "
                        "those records is no longer needed for its original "
                        "purpose. Where Article 19's six-month floor and "
                        "UK GDPR's minimisation instinct point in different "
                        "directions, the longer retention period governs for "
                        "that specific data, Article 19 says so explicitly, "
                        "but that means someone has to actually check which "
                        "one is longer for each record, not default to "
                        "whichever is more convenient to apply."
                    ),
                ],
            },
        ],
    },
]

REFERENCES = [
    "Algorithmic Transparency Recording Standard: Guidance for Public Sector "
    "Bodies, Government Digital Service.",
    "NIST AI 100-1, Artificial Intelligence Risk Management Framework "
    "(AI RMF 1.0), National Institute of Standards and Technology, January 2023.",
    "NIST AI RMF Playbook, National Institute of Standards and Technology.",
    "Regulation (EU) 2024/1689 of the European Parliament and of the Council "
    "of 13 June 2024 laying down harmonised rules on artificial intelligence "
    "(Artificial Intelligence Act).",
    "Clinical Risk Management: its Application in the Deployment and Use of "
    "Health IT Systems, Implementation Guidance v4.2, NHS Digital, "
    "2 May 2018 (DCB0160).",
    "Clinical Risk Management: its Application in the Deployment and Use of "
    "Health IT Systems, Specification v3.2, NHS Digital, 2 May 2018 (DCB0160).",
    "Guidance on AI and Data Protection, Information Commissioner's Office.",
    "Digital Technology Assessment Criteria (DTAC), NHS England / NHS Digital.",
    "Equality Act 2010, c. 15.",
    "UK General Data Protection Regulation (UK GDPR), retained EU law as "
    "amended, and the Data Protection Act 2018, c. 12.",
    "Explaining Decisions Made with AI, Information Commissioner's Office "
    "and The Alan Turing Institute.",
    "Software and Artificial Intelligence (AI) as a Medical Device, "
    "Medicines and Healthcare products Regulatory Agency (MHRA).",
    "ISO/IEC 42001:2023, Information technology, Artificial intelligence, "
    "Management system, International Organization for Standardization "
    "(public explainer and overview pages; standard itself not licensed "
    "for this project, see library notes).",
    "AI management system certification ISO/IEC 42001, BSI.",
]
