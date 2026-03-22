"""
Generate a professional HIPAA IT Compliance Checklist PDF for FlossByte.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepTogether, PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfgen import canvas
import os

# Brand colors
NAVY = HexColor('#0f1b2d')
DARK_NAVY = HexColor('#0a1220')
TEAL = HexColor('#00BFA5')
LIGHT_TEAL = HexColor('#e0f7f3')
DARK_GRAY = HexColor('#2d3748')
MED_GRAY = HexColor('#4a5568')
LIGHT_GRAY = HexColor('#f7fafc')
BORDER_GRAY = HexColor('#e2e8f0')
WHITE = white
CHECK_BG = HexColor('#f0fdf9')

OUTPUT = os.path.join(os.path.dirname(__file__), 'hipaa-it-checklist.pdf')


def draw_header_footer(c, doc):
    """Draw branded header and footer on each page."""
    width, height = letter
    page_num = doc.page

    # Header bar
    c.setFillColor(NAVY)
    c.rect(0, height - 50, width, 50, fill=1, stroke=0)

    # Header text
    c.setFillColor(WHITE)
    c.setFont('Helvetica-Bold', 11)
    c.drawString(54, height - 33, 'FlossByte')
    c.setFillColor(TEAL)
    c.setFont('Helvetica', 9)
    c.drawString(120, height - 33, '|  HIPAA IT Compliance Checklist')

    # Header right — contact
    c.setFillColor(HexColor('#94a3b8'))
    c.setFont('Helvetica', 8)
    c.drawRightString(width - 54, height - 30, '(669) 237-2264  |  hello@flossbyte.com')
    c.drawRightString(width - 54, height - 40, 'flossbyte.com')

    # Footer bar
    c.setFillColor(NAVY)
    c.rect(0, 0, width, 36, fill=1, stroke=0)

    c.setFillColor(HexColor('#94a3b8'))
    c.setFont('Helvetica', 7)
    c.drawString(54, 14, '\u00a9 2026 FlossByte  |  Dental IT Support  |  Bay Area, CA')
    c.drawRightString(width - 54, 14, f'Page {page_num}')

    # Teal accent line under header
    c.setStrokeColor(TEAL)
    c.setLineWidth(2)
    c.line(0, height - 50, width, height - 50)


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        topMargin=80,
        bottomMargin=60,
        leftMargin=54,
        rightMargin=54,
    )

    # Styles
    s_title = ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=26,
                             textColor=NAVY, leading=32, spaceAfter=6)
    s_subtitle = ParagraphStyle('Subtitle', fontName='Helvetica', fontSize=11,
                                textColor=MED_GRAY, leading=16, spaceAfter=20)
    s_section = ParagraphStyle('Section', fontName='Helvetica-Bold', fontSize=14,
                               textColor=NAVY, leading=20, spaceBefore=24, spaceAfter=8)
    s_body = ParagraphStyle('Body', fontName='Helvetica', fontSize=9.5,
                            textColor=DARK_GRAY, leading=14, spaceAfter=6)
    s_body_bold = ParagraphStyle('BodyBold', fontName='Helvetica-Bold', fontSize=9.5,
                                 textColor=DARK_GRAY, leading=14, spaceAfter=6)
    s_small = ParagraphStyle('Small', fontName='Helvetica', fontSize=8,
                             textColor=MED_GRAY, leading=11)
    s_check_title = ParagraphStyle('CheckTitle', fontName='Helvetica-Bold', fontSize=10,
                                   textColor=NAVY, leading=14)
    s_check_body = ParagraphStyle('CheckBody', fontName='Helvetica', fontSize=8.5,
                                  textColor=MED_GRAY, leading=12)
    s_cta_head = ParagraphStyle('CTAHead', fontName='Helvetica-Bold', fontSize=16,
                                textColor=NAVY, leading=22, alignment=TA_CENTER, spaceAfter=8)
    s_cta_body = ParagraphStyle('CTABody', fontName='Helvetica', fontSize=10,
                                textColor=MED_GRAY, leading=15, alignment=TA_CENTER, spaceAfter=16)
    s_cta_btn = ParagraphStyle('CTABtn', fontName='Helvetica-Bold', fontSize=12,
                               textColor=WHITE, leading=16, alignment=TA_CENTER)
    s_footer_note = ParagraphStyle('FooterNote', fontName='Helvetica-Oblique', fontSize=8,
                                   textColor=MED_GRAY, leading=11, alignment=TA_CENTER)
    s_num = ParagraphStyle('Num', fontName='Helvetica-Bold', fontSize=11,
                           textColor=TEAL, leading=14, alignment=TA_CENTER)

    story = []

    # ── COVER / INTRO ──────────────────────────────────────────
    story.append(Spacer(1, 20))

    # Teal accent badge
    badge_data = [[Paragraph('FREE RESOURCE', ParagraphStyle('Badge', fontName='Helvetica-Bold',
                    fontSize=8, textColor=TEAL, alignment=TA_CENTER, leading=10))]]
    badge_table = Table(badge_data, colWidths=[120], rowHeights=[22])
    badge_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_TEAL),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROUNDEDCORNERS', [6, 6, 6, 6]),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(badge_table)
    story.append(Spacer(1, 14))

    story.append(Paragraph('HIPAA IT Compliance<br/>Checklist for Dental Practices', s_title))
    story.append(Paragraph(
        '15 critical technical safeguards every dental office must have in place to protect '
        'patient data, avoid costly fines, and pass an OCR audit with confidence.',
        s_subtitle
    ))

    # Intro box
    intro_text = Paragraph(
        '<b>Why this checklist matters:</b> HIPAA violations can cost dental practices '
        '$50,000 to $1.5 million per incident. The Office for Civil Rights (OCR) has '
        'increased enforcement actions against healthcare providers, including dental '
        'practices, for failing to implement required technical safeguards. This checklist '
        'covers the IT controls that OCR auditors specifically look for.',
        ParagraphStyle('IntroBody', fontName='Helvetica', fontSize=9.5,
                       textColor=DARK_GRAY, leading=14)
    )
    intro_table = Table([[intro_text]], colWidths=[doc.width - 24])
    intro_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_GRAY),
        ('BOX', (0, 0), (-1, -1), 1, BORDER_GRAY),
        ('LEFTPADDING', (0, 0), (-1, -1), 16),
        ('RIGHTPADDING', (0, 0), (-1, -1), 16),
        ('TOPPADDING', (0, 0), (-1, -1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 14),
    ]))
    story.append(intro_table)
    story.append(Spacer(1, 8))

    # How to use
    story.append(Paragraph(
        '<b>How to use:</b> Work through each item with your IT provider. Check off items '
        'you have in place. Any unchecked item is a compliance gap that needs to be addressed. '
        'Items marked with <font color="#dc2626"><b>CRITICAL</b></font> are the most common '
        'audit findings.',
        s_body
    ))
    story.append(Spacer(1, 4))

    # ── CHECKLIST SECTIONS ─────────────────────────────────────

    sections = [
        {
            'title': 'Section 1: Access Controls & Authentication',
            'icon': 'LOCK',
            'items': [
                {
                    'num': '1',
                    'title': 'Unique User IDs for Every Staff Member',
                    'desc': 'Each employee must log in with their own unique username and password. No shared logins or generic accounts (e.g., "FrontDesk1"). HIPAA requires individual accountability for all system access.',
                    'critical': True,
                },
                {
                    'num': '2',
                    'title': 'Multi-Factor Authentication (MFA) Enabled',
                    'desc': 'MFA must be enabled on all systems that access patient data — including email, practice management software (Dentrix, Eaglesoft, Open Dental), remote access, and cloud services.',
                    'critical': True,
                },
                {
                    'num': '3',
                    'title': 'Role-Based Access Controls (RBAC)',
                    'desc': 'Staff should only access the data they need for their role. Front desk staff don\'t need access to clinical notes. Hygienists don\'t need billing data. Configure permissions in your PMS accordingly.',
                    'critical': False,
                },
                {
                    'num': '4',
                    'title': 'Automatic Session Timeouts',
                    'desc': 'Workstations must lock automatically after a period of inactivity (recommended: 5-10 minutes). This prevents unauthorized access when staff walk away from a computer during patient care.',
                    'critical': False,
                },
            ]
        },
        {
            'title': 'Section 2: Data Encryption',
            'icon': 'SHIELD',
            'items': [
                {
                    'num': '5',
                    'title': 'Encryption at Rest — Full Disk Encryption',
                    'desc': 'All workstations, servers, and portable devices must use full disk encryption (BitLocker for Windows, FileVault for Mac). If a laptop is stolen, encrypted data is unreadable without the key.',
                    'critical': True,
                },
                {
                    'num': '6',
                    'title': 'Encryption in Transit — TLS/SSL for All Communications',
                    'desc': 'All data transmitted over networks must be encrypted. This includes email (TLS), web traffic (HTTPS), VPN connections, and cloud sync. Unencrypted email containing PHI is a direct HIPAA violation.',
                    'critical': True,
                },
                {
                    'num': '7',
                    'title': 'Encrypted Backup Storage',
                    'desc': 'Backup files — whether stored locally, on external drives, or in the cloud — must be encrypted using AES-256 or equivalent. Unencrypted backups are one of the most common audit findings.',
                    'critical': False,
                },
            ]
        },
        {
            'title': 'Section 3: Backup & Disaster Recovery',
            'icon': 'CLOUD',
            'items': [
                {
                    'num': '8',
                    'title': 'Daily Automated Backups',
                    'desc': 'Patient data, practice management databases, imaging files, and system configurations must be backed up daily. Manual backups are unreliable — use automated, scheduled backup systems.',
                    'critical': True,
                },
                {
                    'num': '9',
                    'title': 'Backup Recovery Testing (Quarterly)',
                    'desc': 'Backups are useless if they can\'t be restored. Test your backup recovery process at least quarterly. Document the test date, recovery time, and results. OCR auditors ask for this documentation.',
                    'critical': False,
                },
                {
                    'num': '10',
                    'title': 'Off-Site or Cloud Backup Storage',
                    'desc': 'At least one copy of your backups must be stored off-site (cloud or separate physical location). This protects against fire, flood, theft, and ransomware that encrypts local files.',
                    'critical': False,
                },
            ]
        },
        {
            'title': 'Section 4: Network Security & Monitoring',
            'icon': 'NETWORK',
            'items': [
                {
                    'num': '11',
                    'title': 'Enterprise-Grade Firewall with Active Monitoring',
                    'desc': 'A properly configured firewall is required — not a consumer-grade router. The firewall should have intrusion detection/prevention (IDS/IPS), content filtering, and active threat monitoring.',
                    'critical': True,
                },
                {
                    'num': '12',
                    'title': 'Endpoint Detection & Response (EDR)',
                    'desc': 'Traditional antivirus is no longer sufficient. EDR solutions monitor endpoint behavior in real time, detecting ransomware, zero-day threats, and fileless attacks that signature-based antivirus misses.',
                    'critical': False,
                },
                {
                    'num': '13',
                    'title': 'Segregated Guest Wi-Fi Network',
                    'desc': 'Patient Wi-Fi must be on a completely separate network from practice systems. A flat network allows anyone on guest Wi-Fi to potentially access practice management software and patient records.',
                    'critical': False,
                },
            ]
        },
        {
            'title': 'Section 5: Policies, Training & Documentation',
            'icon': 'DOC',
            'items': [
                {
                    'num': '14',
                    'title': 'Annual HIPAA Security Risk Assessment',
                    'desc': 'HIPAA requires a documented risk assessment at least annually. This must identify threats, vulnerabilities, and the likelihood/impact of a breach. It is the single most requested document in an OCR audit.',
                    'critical': True,
                },
                {
                    'num': '15',
                    'title': 'Staff Security Awareness Training',
                    'desc': 'All staff with access to PHI must receive HIPAA security training at hire and annually thereafter. Training should cover phishing recognition, password hygiene, device security, and incident reporting procedures.',
                    'critical': True,
                },
            ]
        },
    ]

    for sec in sections:
        story.append(Spacer(1, 6))

        # Section header with teal left border
        sec_head = Paragraph(sec['title'], s_section)
        sec_table = Table([[sec_head]], colWidths=[doc.width - 8])
        sec_table.setStyle(TableStyle([
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LINEBEFOREDECOR', (0, 0), (0, -1), 3, TEAL),
        ]))
        story.append(sec_table)

        for item in sec['items']:
            # Build checklist row
            checkbox = Paragraph('\u2610', ParagraphStyle('CB', fontName='Helvetica',
                                 fontSize=16, textColor=TEAL, alignment=TA_CENTER, leading=18))
            num = Paragraph(item['num'], s_num)

            critical_tag = ''
            if item['critical']:
                critical_tag = '  <font color="#dc2626" size="7"><b>CRITICAL</b></font>'

            title_p = Paragraph(f"{item['title']}{critical_tag}", s_check_title)
            desc_p = Paragraph(item['desc'], s_check_body)

            inner = Table(
                [[title_p], [desc_p]],
                colWidths=[doc.width - 80]
            )
            inner.setStyle(TableStyle([
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))

            row_table = Table(
                [[checkbox, inner]],
                colWidths=[36, doc.width - 44],
                rowHeights=[None],
            )

            bg = CHECK_BG if item['critical'] else WHITE
            row_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), bg),
                ('BOX', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
                ('VALIGN', (0, 0), (0, 0), 'TOP'),
                ('VALIGN', (1, 0), (1, 0), 'TOP'),
                ('LEFTPADDING', (0, 0), (0, 0), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                ('RIGHTPADDING', (1, 0), (1, 0), 12),
                ('LEFTPADDING', (1, 0), (1, 0), 4),
            ]))

            story.append(KeepTogether([row_table, Spacer(1, 6)]))

    # ── SCORING SECTION ────────────────────────────────────────
    story.append(PageBreak())
    story.append(Spacer(1, 10))
    story.append(Paragraph('Your HIPAA IT Compliance Score', s_section))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        'Count the number of items you checked off above. Use the scoring guide below '
        'to assess your practice\'s current compliance posture:',
        s_body
    ))
    story.append(Spacer(1, 10))

    score_data = [
        [
            Paragraph('<b>Score</b>', ParagraphStyle('TH', fontName='Helvetica-Bold',
                       fontSize=9, textColor=WHITE, leading=12)),
            Paragraph('<b>Rating</b>', ParagraphStyle('TH', fontName='Helvetica-Bold',
                       fontSize=9, textColor=WHITE, leading=12)),
            Paragraph('<b>What It Means</b>', ParagraphStyle('TH', fontName='Helvetica-Bold',
                       fontSize=9, textColor=WHITE, leading=12)),
        ],
        [
            Paragraph('13\u201315', s_body),
            Paragraph('<font color="#16a34a"><b>Strong</b></font>', s_body),
            Paragraph('Your practice has a solid HIPAA IT foundation. Continue monitoring and update your risk assessment annually.', s_small),
        ],
        [
            Paragraph('9\u201312', s_body),
            Paragraph('<font color="#ca8a04"><b>Moderate</b></font>', s_body),
            Paragraph('You have basic protections but notable gaps. Address unchecked items — especially any marked CRITICAL — within 30 days.', s_small),
        ],
        [
            Paragraph('5\u20138', s_body),
            Paragraph('<font color="#ea580c"><b>At Risk</b></font>', s_body),
            Paragraph('Significant compliance gaps exist. Your practice is vulnerable to breaches and audit penalties. Prioritize remediation immediately.', s_small),
        ],
        [
            Paragraph('0\u20134', s_body),
            Paragraph('<font color="#dc2626"><b>Critical</b></font>', s_body),
            Paragraph('Your practice faces serious HIPAA exposure. A data breach at this level could result in substantial fines and reputational damage. Seek professional IT assessment now.', s_small),
        ],
    ]

    score_table = Table(score_data, colWidths=[60, 70, doc.width - 150])
    score_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('BACKGROUND', (0, 1), (-1, -1), WHITE),
        ('BOX', (0, 0), (-1, -1), 1, BORDER_GRAY),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER_GRAY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(score_table)

    # ── COMMON MISTAKES ────────────────────────────────────────
    story.append(Spacer(1, 20))
    story.append(Paragraph('5 Most Common HIPAA IT Mistakes in Dental Practices', s_section))
    story.append(Spacer(1, 4))

    mistakes = [
        ('Using shared logins', 'Multiple staff using the same username/password makes it impossible to track who accessed patient records — a direct HIPAA violation.'),
        ('No Business Associate Agreement (BAA)', 'Every vendor that touches patient data (IT provider, cloud backup, email host) must sign a BAA. Without one, your practice is liable for their breaches.'),
        ('Relying on antivirus alone', 'Antivirus catches known threats. Modern ransomware, phishing, and zero-day attacks require EDR, email filtering, and network monitoring.'),
        ('Never testing backups', 'Having backups isn\'t enough. If you\'ve never tested a restore, you have no idea if your data is actually recoverable after a disaster.'),
        ('Skipping the annual risk assessment', 'This is the #1 audit finding. OCR will ask for your most recent risk assessment. If you don\'t have one, you fail the audit.'),
    ]

    for i, (title, desc) in enumerate(mistakes, 1):
        num_p = Paragraph(f'<b>{i}</b>', ParagraphStyle('MistakeNum', fontName='Helvetica-Bold',
                          fontSize=11, textColor=WHITE, alignment=TA_CENTER, leading=14))
        num_cell = Table([[num_p]], colWidths=[28], rowHeights=[28])
        num_cell.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), TEAL),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROUNDEDCORNERS', [4, 4, 4, 4]),
        ]))

        text_p = Paragraph(f'<b>{title}:</b> {desc}', s_body)

        mistake_row = Table([[num_cell, text_p]], colWidths=[36, doc.width - 48])
        mistake_row.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (1, 0), (1, 0), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(KeepTogether([mistake_row, Spacer(1, 6)]))

    # ── CTA SECTION ────────────────────────────────────────────
    story.append(Spacer(1, 24))

    cta_content = [
        [Paragraph('Need Help Closing the Gaps?', s_cta_head)],
        [Paragraph(
            'FlossByte provides HIPAA-compliant managed IT services built exclusively for dental '
            'practices in the Bay Area. We\'ll assess your current setup, identify compliance gaps, '
            'and implement the safeguards your practice needs — so you can focus on patient care.',
            s_cta_body
        )],
    ]

    # CTA button
    btn_text = Paragraph('Book Your Free IT Assessment', s_cta_btn)
    btn_table = Table([[btn_text]], colWidths=[240], rowHeights=[40])
    btn_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), TEAL),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ]))

    cta_content.append([btn_table])
    cta_content.append([Spacer(1, 10)])

    contact_style = ParagraphStyle('Contact', fontName='Helvetica', fontSize=9,
                                   textColor=MED_GRAY, leading=14, alignment=TA_CENTER)
    cta_content.append([Paragraph(
        '<b>Call:</b> (669) 237-2264  |  <b>Email:</b> hello@flossbyte.com  |  '
        '<b>Web:</b> flossbyte.com', contact_style
    )])
    cta_content.append([Spacer(1, 8)])
    cta_content.append([Paragraph(
        'Serving dental practices across the Peninsula, East Bay &amp; South Bay',
        s_footer_note
    )])

    cta_table = Table(cta_content, colWidths=[doc.width - 40])
    cta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_GRAY),
        ('BOX', (0, 0), (-1, -1), 1, BORDER_GRAY),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LEFTPADDING', (0, 0), (-1, -1), 24),
        ('RIGHTPADDING', (0, 0), (-1, -1), 24),
        ('TOPPADDING', (0, 0), (0, 0), 24),
        ('BOTTOMPADDING', (-1, -1), (-1, -1), 20),
    ]))
    story.append(cta_table)

    # ── DISCLAIMER ─────────────────────────────────────────────
    story.append(Spacer(1, 16))
    story.append(Paragraph(
        '<i>Disclaimer: This checklist is provided for informational purposes only and does not '
        'constitute legal advice. HIPAA compliance requirements may vary based on your practice\'s '
        'specific circumstances. Consult with a qualified HIPAA compliance professional for a '
        'comprehensive assessment.</i>',
        ParagraphStyle('Disclaimer', fontName='Helvetica-Oblique', fontSize=7,
                       textColor=HexColor('#94a3b8'), leading=10, alignment=TA_CENTER)
    ))

    # Build
    doc.build(story, onFirstPage=draw_header_footer, onLaterPages=draw_header_footer)
    print(f'PDF created: {OUTPUT}')


if __name__ == '__main__':
    build_pdf()
