#!/usr/bin/env python3
"""
Texas Habeas Corpus Questionnaire Generator
Generates a PDF intake questionnaire for potential clients seeking
postconviction relief under Texas Code of Criminal Procedure
Articles 11.07, 11.072, 11.08, and 11.09
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY


def create_text_field(width=5*inch):
    """Create a blank line for text input"""
    return "_" * int(width / 6)


def create_checkbox():
    """Create a checkbox symbol"""
    return "[ ]"


def build_questionnaire(filename="texas_habeas_questionnaire.pdf"):
    """Build the complete habeas questionnaire PDF"""

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=6,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )

    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=12,
        alignment=TA_CENTER,
        textColor=colors.gray
    )

    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=12,
        spaceBefore=16,
        spaceAfter=8,
        textColor=colors.darkblue,
        borderPadding=4,
        backColor=colors.lightgrey
    )

    subsection_style = ParagraphStyle(
        'SubsectionHeader',
        parent=styles['Heading3'],
        fontSize=11,
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.black
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=4,
        leading=14
    )

    question_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=2,
        spaceBefore=6,
        leading=12
    )

    instruction_style = ParagraphStyle(
        'Instruction',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=8,
        textColor=colors.gray,
        alignment=TA_JUSTIFY
    )

    field_style = ParagraphStyle(
        'Field',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        leading=18
    )

    checkbox_style = ParagraphStyle(
        'Checkbox',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=2,
        leftIndent=20,
        leading=14
    )

    story = []

    # Title
    story.append(Paragraph("TEXAS HABEAS CORPUS QUESTIONNAIRE", title_style))
    story.append(Paragraph("Postconviction Relief Intake Form", subtitle_style))
    story.append(Paragraph(
        "Texas Code of Criminal Procedure Articles 11.07, 11.072, 11.08, 11.09",
        subtitle_style
    ))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.darkblue))
    story.append(Spacer(1, 12))

    # Instructions
    story.append(Paragraph("INSTRUCTIONS", section_style))
    story.append(Paragraph(
        """This questionnaire is designed to gather information necessary to evaluate
        your potential habeas corpus case. Please complete all sections as thoroughly
        as possible. Your answers are confidential and protected by attorney-client
        privilege. If you do not know an answer, write "Unknown." If a question does
        not apply to your situation, write "N/A." Attach additional pages if needed.""",
        instruction_style
    ))
    story.append(Paragraph(
        """<b>IMPORTANT:</b> This questionnaire does not create an attorney-client
        relationship. Submitting this form does not guarantee representation.
        Time limits (statutes of limitations) may apply to your case. Do not delay
        in seeking legal assistance.""",
        instruction_style
    ))

    # Section 1: Personal Information
    story.append(Paragraph("SECTION 1: PERSONAL INFORMATION", section_style))

    fields_1 = [
        ("Full Legal Name:", 4.5),
        ("Other Names Used (aliases, maiden name):", 4.5),
        ("Date of Birth:", 2),
        ("TDCJ Number (if applicable):", 2.5),
        ("SID Number:", 2.5),
        ("Current Location/Facility:", 4),
        ("Current Mailing Address:", 5),
        ("City, State, ZIP:", 4),
        ("Phone Number:", 2.5),
        ("Email Address:", 3.5),
        ("Emergency Contact Name:", 3),
        ("Emergency Contact Phone:", 2.5),
        ("Emergency Contact Relationship:", 2.5),
    ]

    for label, width in fields_1:
        story.append(Paragraph(
            f"{label} {'_' * int(width * 10)}",
            field_style
        ))

    # Section 2: Type of Relief Sought
    story.append(Paragraph("SECTION 2: TYPE OF RELIEF SOUGHT", section_style))
    story.append(Paragraph(
        "Check all that apply to your situation:",
        question_style
    ))

    relief_types = [
        ("Art. 11.07", "Felony conviction - currently incarcerated or completed sentence"),
        ("Art. 11.072", "Felony conviction - currently on community supervision (probation)"),
        ("Art. 11.08", "Felony charge - pretrial detention (not yet convicted)"),
        ("Art. 11.09", "Misdemeanor charge - pretrial detention (not yet convicted)"),
    ]

    for code, description in relief_types:
        story.append(Paragraph(
            f"[ ] <b>{code}</b> - {description}",
            checkbox_style
        ))

    # Section 3: Case Information
    story.append(Paragraph("SECTION 3: CASE INFORMATION", section_style))
    story.append(Paragraph("Primary Case (the conviction/charge you are challenging):", subsection_style))

    case_fields = [
        ("Case/Cause Number:", 3),
        ("Court (e.g., 299th District Court):", 4),
        ("County:", 2.5),
        ("Offense(s) Charged/Convicted:", 5),
        ("Date of Arrest:", 2.5),
        ("Date of Indictment/Information:", 2.5),
        ("Date of Plea or Trial:", 2.5),
        ("Type of Proceeding:", 0),
    ]

    for label, width in case_fields:
        if width > 0:
            story.append(Paragraph(
                f"{label} {'_' * int(width * 10)}",
                field_style
            ))
        else:
            story.append(Paragraph(label, question_style))

    story.append(Paragraph("[ ] Guilty Plea    [ ] Jury Trial    [ ] Bench Trial (Judge)", checkbox_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Sentence Received:", question_style))

    sentence_fields = [
        ("Prison Term:", 2),
        ("Probation Term:", 2),
        ("Fine Amount: $", 2),
        ("Restitution: $", 2),
        ("Date Sentence Imposed:", 2.5),
    ]

    for label, width in sentence_fields:
        story.append(Paragraph(
            f"    {label} {'_' * int(width * 10)}",
            field_style
        ))

    story.append(Paragraph("[ ] Sentence Enhanced (prior convictions)    [ ] Deadly Weapon Finding", checkbox_style))
    story.append(Paragraph("[ ] Sex Offender Registration Required    [ ] Deferred Adjudication", checkbox_style))

    # Section 4: Prior Criminal History
    story.append(PageBreak())
    story.append(Paragraph("SECTION 4: PRIOR CRIMINAL HISTORY", section_style))
    story.append(Paragraph(
        "List ALL prior convictions (attach additional pages if needed):",
        instruction_style
    ))

    prior_table_data = [
        ["Year", "Offense", "County/State", "Sentence", "Case Number"],
        ["____", "_" * 20, "_" * 15, "_" * 12, "_" * 15],
        ["____", "_" * 20, "_" * 15, "_" * 12, "_" * 15],
        ["____", "_" * 20, "_" * 15, "_" * 12, "_" * 15],
        ["____", "_" * 20, "_" * 15, "_" * 12, "_" * 15],
    ]

    prior_table = Table(prior_table_data, colWidths=[0.6*inch, 2*inch, 1.3*inch, 1.2*inch, 1.5*inch])
    prior_table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(prior_table)

    # Section 5: Trial Attorney Information
    story.append(Paragraph("SECTION 5: TRIAL ATTORNEY INFORMATION", section_style))

    atty_fields = [
        ("Trial Attorney's Name:", 4),
        ("Attorney's Phone:", 3),
        ("Attorney's Address:", 5),
        ("Was attorney:", 0),
    ]

    for label, width in atty_fields:
        if width > 0:
            story.append(Paragraph(
                f"{label} {'_' * int(width * 10)}",
                field_style
            ))
        else:
            story.append(Paragraph(label, question_style))

    story.append(Paragraph("[ ] Retained (hired)    [ ] Court-appointed    [ ] Public Defender", checkbox_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Rate your satisfaction with trial attorney's representation:", question_style))
    story.append(Paragraph("[ ] Very Satisfied    [ ] Satisfied    [ ] Unsatisfied    [ ] Very Unsatisfied", checkbox_style))

    # Section 6: Appeal Information
    story.append(Paragraph("SECTION 6: APPEAL INFORMATION", section_style))
    story.append(Paragraph("Did you file a direct appeal? [ ] Yes    [ ] No", question_style))

    appeal_fields = [
        ("If yes, Court of Appeals Case Number:", 3),
        ("Appellate Attorney's Name:", 3.5),
        ("Date of Appeals Court Decision:", 2.5),
        ("Result of Appeal:", 4),
    ]

    for label, width in appeal_fields:
        story.append(Paragraph(
            f"{label} {'_' * int(width * 10)}",
            field_style
        ))

    story.append(Paragraph("Did you file a Petition for Discretionary Review (PDR) to the Texas Court of Criminal Appeals?", question_style))
    story.append(Paragraph("[ ] Yes    [ ] No    [ ] Don't Know", checkbox_style))
    story.append(Paragraph(f"If yes, PDR Case Number: {'_' * 30}", field_style))
    story.append(Paragraph(f"Date of CCA Decision: {'_' * 30}", field_style))

    # Section 7: Prior Habeas Applications
    story.append(Paragraph("SECTION 7: PRIOR HABEAS CORPUS APPLICATIONS", section_style))
    story.append(Paragraph(
        "<b>CRITICAL:</b> Texas law generally limits applicants to ONE state habeas application. "
        "Prior applications may affect your ability to file.",
        instruction_style
    ))

    story.append(Paragraph("Have you previously filed a state habeas corpus application (Art. 11.07)?", question_style))
    story.append(Paragraph("[ ] Yes    [ ] No", checkbox_style))

    prior_habeas_fields = [
        "If yes, provide the following for EACH prior application:",
        ("Writ Number:", 3),
        ("Date Filed:", 2.5),
        ("Claims Raised:", 5),
        ("Result (granted/denied/dismissed):", 3),
        ("Date of Final Decision:", 2.5),
    ]

    story.append(Paragraph(prior_habeas_fields[0], question_style))
    for item in prior_habeas_fields[1:]:
        story.append(Paragraph(
            f"    {item[0]} {'_' * int(item[1] * 10)}",
            field_style
        ))

    story.append(Paragraph("Have you filed a federal habeas corpus petition (28 U.S.C. 2254)?", question_style))
    story.append(Paragraph("[ ] Yes    [ ] No", checkbox_style))
    story.append(Paragraph(f"If yes, Federal Case Number: {'_' * 30}    Result: {'_' * 20}", field_style))

    # Section 8: Grounds for Relief
    story.append(PageBreak())
    story.append(Paragraph("SECTION 8: GROUNDS FOR RELIEF", section_style))
    story.append(Paragraph(
        "Check ALL grounds that may apply to your case. You will explain each in detail below.",
        instruction_style
    ))

    grounds = [
        ("Ineffective Assistance of Trial Counsel", "Attorney failed to properly investigate, prepare, or represent you"),
        ("Ineffective Assistance of Appellate Counsel", "Appellate attorney failed to raise meritorious issues on appeal"),
        ("Actual Innocence", "You are factually innocent of the crime"),
        ("Newly Discovered Evidence", "New evidence exists that was not available at trial"),
        ("False or Misleading Evidence", "Prosecution used false testimony or fabricated evidence"),
        ("Brady Violation", "Prosecution withheld favorable evidence"),
        ("Prosecutorial Misconduct", "Improper conduct by the prosecutor"),
        ("Illegal Sentence", "Sentence exceeds legal limits or was improperly calculated"),
        ("Involuntary Plea", "Guilty plea was not knowing, voluntary, or intelligent"),
        ("Plea Bargain Violation", "State or court failed to honor plea agreement"),
        ("Jury Misconduct", "Improper jury deliberations or outside influences"),
        ("Ineffective Counsel During Plea", "Attorney gave incorrect advice about plea consequences"),
        ("Denial of Right to Counsel", "Denied attorney at critical stage"),
        ("Other Constitutional Violation", "Other violation of state or federal constitution"),
    ]

    for ground, description in grounds:
        story.append(Paragraph(
            f"[ ] <b>{ground}</b><br/>     <i>{description}</i>",
            checkbox_style
        ))

    # Section 9: Detailed Explanation
    story.append(Paragraph("SECTION 9: DETAILED EXPLANATION OF CLAIMS", section_style))
    story.append(Paragraph(
        """For EACH ground checked above, provide a detailed explanation. Include: (1) what
        happened, (2) when it happened, (3) who was involved, (4) what evidence supports
        your claim, and (5) how you were harmed. Use additional pages as needed.""",
        instruction_style
    ))

    for i in range(1, 4):
        story.append(Paragraph(f"<b>Claim {i}:</b>", question_style))
        story.append(Paragraph(f"Ground: {'_' * 50}", field_style))
        story.append(Paragraph("Explanation:", question_style))
        for _ in range(6):
            story.append(Paragraph("_" * 80, field_style))
        story.append(Spacer(1, 6))

    # Section 10: Trial Attorney Issues
    story.append(PageBreak())
    story.append(Paragraph("SECTION 10: TRIAL ATTORNEY PERFORMANCE", section_style))
    story.append(Paragraph(
        "If claiming ineffective assistance of counsel, check all issues that apply:",
        instruction_style
    ))

    iac_issues = [
        "Failed to investigate the facts of the case",
        "Failed to interview or call witnesses",
        "Failed to obtain or present expert witnesses",
        "Failed to investigate my background for mitigation",
        "Failed to file appropriate pretrial motions",
        "Failed to object to inadmissible evidence",
        "Failed to adequately prepare for trial",
        "Failed to properly cross-examine witnesses",
        "Failed to challenge identification procedures",
        "Failed to investigate alibi witnesses",
        "Gave incorrect advice about plea consequences",
        "Failed to communicate plea offers",
        "Failed to explain immigration consequences",
        "Failed to explain sex offender registration requirements",
        "Failed to challenge legality of search/seizure",
        "Failed to request jury instructions",
        "Failed to preserve issues for appeal",
        "Had a conflict of interest",
        "Was impaired or distracted during representation",
        "Provided ineffective assistance at sentencing",
    ]

    for issue in iac_issues:
        story.append(Paragraph(f"[ ] {issue}", checkbox_style))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Describe any other issues with your trial attorney:", question_style))
    for _ in range(4):
        story.append(Paragraph("_" * 80, field_style))

    # Section 11: Witnesses
    story.append(Paragraph("SECTION 11: WITNESSES", section_style))
    story.append(Paragraph("Witnesses who support your claims:", subsection_style))
    story.append(Paragraph(
        "List anyone who has information supporting your claims (include contact information if known):",
        instruction_style
    ))

    witness_table_data = [
        ["Name", "Relationship", "Contact Information", "What They Know"],
        ["_" * 18, "_" * 12, "_" * 20, "_" * 18],
        ["_" * 18, "_" * 12, "_" * 20, "_" * 18],
        ["_" * 18, "_" * 12, "_" * 20, "_" * 18],
        ["_" * 18, "_" * 12, "_" * 20, "_" * 18],
    ]

    witness_table = Table(witness_table_data, colWidths=[1.6*inch, 1.2*inch, 2*inch, 1.8*inch])
    witness_table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(witness_table)

    story.append(Paragraph("Witnesses NOT called at trial who should have been:", subsection_style))
    for _ in range(3):
        story.append(Paragraph("_" * 80, field_style))

    # Section 12: Evidence
    story.append(Paragraph("SECTION 12: EVIDENCE AND DOCUMENTS", section_style))
    story.append(Paragraph("Check all documents you have access to:", question_style))

    documents = [
        "Indictment or Information",
        "Judgment and Sentence",
        "Reporter's Record (trial transcript)",
        "Clerk's Record",
        "Plea Paperwork",
        "Police Reports",
        "Witness Statements",
        "Expert Reports",
        "Laboratory Reports",
        "Photographs/Videos",
        "Appeals Court Opinion",
        "PDR Decision",
        "Prior Habeas Decisions",
        "Attorney Correspondence",
        "Discovery Materials",
    ]

    for document in documents:
        story.append(Paragraph(f"[ ] {document}", checkbox_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("Describe any NEW evidence not presented at trial:", question_style))
    for _ in range(4):
        story.append(Paragraph("_" * 80, field_style))

    # Section 13: Immigration Status
    story.append(PageBreak())
    story.append(Paragraph("SECTION 13: IMMIGRATION STATUS (if applicable)", section_style))
    story.append(Paragraph("Are you a United States citizen? [ ] Yes    [ ] No", question_style))
    story.append(Paragraph("If no:", question_style))
    story.append(Paragraph(f"    Country of Citizenship: {'_' * 30}", field_style))
    story.append(Paragraph(f"    Immigration Status at time of conviction: {'_' * 25}", field_style))
    story.append(Paragraph("    Are you in removal/deportation proceedings? [ ] Yes    [ ] No", checkbox_style))
    story.append(Paragraph("    Were you advised of immigration consequences before pleading guilty? [ ] Yes    [ ] No", checkbox_style))

    # Section 14: Current Status
    story.append(Paragraph("SECTION 14: CURRENT STATUS", section_style))
    story.append(Paragraph("Current custody status:", question_style))
    story.append(Paragraph("[ ] TDCJ Prison    [ ] County Jail    [ ] State Jail    [ ] Federal Custody", checkbox_style))
    story.append(Paragraph("[ ] Community Supervision (Probation)    [ ] Parole    [ ] Released/Discharged", checkbox_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph(f"Projected Release Date (if incarcerated): {'_' * 25}", field_style))
    story.append(Paragraph(f"Parole Eligibility Date: {'_' * 25}", field_style))
    story.append(Paragraph("Have you completed your sentence? [ ] Yes    [ ] No", question_style))
    story.append(Paragraph(
        "If yes, are you experiencing collateral consequences (employment, housing, etc.)? [ ] Yes    [ ] No",
        question_style
    ))
    story.append(Paragraph("Explain:", question_style))
    for _ in range(2):
        story.append(Paragraph("_" * 80, field_style))

    # Section 15: Time Limits
    story.append(Paragraph("SECTION 15: TIME-SENSITIVE INFORMATION", section_style))
    story.append(Paragraph(
        "<b>WARNING:</b> Strict time limits apply to habeas corpus applications. Answer carefully.",
        instruction_style
    ))

    story.append(Paragraph(f"Date conviction became final (mandate issued): {'_' * 25}", field_style))
    story.append(Paragraph("When did you first discover the grounds for this application?", question_style))
    story.append(Paragraph(f"Date: {'_' * 20}    Circumstances: {'_' * 35}", field_style))
    story.append(Paragraph("Why are you filing now?", question_style))
    for _ in range(2):
        story.append(Paragraph("_" * 80, field_style))

    # Section 16: Additional Information
    story.append(Paragraph("SECTION 16: ADDITIONAL INFORMATION", section_style))
    story.append(Paragraph("Is there anything else we should know about your case?", question_style))
    for _ in range(8):
        story.append(Paragraph("_" * 80, field_style))

    # Certification
    story.append(PageBreak())
    story.append(Paragraph("CERTIFICATION AND SIGNATURE", section_style))
    story.append(Paragraph(
        """I declare under penalty of perjury that the information provided in this
        questionnaire is true and correct to the best of my knowledge. I understand
        that providing false information may adversely affect my case and could result
        in criminal prosecution for perjury. I understand that completing this
        questionnaire does not create an attorney-client relationship and does not
        guarantee that I will receive legal representation.""",
        instruction_style
    ))

    story.append(Spacer(1, 20))
    story.append(Paragraph(f"Signature: {'_' * 50}", field_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"Printed Name: {'_' * 47}", field_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"Date: {'_' * 55}", field_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"TDCJ/Inmate Number: {'_' * 40}", field_style))

    # Office Use Only
    story.append(Spacer(1, 30))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.gray))
    story.append(Paragraph("FOR OFFICE USE ONLY", subsection_style))

    office_fields = [
        ("Date Received:", 2.5),
        ("Received By:", 3),
        ("Conflict Check Completed:", 2),
        ("Statute of Limitations Review:", 3),
        ("Case Assigned To:", 3),
        ("Initial Assessment:", 4),
    ]

    for label, width in office_fields:
        story.append(Paragraph(
            f"{label} {'_' * int(width * 10)}",
            field_style
        ))

    # Build PDF
    doc.build(story)
    print(f"PDF generated: {filename}")
    return filename


if __name__ == "__main__":
    build_questionnaire()
