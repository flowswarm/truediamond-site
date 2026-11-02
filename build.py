#!/usr/bin/env python3
"""
Static site generator for True Diamond Life Care Group.

Run:  python3 build.py
Then: cd site && python3 -m http.server 8080  ->  http://localhost:8080

Every page shares the header / footer defined below, so edit them once here
and re-run build.py. Content comes from the "Website Breakdown" PDF.
"""
from pathlib import Path
import html

OUT = Path(__file__).parent / "site"

# ---------------------------------------------------------------------------
# Business basics
# ---------------------------------------------------------------------------
BIZ = {
    "name": "True Diamond Life Care Group",
    "legal": "True Diamond Care Group LLC",
    "tagline": "Elevated Care. Trusted Protection.",
    "address": "600 N Jackson Street, Media, PA 19063",
    "phone": "610-717-8530",
    "phone_tel": "+16107178530",
    "email": "owner@truediamondlcg.com",
    "owner": "Diamond P. Foster, NCG",
    "serving": "Now Serving Pennsylvania and Delaware",
}

FORM_NOTE = ("Whether you're seeking professional guardianship services for a loved one, exploring available options, "
             "or interested in professional collaboration, we're here to help. Share a few details about your needs, "
             "and a member of our team will contact you to discuss the next steps.")
FORM_DISCLAIMER = ("To protect your privacy, please refrain from submitting sensitive medical, financial, or personally "
                   "identifying information through this form. Submitting an inquiry does not establish a professional "
                   "guardianship relationship. Information provided during a consultation is for general informational "
                   "purposes and does not constitute legal advice.")

SERVICES = [
    {
        "slug": "court-appointed-guardianship",
        "title": "Court-Appointed Guardianship",
        "short": "Professional guardianship services for individuals appointed by the court, with responsibilities guided by the applicable court order and governing law.",
        "body": [
            "Professional guardianship services for individuals appointed by the court, with responsibilities guided by the applicable court order and governing law. We prioritize individual rights, personal dignity, safety, and well-being while fulfilling our fiduciary and legal responsibilities.",
        ],
        "includes": [
            "Serving as a court-appointed guardian under the authority granted by the court order",
            "Fulfilling fiduciary and legal responsibilities in accordance with governing law",
            "Prioritizing individual rights, personal dignity, safety, and well-being",
            "Respecting the individual's expressed wishes and preferences to the greatest extent possible",
        ],
    },
    {
        "slug": "person-centered-advocacy",
        "title": "Person-Centered Advocacy",
        "short": "Individualized advocacy that recognizes each person's preferences, values, needs, and personal history.",
        "body": [
            "Individualized advocacy that recognizes each person's preferences, values, needs, and personal history. We strive to ensure individuals are heard, respected, and involved in decisions to the greatest extent possible.",
        ],
        "includes": [
            "Recognizing each person's preferences, values, needs, and personal history",
            "Ensuring individuals are heard and respected",
            "Involving the individual in decisions to the greatest extent possible",
            "Promoting individual rights, dignity, and participation",
        ],
    },
    {
        "slug": "healthcare-decision-support",
        "title": "Healthcare and Medical Decision Support",
        "short": "When authorized by the applicable guardianship order, assisting with healthcare decisions and advocating for appropriate treatment and continuity of care.",
        "body": [
            "When authorized by the applicable guardianship order, assisting with healthcare decisions, communicating with medical providers, reviewing care recommendations, and advocating for appropriate treatment and continuity of care.",
        ],
        "includes": [
            "Assisting with healthcare decisions as authorized by the guardianship order",
            "Communicating with medical providers",
            "Reviewing care recommendations",
            "Advocating for appropriate treatment and continuity of care",
        ],
    },
    {
        "slug": "estate-financial-guardianship",
        "title": "Estate and Financial Guardianship",
        "short": "When specifically appointed and authorized, overseeing financial matters, safeguarding assets, and fulfilling required financial reporting obligations.",
        "body": [
            "When specifically appointed and authorized, overseeing financial matters, monitoring income and expenses, safeguarding assets, maintaining accurate records, and fulfilling required financial reporting and accounting obligations.",
        ],
        "includes": [
            "Overseeing financial matters when specifically appointed and authorized",
            "Monitoring income and expenses",
            "Safeguarding assets",
            "Maintaining accurate records",
            "Fulfilling required financial reporting and accounting obligations",
        ],
    },
    {
        "slug": "care-coordination",
        "title": "Care Coordination and Service Advocacy",
        "short": "Collaborating with healthcare providers, social workers, residential facilities, and community resources to support appropriate services.",
        "body": [
            "Collaborating with healthcare providers, social workers, residential facilities, and community resources to support appropriate services, monitor changing needs, and promote the individual's quality of life.",
        ],
        "includes": [
            "Collaborating with healthcare providers, social workers, and residential facilities",
            "Connecting with community resources to support appropriate services",
            "Monitoring changing needs over time",
            "Promoting the individual's quality of life",
        ],
    },
    {
        "slug": "court-reporting-compliance",
        "title": "Court Reporting and Guardianship Compliance",
        "short": "Maintaining appropriate case documentation, preparing required reports, and meeting applicable court deadlines and reporting obligations.",
        "body": [
            "Maintaining appropriate case documentation, monitoring responsibilities established by court orders, preparing required reports, and meeting applicable court deadlines and reporting obligations.",
        ],
        "includes": [
            "Maintaining appropriate case documentation",
            "Monitoring responsibilities established by court orders",
            "Preparing required reports",
            "Meeting applicable court deadlines and reporting obligations",
        ],
    },
    {
        "slug": "professional-collaboration",
        "title": "Professional Collaboration and Case Communication",
        "short": "Working collaboratively with attorneys, court personnel, families, care teams, and other authorized stakeholders.",
        "body": [
            "Working collaboratively with attorneys, court personnel, families, care teams, and other authorized stakeholders to support informed decision-making, clear communication, and responsible guardianship administration.",
        ],
        "includes": [
            "Working with attorneys, court personnel, families, and care teams",
            "Coordinating with other authorized stakeholders",
            "Supporting informed decision-making and clear communication",
            "Supporting responsible guardianship administration",
        ],
    },
]

WHO_WE_SERVE = [
    "Adults who have been determined by a court to need a guardian.",
    "Older adults who require assistance and protection through a court-appointed guardianship.",
    "Individuals with disabilities or other circumstances affecting their ability to make certain decisions, as determined through the applicable legal process.",
    "Courts, attorneys, families, and professionals seeking a qualified, compassionate guardian.",
]

EXPECT = [
    ("Dignity, Respect &amp; Individualized Care",
     "Every individual deserves to be treated as a person of inherent worth. We strive to honor personal preferences, respect individual values, and support participation in decisions to the greatest extent possible."),
    ("Protection of Rights &amp; Best Interests",
     "We are committed to advocating for the rights, safety, and well-being of those we serve, making decisions within our authorized responsibilities and in accordance with applicable law and court orders."),
    ("Responsible &amp; Ethical Decision-Making",
     "Integrity guides our approach to every responsibility. We strive to exercise sound judgment, maintain appropriate documentation, uphold confidentiality, and fulfill our obligations with transparency and accountability."),
    ("Continuity of Care &amp; Coordination",
     "We work toward effective communication and collaboration with healthcare providers, social service professionals, residential facilities, attorneys, and other authorized parties to help address changing needs and support appropriate services."),
    ("Preservation of Independence",
     "We recognize that protection and independence should work together. Whenever possible and consistent with the individual's needs and legal circumstances, we strive to preserve personal autonomy, encourage participation, and support the individual's ability to make choices."),
    ("Confidence Through Professional Accountability",
     "We aim to build lasting trust with families, courts, attorneys, and other professionals through consistent communication, diligent case management, responsible oversight, and adherence to applicable guardianship requirements."),
]

FAQ = [
    ("What is a court-appointed guardian?", """
<p>A court-appointed guardian is a person or qualified entity authorized by the Pennsylvania Court of Common Pleas, typically through its Orphans' Court Division, to make certain decisions on behalf of an individual whom the court has determined to be incapacitated and in need of guardianship services.</p>
<p>Under Pennsylvania law, guardians may be appointed to oversee personal matters, financial matters, or both, depending on the court's findings and order. A guardian has a legal and fiduciary responsibility to protect the individual's rights and best interests while respecting their expressed wishes and preferences to the greatest extent possible.</p>
<p>At True Diamond Life Care Group, we recognize that guardianship is a position of profound trust, requiring sound judgment, ethical decision-making, compassion, and accountability.</p>"""),
    ("Who may need a guardian?", """
<p>Under Pennsylvania law, an adult may need a guardian when a court determines, based on clear and convincing evidence, that a condition or disability impairs their ability to make or communicate decisions and that guardianship services are necessary to meet their essential needs or protect their financial resources.</p>
<p>The court must consider the individual's functional abilities, available support systems, and less restrictive alternatives before appointing a guardian. A diagnosis, disability, or residence in a care facility does not automatically establish the need for guardianship.</p>
<p>True Diamond Life Care Group is committed to recognizing everyone's unique circumstances and fully respecting their right to independence and self-determination permitted by law.</p>"""),
    ("What types of guardianship services does True Diamond Life Care Group provide?", """
<p>True Diamond Life Care Group focuses on professional, person-centered guardianship and advocacy. Depending on the appointment, authorization, and availability of services, our intended service areas include:</p>
<ul>
<li><strong>Guardianship of the Person:</strong> Supporting personal care, living arrangements, healthcare coordination, and other matters authorized by the court.</li>
<li><strong>Guardianship of the Estate:</strong> Managing financial affairs, safeguarding assets, monitoring income and expenditures, and maintaining appropriate records when appointed and authorized.</li>
<li><strong>Person-Centered Advocacy:</strong> Promoting individual rights, preferences, dignity, and participation in decisions.</li>
<li><strong>Care Coordination:</strong> Communicating with healthcare providers, residential facilities, social workers, and other authorized professionals to help address an individual's needs.</li>
<li><strong>Court Reporting and Compliance:</strong> Maintaining appropriate records and completing required guardianship reports and filings.</li>
<li><strong>Professional Collaboration:</strong> Coordinating with attorneys, court personnel, families, and other relevant parties when appropriate and legally authorized.</li>
</ul>
<p>Specific services depend on the authority granted by the court, the needs of the individual, and our capacity to accept the appointment. Please <a href="contact.html">contact us</a> to discuss a potential referral.</p>"""),
    ("What does a guardianship consultation include?", """
<p>A guardianship consultation with True Diamond Life Care Group provides an opportunity to discuss an individual's circumstances, identify potential guardianship needs, and explore how professional guardianship services may be appropriate.</p>
<p>During the consultation, we discuss the individual's current situation, support needs, existing legal arrangements, and any concerns regarding personal well-being, healthcare coordination, or financial oversight. We also review the general guardianship process in Pennsylvania, explain the differences between guardianship of the person and guardianship of the estate, and discuss the responsibilities associated with a potential court appointment.</p>
<p>Our consultation may include:</p>
<ul>
<li><strong>Individual Needs Assessment:</strong> Discussing the individual's circumstances, functional needs, available support systems, and areas where assistance may be needed.</li>
<li><strong>Guardianship Options:</strong> Exploring whether guardianship may be appropriate and discussing less restrictive alternatives that may be worth considering.</li>
<li><strong>Legal Process Overview:</strong> Explaining the general Pennsylvania guardianship appointment process and identifying questions that may require guidance from a qualified attorney.</li>
<li><strong>Scope of Services:</strong> Reviewing the types of guardianship services we offer and whether the potential appointment aligns with our capabilities.</li>
<li><strong>Documentation and Next Steps:</strong> Identifying potentially relevant records and outlining possible next steps, referrals, or information needed to move forward.</li>
<li><strong>Fees and Appointment Expectations:</strong> Discussing consultation fees, service availability, potential responsibilities, and the court appointment process.</li>
</ul>
<p>At True Diamond Life Care Group, we approach every consultation with empathy, professionalism, confidentiality, and respect for the individual's dignity. Our goal is to provide clarity, help families and professionals better understand their options, and determine whether our guardianship services may be an appropriate fit.</p>
<p><em>Please note: A consultation does not establish a guardianship relationship, guarantee acceptance of an appointment, or replace legal advice from an attorney. In Pennsylvania, guardianship authority must be granted by the court.</em></p>"""),
    ("Can family members refer someone to True Diamond Life Care Group?", """
<p>Yes. Family members, attorneys, healthcare professionals, social workers, and other interested parties may contact us to inquire about a potential guardianship referral. We welcome preliminary inquiries from families and professionals seeking information about our services and potential availability.</p>"""),
    ("Do you work with attorneys, courts, and healthcare professionals?", """
<p>Professional collaboration is an important part of responsible guardianship. Where appropriate and legally authorized, True Diamond Life Care Group works to maintain effective communication with attorneys, court personnel, healthcare providers, social workers, residential facilities, and other professionals involved in an individual's care.</p>
<p>A guardian's responsibilities may include coordinating supportive services, advocating for the individual's best interests, monitoring care arrangements, maintaining appropriate documentation, and submitting required reports to the appointing court.</p>
<p>We recognize the importance of professional accountability, timely communication, confidentiality, and respect for the roles of other professionals involved in supporting the individual.</p>"""),
    ("What does guardianship cost?", """
<p>The cost of guardianship depends on the nature of the appointment, the scope of responsibilities, the individual's circumstances, and applicable legal and court requirements.</p>
<p>Court-appointed guardianship may involve attorney fees, court costs, evaluation expenses, guardian compensation, and other authorized administrative expenses. Responsibility for these expenses varies according to the circumstances and applicable law.</p>
<p>Please <a href="contact.html">contact us</a> for information about fees for a potential appointment.</p>"""),
    ("How can I contact True Diamond Life Care Group?", """
<p>We welcome inquiries from families, attorneys, healthcare professionals, social workers, and other individuals seeking information about our guardianship services or a potential referral.</p>
<p>Please use the contact information provided on our <a href="contact.html">contact page</a> to inquire about service availability or request additional information.</p>
<p>To protect privacy, please do not submit sensitive medical, financial, or identifying information through an unsecured contact form. Information about a potential appointment should be shared through an appropriate, secure channel.</p>"""),
]

RESOURCES = [
    ("Standards of Practice for Guardians", "https://www.guardianship.org/standards/",
     "National Guardianship Association",
     "Discover the nationally recognized principles that guide professional guardianship. These standards emphasize ethical decision-making, accountability, individual rights, and the importance of preserving dignity and independence."),
    ("How to Recognize a Good Guardian", "https://www.guardianship.org/guardianship-resources/",
     "National Guardianship Association",
     "Choosing the right guardian is an important decision. Learn about the qualities, responsibilities, and ethical practices that distinguish effective guardianship, including compassionate advocacy, accountability, and respect for individual preferences."),
    ("Understanding Guardianship: Key Concepts &amp; Resources", "https://www.justice.gov/elderjustice/guardianship-key-concepts-and-resources",
     "U.S. Department of Justice — Elder Justice Initiative",
     "Explore essential information about guardianship, including its purpose, legal considerations, and the responsibilities involved in protecting individuals who may require decision-making assistance."),
]
ARTICLE_ILLUS = ["article-standards", "article-recognize", "article-understanding"]
RESOURCES_INTRO = ("Explore trusted educational resources designed to provide insight into guardianship responsibilities, "
                   "professional standards, and the principles of ethical, person-centered care. Understanding guardianship "
                   "is an important step toward making informed decisions for yourself or someone you care about.")

AFFILIATIONS = [
    ("affil-cgc.png", "Center for Guardianship Certification"),
    ("affil-nga.png", "National Guardianship Association"),
    ("affil-cge.png", "The Center for Guardianship Excellence"),
]

# ---------------------------------------------------------------------------
# Shared fragments
# ---------------------------------------------------------------------------
ICON_PHONE = '<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .57 3.6 1 1 0 0 1-.25 1z"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>'


def placeholder(label, extra=""):
    return f'<div class="img-placeholder {extra}" role="img" aria-label="{html.escape(label)} (image placeholder)"><span>{html.escape(label)}</span></div>'


def illus(name, alt, extra=""):
    return f'<img class="illus {extra}" src="assets/images/illus/{name}.svg" alt="{html.escape(alt)}" loading="lazy" decoding="async">'


SERVICE_ALT = {
    "court-appointed-guardianship": "Courthouse, gavel and sealed court order protecting an individual",
    "person-centered-advocacy": "An individual at the centre, their voice heard and supported with compassion",
    "healthcare-decision-support": "Medical cross, stethoscope, heartbeat and a care plan checklist",
    "estate-financial-guardianship": "Vault, ledger and financial chart safeguarded by a shield",
    "care-coordination": "An individual connected to hospital, residence, care team and community resources",
    "court-reporting-compliance": "Calendar deadline, report stack, clock and completed checklist",
    "professional-collaboration": "Handshake between professionals with dialogue bubbles",
}
VALUE_ICONS = ["value-dignity", "value-rights", "value-ethics", "value-continuity", "value-independence", "value-accountability"]


def founder_img(extra=""):
    return (f'<img class="founder-img {extra}" src="assets/images/founder.jpg" '
            f'srcset="assets/images/founder-800.jpg 800w, assets/images/founder.jpg 1374w" '
            f'sizes="(max-width: 980px) 100vw, 40vw" '
            f'alt="Diamond Foster, Founder of True Diamond Life Care Group" width="1374" height="1145" loading="lazy" decoding="async">')


# Web3Forms delivers submissions to the email the access key was created for
# (owner@truediamondlcg.com). Get a key at https://web3forms.com — no account needed.
WEB3FORMS_ACCESS_KEY = "e3c2bf45-0c92-43a9-92f1-59910344c0c0"
FORM_ENDPOINT = "https://api.web3forms.com/submit"


def form_hidden(subject):
    """Hidden fields Web3Forms reads: access key, subject line, sender name, spam honeypot."""
    return f"""
    <input type="hidden" name="access_key" value="{WEB3FORMS_ACCESS_KEY}">
    <input type="hidden" name="subject" value="{subject}">
    <input type="hidden" name="from_name" value="True Diamond Website">
    <input type="checkbox" name="botcheck" class="hidden" style="display:none" tabindex="-1" autocomplete="off">"""


def form(heading="Request a Consultation", note=FORM_NOTE, compact=False, uid="f", subject="New Consultation Request — True Diamond website"):
    msg = "" if compact else f"""
      <div class="field full"><label for="{uid}-msg">How can we help you?</label><textarea id="{uid}-msg" name="message" placeholder="Briefly describe the inquiry or referral"></textarea></div>"""
    return f"""
<div class="form-card">
  <h3>{heading}</h3>
  <p class="form-note">{note}</p>
  <form class="js-form" action="{FORM_ENDPOINT}" method="POST">{form_hidden(subject)}
    <div class="form-grid">
      <div class="field"><label for="{uid}-fn">First Name</label><input id="{uid}-fn" name="first_name" type="text" required></div>
      <div class="field"><label for="{uid}-ln">Last Name</label><input id="{uid}-ln" name="last_name" type="text" required></div>
      <div class="field"><label for="{uid}-em">Email</label><input id="{uid}-em" name="email" type="email" required></div>
      <div class="field"><label for="{uid}-ph">Phone / Mobile</label><input id="{uid}-ph" name="phone" type="tel"></div>{msg}
    </div>
    <button class="btn btn--gold btn--block" type="submit">Submit</button>
    <div class="form-success">Thank you. Your inquiry has been received and we will be in touch.</div>
    <div class="form-error">Sorry — your message could not be sent. Please email <a href="mailto:{BIZ['email']}">{BIZ['email']}</a> or call <a href="tel:{BIZ['phone_tel']}">{BIZ['phone']}</a>.</div>
  </form>
  <p class="form-disclaimer">{FORM_DISCLAIMER}</p>
</div>"""


def nav_services_items():
    items = '<li><a href="services.html">All Guardianship Services</a></li>'
    for s in SERVICES:
        items += f'<li><a href="service-{s["slug"]}.html">{s["title"]}</a></li>'
    items += '<li><a href="services.html#who-we-serve">Who We Serve</a></li>'
    items += '<li><a href="commitment.html">Our Commitment &amp; Outcomes</a></li>'
    return items


def header():
    return f"""
<div class="topbar">
  <div class="container">
    <span class="tagline">Professional Guardianship &amp; Advocacy Services</span>
    <ul>
      <li>{ICON_PHONE}<a href="tel:{BIZ['phone_tel']}">{BIZ['phone']}</a></li>
      <li>{ICON_MAIL}<a href="mailto:{BIZ['email']}">{BIZ['email']}</a></li>
      <li>{ICON_PIN}<span>{BIZ['address']}</span></li>
    </ul>
  </div>
</div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="{BIZ['name']} home">
      <img class="brand-logo" src="assets/images/logo-160.png" srcset="assets/images/logo-160.png 1x, assets/images/logo-320.png 2x" alt="{BIZ['name']} logo" width="160" height="160">
      <span class="brand-text">
        <span class="brand-name">{BIZ['name']} LLC</span>
        <span class="brand-sub">Elevated Care &amp; Trusted Protection</span>
      </span>
    </a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav" aria-label="Main">
      <ul>
        <li><a href="index.html">Home</a></li>
        <li class="has-sub"><a href="about.html">About</a>
          <ul class="sub">
            <li><a href="about.html">Our Mission &amp; Philosophy</a></li>
            <li><a href="founder.html">Meet the Founder</a></li>
            <li><a href="commitment.html">Our Commitment &amp; Outcomes</a></li>
          </ul>
        </li>
        <li class="has-sub"><a href="services.html">Services</a>
          <ul class="sub">{nav_services_items()}</ul>
        </li>
        <li><a href="faq.html">FAQ</a></li>
        <li><a href="resources.html">Resources</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
    <div class="header-cta">
      <a class="btn btn--gold" href="contact.html">Request a Consultation</a>
      <a class="btn btn--outline" href="tel:{BIZ['phone_tel']}">Call Now</a>
    </div>
  </div>
</header>
<div class="badge-strip"><span class="star">★</span> Elevating the Standard of Care. Protecting What Matters Most. <span class="star">★</span></div>
"""


def commitment_cards(limit=None):
    items = EXPECT if limit is None else EXPECT[:limit]
    out = '<div class="testi-grid">'
    for i, (title, text) in enumerate(items):
        out += f"""
<article class="testi">
  <div class="stars">★★★★★</div>
  <h3>{title}</h3>
  <p>{text}</p>
  <div class="who">{illus(VALUE_ICONS[i], title, 'illus--avatar')}<span>What You Can Expect from Us</span></div>
</article>"""
    return out + "</div>"


def bottom_sections(include_contact=True):
    """Shared sections that appear under the main content on most pages (mirrors the reference layout)."""
    out = f"""
<section class="logo-strip">
  <div class="container">
    <h2>Our Professional Affiliations</h2>
    <div class="logo-row logo-row--3">
      {''.join(f'<div class="affil"><img src="assets/images/{f}" alt="{n}" loading="lazy" decoding="async"></div>' for f, n in AFFILIATIONS)}
    </div>
  </div>
</section>
<section class="section section--ivory">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Our Commitment</span>
      <h2>Meaningful Advocacy. Greater Peace of Mind. Protection With Purpose.</h2>
    </div>
    {commitment_cards(3)}
    <p style="text-align:center;margin-top:30px"><a class="btn btn--navy" href="commitment.html">See Our Full Commitment &amp; Expected Outcomes</a></p>
  </div>
</section>"""
    if include_contact:
        out += contact_section()
    return out


def contact_section(title="Contact Us", sub="Request a Consultation ↓"):
    return f"""
<section class="section" id="contact">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Get in touch</span>
      <h2>{title}</h2>
      <h3 style="font-family:var(--font-body);font-weight:400;color:var(--ink-soft)">{sub}</h3>
    </div>
    <div class="contact-grid">
      {form(uid="c")}
      <div class="contact-info">
        <h3>{BIZ['name']}</h3>
        <p style="color:var(--gold-soft);font-family:var(--font-head);font-style:italic">{BIZ['tagline']}</p>
        <h4>Address</h4>
        <p>{BIZ['address']}</p>
        <h4>Phone</h4>
        <p><a href="tel:{BIZ['phone_tel']}">{BIZ['phone']}</a></p>
        <h4>Email</h4>
        <p><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></p>
        <h4>Owner / Registered Agent</h4>
        <p>{BIZ['owner']}</p>
        <a class="btn btn--gold" href="mailto:{BIZ['email']}">Email Us</a>
        <a class="btn btn--outline-light" href="tel:{BIZ['phone_tel']}">Call Now</a>
        <p class="privacy-note">{FORM_DISCLAIMER}</p>
      </div>
    </div>
  </div>
</section>"""


def footer():
    svc_links = "".join(f'<li><a href="service-{s["slug"]}.html">{s["title"]}</a></li>' for s in SERVICES)
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-main">
      <div class="footer-brand">
        <a class="brand brand--footer" href="index.html"><img class="brand-logo brand-logo--lg" src="assets/images/logo-320.png" alt="{BIZ['name']} logo" width="320" height="320" loading="lazy"></a>
        <p class="tag">Elevating the Standard of Care. Protecting What Matters Most.</p>
        <p class="serving-footer">{BIZ['serving']}</p>
        <h5>Address</h5><p>{BIZ['address']}</p>
        <h5>Phone</h5><p><a href="tel:{BIZ['phone_tel']}">{BIZ['phone']}</a></p>
        <h5>Email</h5><p><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></p>
        <div style="margin-top:16px">
          <a class="btn btn--gold" href="contact.html">Request a Consultation</a>
          <a class="btn btn--outline-light" href="tel:{BIZ['phone_tel']}">Call Now</a>
        </div>
      </div>
      <div>
        <h4>Our Services</h4>
        <ul>{svc_links}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">Our Mission &amp; Philosophy</a></li>
          <li><a href="founder.html">Meet the Founder</a></li>
          <li><a href="commitment.html">Our Commitment &amp; Outcomes</a></li>
          <li><a href="services.html#who-we-serve">Who We Serve</a></li>
          <li><a href="faq.html">Frequently Asked Questions</a></li>
          <li><a href="resources.html">Guardianship Resources</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
        <div class="footer-cred">
          <strong>{BIZ['owner']}</strong>
          National Certified Guardian — Owner / Registered Agent
          <div style="margin-top:10px"><img class="cert-badge" src="assets/images/affil-cgc.png" alt="Center for Guardianship Certification"></div>
        </div>
      </div>
      <div class="footer-map">
        <h4>Visit Us</h4>
        {illus('footer-map', 'Map of Pennsylvania and Delaware with a pin at Media, PA', 'illus--map')}
        <p class="addr">{BIZ['name']}<br>{BIZ['address']}</p>
      </div>
    </div>
    <div class="footer-legal">
      <p class="policy"><a href="#">Privacy Policy</a> | <a href="#">Terms of Use</a> | <a href="#">Accessibility</a></p>
      <p class="disclaimer"><strong>Disclaimer:</strong> The information presented on this website is for general informational purposes only and is not legal advice. A consultation does not establish a guardianship relationship, guarantee acceptance of an appointment, or replace legal advice from an attorney. In Pennsylvania, guardianship authority must be granted by the court. Specific services depend on the authority granted by the court, the needs of the individual, and our capacity to accept the appointment. Please do not send sensitive medical, financial, or identifying information through this website.</p>
      <p class="copy">Copyright © <span data-year>2026</span> {BIZ['legal']}. All Rights Reserved. &nbsp;·&nbsp; {BIZ['tagline']}</p>
    </div>
  </div>
</footer>
<a class="float-cta" href="contact.html">Request a Consultation</a>
<div class="mobile-bar" role="navigation" aria-label="Quick actions">
  <a class="btn btn--outline" href="tel:{BIZ['phone_tel']}">Call Now</a>
  <a class="btn btn--gold" href="contact.html">Request a Consultation</a>
</div>
"""


def page(filename, title, body, description=""):
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0b1f3a">
<title>{html.escape(title)} | {BIZ['name']}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="icon" type="image/png" href="assets/images/favicon.png">
<link rel="apple-touch-icon" href="assets/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{header()}
<main>
{body}
</main>
{footer()}
<script src="assets/main.js"></script>
</body>
</html>
"""
    (OUT / filename).write_text(doc, encoding="utf-8")
    print("wrote", filename)


def page_title(h1, crumb, meta=None, lead=None):
    meta_html = f'<p class="meta">{meta}</p>' if meta else ""
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f"""
<section class="page-title">
  <div class="container">
    <p class="breadcrumb"><a href="index.html">Home</a><span>›</span>{crumb}</p>
    <h1>{h1}</h1>
    {meta_html}{lead_html}
  </div>
</section>"""


def service_sidebar(active_slug=None):
    links = ""
    for s in SERVICES:
        cls = ' class="active"' if s["slug"] == active_slug else ""
        links += f'<li{cls}><a href="service-{s["slug"]}.html">{s["title"]}</a></li>'
    return f"""
<aside class="sidebar">
  <div class="side-card side-card--navy">
    {founder_img()}
    <h3>Diamond P. Foster, NCG</h3>
    <small>Founder | National Certified Guardian</small>
    <div class="call">{BIZ['phone']}</div>
    <small>Call Now</small>
    <a class="btn btn--gold btn--block" href="contact.html">Request a Consultation</a>
  </div>
  <div class="side-card">
    <h3>Our Guardianship Services</h3>
    <ul class="side-nav">{links}</ul>
  </div>
  <div class="side-card side-card--newsletter">
    <h3>Stay in Touch</h3>
    <form class="js-form" action="{FORM_ENDPOINT}" method="POST">{form_hidden("Stay in Touch signup — True Diamond website")}
      <div class="form-grid">
        <div class="field"><label for="sb-fn">First Name</label><input id="sb-fn" type="text" name="first_name" required></div>
        <div class="field"><label for="sb-ln">Last Name</label><input id="sb-ln" type="text" name="last_name"></div>
        <div class="field"><label for="sb-em">Email</label><input id="sb-em" type="email" name="email" required></div>
        <div class="field"><label for="sb-ph">Phone / Mobile</label><input id="sb-ph" type="tel" name="phone"></div>
      </div>
      <button class="btn btn--navy btn--block" type="submit" style="margin-top:12px">Submit</button>
      <div class="form-success">Thank you — we will be in touch.</div>
      <div class="form-error">Sorry — that didn't go through. Please email <a href="mailto:{BIZ['email']}">{BIZ['email']}</a>.</div>
    </form>
  </div>
</aside>"""


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def build_home():
    svc_cards = ""
    for i, s in enumerate(SERVICES, 1):
        svc_cards += f"""
<a class="service-card" href="service-{s['slug']}.html">
  <div class="num">{i:02d}</div>
  <h3>{s['title']}</h3>
  <p>{s['short']}</p>
  <span class="more">Learn more</span>
</a>"""

    faq_items = ""
    for i, (q, a) in enumerate(FAQ[:3]):
        faq_items += f"""
<div class="faq-item{' open' if i == 0 else ''}">
  <button class="faq-q" aria-expanded="{'true' if i == 0 else 'false'}">{q}</button>
  <div class="faq-a">{a}</div>
</div>"""

    resources = ""
    for i, (title, url, source, desc) in enumerate(RESOURCES):
        resources += f"""
<article class="post-card">
  {illus(ARTICLE_ILLUS[i], title, 'illus--card')}
  <div class="post-body">
    <span class="eyebrow">{source}</span>
    <h3><a href="{url}" target="_blank" rel="noopener">{title}</a></h3>
    <p>{desc}</p>
    <a class="more" href="{url}" target="_blank" rel="noopener">Read More</a>
  </div>
</article>"""

    body = f"""
<section class="hero" id="top">
  <div class="container">
    <div>
      <span class="eyebrow">Professional Guardianship &amp; Advocacy Services</span>
      <h1>True Diamond Life Care Group LLC.</h1>
      <h2>Exceptional Guardianship, Compassionate Advocacy, Uncompromising Integrity</h2>
      <p class="serving">{BIZ['serving']}</p>
      <p>At True Diamond Life Care Group, we are dedicated to protecting individual rights, preserving dignity, and promoting the well-being of those entrusted to our care. Through compassionate advocacy, professional excellence, and unwavering integrity, we deliver personalized guardianship services that honor each individual's unique needs, preferences, and quality of life.</p>
      <div class="hero-actions">
        <a class="btn btn--gold" href="contact.html">Request a Consultation</a>
        <a class="btn btn--outline-light" href="services.html">Explore Our Services</a>
      </div>
    </div>
    <div>
      <p class="hero-quote-label">Let's Start the Conversation.<br><small>Compassionate Guidance begins here.</small></p>
      {form(uid="h")}
    </div>
  </div>
</section>

<section class="features">
  <div class="container">
    <div class="section-head section-head--tight">
      <span class="eyebrow">The Principles Behind Our Promise</span>
      <h2>An unwavering commitment to dignity, integrity, and individualized care.</h2>
    </div>
    <div class="feature-grid">
      <div class="feature">
        <div class="feature-icon"><svg viewBox="0 0 24 24"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg></div>
        <h3>Compassionate Advocacy</h3>
        <p>We are committed to ensuring every individual's needs are heard, their preferences are respected, and their best interests remain a priority.</p>
      </div>
      <div class="feature">
        <div class="feature-icon"><svg viewBox="0 0 24 24"><path d="M3 21h18"/><path d="M5 21V10l7-6 7 6v11"/><path d="M10 21v-6h4v6"/></svg></div>
        <h3>Ethical Leadership</h3>
        <p>Our practice is grounded in integrity, transparency, and accountability. We uphold professional guardianship standards while exercising sound judgment and responsible stewardship in every aspect of our work.</p>
      </div>
      <div class="feature">
        <div class="feature-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></svg></div>
        <h3>Person-Centered Care</h3>
        <p>Our approach prioritizes personal choice, meaningful participation, and the preservation of independence to the greatest extent possible.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="container">
    <div class="about-grid">
      <div class="about-media">
        {founder_img()}
        <div class="caption">Diamond P. Foster, NCG<small>Founder | National Certified Guardian</small></div>
      </div>
      <div class="about-text">
        <span class="eyebrow">About True Diamond Life Care Group</span>
        <h2>A Higher Standard of Guardianship. A Commitment You Can Trust.</h2>
        <p><strong>Providing distinguished guardianship services grounded in professional excellence, ethical responsibility, and compassionate advocacy.</strong></p>
        <p>At True Diamond Life Care Group, we recognize that guardianship is more than a legal responsibility. It is a profound commitment to protecting individual rights, preserving dignity, and enhancing the quality of life of those who depend on our advocacy.</p>
        <p>Founded on the principles of integrity, accountability, and individualized attention, our practice delivers thoughtful, person-centered guardianship services tailored to the unique circumstances of every individual we serve.</p>
        <p>Led by Diamond Foster, a National Certified Guardian with extensive hands-on guardianship experience, True Diamond Life Care Group combines professional knowledge with a deeply personal commitment to those we represent. We work to build confidence among families, legal professionals, and the courts through responsible decision-making, transparent communication, and steadfast advocacy.</p>
        <p><strong>Our philosophy is simple: Every life has value. Every voice matters. And every individual deserves to be represented with dignity, compassion, and unwavering integrity.</strong></p>
        <a class="btn btn--navy" href="about.html">Discover Our Mission</a>
        <a class="btn btn--outline" href="founder.html" style="margin-left:8px">Meet the Founder</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--ivory" id="services">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Our Services</span>
      <h2>Our Guardianship Services</h2>
      <p class="lead">Individualized guardianship services designed to protect the rights, dignity, and well-being of individuals who require assistance with personal decision-making.</p>
    </div>
    <div class="service-grid">{svc_cards}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Frequently Asked Questions</span>
      <h2>Your Questions. Answered.</h2>
    </div>
    <div class="faq-list">{faq_items}</div>
    <p style="text-align:center;margin-top:30px"><a class="btn btn--outline" href="faq.html">View All Frequently Asked Questions</a></p>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>Still have questions? We're Here to Help.</h2>
      <p>We welcome inquiries from families, attorneys, and professionals seeking information about our services and potential referrals.</p>
    </div>
    <a class="btn btn--gold" href="contact.html">Talk To Us Today</a>
  </div>
</section>

<section class="section section--ivory">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Knowledge • Advocacy • Empowerment</span>
      <h2>Guardianship <a href="resources.html">Resources</a></h2>
      <p class="lead">{RESOURCES_INTRO}</p>
    </div>
    <div class="card-grid">{resources}</div>
  </div>
</section>

{bottom_sections()}
"""
    page("index.html", "Elevated Care. Trusted Protection.", body,
         "True Diamond Life Care Group provides professional guardianship and advocacy services, now serving Pennsylvania and Delaware. Elevated Care. Trusted Protection.")


def build_about():
    expect = ""
    for i, (t, txt) in enumerate(EXPECT, 1):
        expect += f'<div class="value"><div class="mark">{i}</div><div><h3>{t}</h3><p>{txt}</p></div></div>'
    body = page_title("About True Diamond Life Care Group", "About",
                      meta="Our Mission &amp; Philosophy",
                      lead="Where Care is Elevated and Protection is Assured.") + f"""
<section class="inner">
  <div class="container">
    <div class="inner-grid">
      <div class="content">
        <h2>Our Mission</h2>
        <p class="intro">At True Diamond Life Care Group, our mission is to safeguard dignity, protect individual rights, and champion the well-being of those entrusted to our care through compassionate advocacy, empathetic service, and unwavering integrity.</p>
        <p>We are committed to ensuring that every individual is treated with respect, every voice is valued, and every decision reflects the person's best interests, unique needs, and inherent right to dignity.</p>

        {illus('about-mission', 'An individual held safe within a diamond-shaped shield, supported by open hands', 'illus--wide')}

        <h2>Our Philosophy</h2>
        <p>We believe guardianship is more than a professional responsibility—it's a commitment to humanity, trust, and the protection of those who may be unable to fully advocate for themselves.</p>
        <p>Through ethical leadership, transparency, accountability, and person-centered care, we strive to preserve independence whenever possible, fully empower individuals, and provide families, legal professionals, and the courts with confidence in our advocacy.</p>

        <div class="callout">
          <h3 style="margin-top:0">A Commitment You Can Trust</h3>
          <p>Because every life holds value. Every voice deserves to be heard. And every person deserves an advocate who leads with empathy, acts with integrity, and protects with unwavering purpose.</p>
          <p>Discover how True Diamond Life Care Group is committed to making a meaningful difference.</p>
        </div>

        <h2>What You Can Expect from Us</h2>
        <div class="value-grid">{expect}</div>

        <p style="margin-top:32px"><a class="btn btn--navy" href="founder.html">Meet the Founder</a> <a class="btn btn--outline" href="contact.html" style="margin-left:8px">Request a Consultation</a></p>
      </div>
      {service_sidebar()}
    </div>
  </div>
</section>
{bottom_sections()}
"""
    page("about.html", "About Us", body, "Our mission and philosophy: safeguarding dignity, protecting individual rights, and championing the well-being of those entrusted to our care.")


def build_founder():
    body = page_title("Meet the Founder", "About <span>›</span> Meet the Founder",
                      meta="Diamond Foster | Founder, True Diamond Life Care Group") + f"""
<section class="inner">
  <div class="container">
    <div class="founder-grid">
      <div class="founder-card">
        {founder_img()}
        <div class="name-block"><strong>Diamond P. Foster, NCG</strong><span>Founder | National Certified Guardian</span></div>
      </div>
      <div class="content founder-text">
        <span class="eyebrow">Introduction</span>
        <h2>Diamond Foster</h2>
        <p class="intro">My journey in guardianship has been shaped by five years of hands-on experience, a deep respect for human dignity, and a commitment to protecting the rights and well-being of vulnerable individuals.</p>
        <p>As a nationally certified guardian, I understand that effective guardianship requires more than professional knowledge—it demands sound judgment, unwavering integrity, genuine empathy, and a profound sense of responsibility to those entrusted to your care.</p>
        <blockquote>I founded True Diamond Life Care Group with a clear vision: to provide principled, person-centered guardianship services that honor everyone's dignity, preserve their voice, and prioritize their best interests.</blockquote>
        <p>My approach is grounded in the belief that every person deserves to be treated with compassion, advocated for with purpose, and protected with the highest level of professionalism.</p>
        <p>Through True Diamond Life Care Group, I am committed to making a meaningful difference in the lives of those I serve, building trust with families and professionals, and upholding the responsibility of guardianship with the integrity and dedication it deserves.</p>
        <div class="callout">
          <p><strong>Credentials:</strong> National Certified Guardian (NCG) · Five years of hands-on guardianship experience · Owner / Registered Agent, {BIZ['legal']}</p>
        </div>
        <p><a class="btn btn--gold" href="contact.html">Request a Consultation</a> <a class="btn btn--outline" href="services.html" style="margin-left:8px">Our Services</a></p>
      </div>
    </div>
  </div>
</section>
{bottom_sections()}
"""
    page("founder.html", "Meet the Founder", body, "Meet Diamond Foster, founder of True Diamond Life Care Group and nationally certified guardian.")


def build_services():
    svc_cards = ""
    for i, s in enumerate(SERVICES, 1):
        svc_cards += f"""
<a class="service-card" href="service-{s['slug']}.html">
  <div class="num">{i:02d}</div>
  <h3>{s['title']}</h3>
  <p>{s['short']}</p>
  <span class="more">Learn more</span>
</a>"""
    serve = "".join(f"<li>{w}</li>" for w in WHO_WE_SERVE)
    body = page_title("Our Services", "Services",
                      meta="Guardianship Services in Pennsylvania",
                      lead="At True Diamond Life Care Group, we provide individualized guardianship services designed to protect the rights, dignity, and well-being of individuals who require assistance with personal decision-making. Every service is delivered with professionalism, empathy, integrity, and respect for everyone's unique circumstances.") + f"""
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">What we do</span>
      <h2>Our Guardianship Services</h2>
    </div>
    <div class="service-grid">{svc_cards}</div>
  </div>
</section>

<section class="section section--ivory" id="who-we-serve">
  <div class="container">
    <div class="about-grid">
      <div class="about-media">{illus('who-we-serve', 'Adults across the lifespan, including an older adult and a wheelchair user, under an arc of protection', 'illus--portrait')}</div>
      <div class="about-text">
        <span class="eyebrow">Services</span>
        <h2>Who We Serve</h2>
        <p>True Diamond Life Care Group aims to support individuals across the lifespan who require court-appointed guardianship, subject to applicable law, court authorization, and our service capacity.</p>
        <ul class="serve-list">{serve}</ul>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>Discuss a Potential Referral</h2>
      <p>Specific services depend on the authority granted by the court, the needs of the individual, and our capacity to accept the appointment.</p>
    </div>
    <a class="btn btn--gold" href="contact.html">Contact Us</a>
  </div>
</section>
{bottom_sections()}
"""
    page("services.html", "Our Services", body, "Individualized guardianship services designed to protect the rights, dignity, and well-being of individuals who require assistance with personal decision-making.")


def build_service_pages():
    for s in SERVICES:
        paragraphs = "".join(f"<p class='intro'>{p}</p>" for p in s["body"])
        includes = "".join(f"<li>{i}</li>" for i in s["includes"])
        serve = "".join(f"<li>{w}</li>" for w in WHO_WE_SERVE)
        body = page_title(s["title"], f'<a href="services.html">Services</a><span>›</span>{s["title"]}',
                          meta="Guardianship Services · Media, Pennsylvania") + f"""
<section class="inner">
  <div class="container">
    <div class="inner-grid">
      <div class="content">
        <h2>{s['title']} Services We Provide</h2>
        {paragraphs}
        <div class="inline-form">{form(heading="Request a Consultation", note="Tell us about the situation and we will follow up to discuss whether our services may be an appropriate fit.", uid="s")}</div>

        {illus('service-' + s['slug'], SERVICE_ALT[s['slug']], 'illus--wide')}

        <h2>What This Service Includes</h2>
        <ul class="check-list">{includes}</ul>

        <h2>Who We Serve</h2>
        <p>True Diamond Life Care Group aims to support individuals across the lifespan who require court-appointed guardianship, subject to applicable law, court authorization, and our service capacity.</p>
        <ul>{serve}</ul>

        <h2>Our Approach</h2>
        <p>At True Diamond Life Care Group, we believe that effective guardianship should make a meaningful difference in the lives of the individuals entrusted to our care. Our goal is to promote dignity, safeguard individual rights, support personal well-being, and ensure that every guardianship responsibility is approached with compassion, integrity, and accountability.</p>
        <p>Through thoughtful advocacy, responsible decision-making, and individualized attention, we strive to achieve outcomes that reflect each person's unique needs, preferences, circumstances, and best interests.</p>

        <div class="callout">
          <h3 style="margin-top:0">Our Promise</h3>
          <p>We approach every guardianship with the understanding that we have been entrusted with profound responsibility. While individual circumstances and outcomes may vary, our commitment to ethical service, empathetic advocacy, and professional accountability remains constant.</p>
        </div>

        <p class="note">Specific services depend on the authority granted by the court, the needs of the individual, and our capacity to accept the appointment. Please <a href="contact.html">contact us</a> to discuss a potential referral.</p>

        <h2>Work With a National Certified Guardian</h2>
        <p>If you are a family member, attorney, healthcare professional, or social worker seeking a qualified, compassionate guardian, True Diamond Life Care Group welcomes your inquiry.</p>
        <p><strong>Contact us today to discuss a potential referral.</strong></p>
        <p><a class="btn btn--gold" href="contact.html">Request a Consultation</a></p>
      </div>
      {service_sidebar(s['slug'])}
    </div>
  </div>
</section>
{bottom_sections()}
"""
        page(f"service-{s['slug']}.html", s["title"], body, s["short"])


def build_commitment():
    expect = ""
    for i, (t, txt) in enumerate(EXPECT, 1):
        expect += f'<div class="value"><div class="mark">{i}</div><div><h3>{t}</h3><p>{txt}</p></div></div>'
    body = page_title("Our Commitment &amp; Expected Outcomes", "Services <span>›</span> Our Commitment",
                      meta="Meaningful Advocacy. Greater Peace of Mind. Protection With Purpose.") + f"""
<section class="inner">
  <div class="container">
    <div class="inner-grid">
      <div class="content">
        <p class="intro">At True Diamond Life Care Group, we believe that effective guardianship should make a meaningful difference in the lives of the individuals entrusted to our care. Our goal is to promote dignity, safeguard individual rights, support personal well-being, and ensure that every guardianship responsibility is approached with compassion, integrity, and accountability.</p>
        <p>Through thoughtful advocacy, responsible decision-making, and individualized attention, we strive to achieve outcomes that reflect each person's unique needs, preferences, circumstances, and best interests.</p>

        <h2>What You Can Expect from Us</h2>
        <div class="value-grid">{expect}</div>

        <h2>Our Definition of Success</h2>
        <p>At True Diamond Life Care Group, success is not measured solely by completed paperwork or fulfilled legal obligations. It is reflected in the quality of our advocacy, the care with which decisions are made, the dignity afforded by every individual, and the diligence applied to every responsibility.</p>
        <p>We strive to ensure that each person entrusted to our care is treated with compassion, protected within the scope of our authority, and supported in a manner that recognizes their individuality and inherent worth.</p>

        <div class="callout">
          <h3 style="margin-top:0">Our Promise</h3>
          <p>We approach every guardianship with the understanding that we have been entrusted with profound responsibility. While individual circumstances and outcomes may vary, our commitment to ethical service, empathetic advocacy, and professional accountability remains constant.</p>
          <p>Because meaningful guardianship is not simply about making decisions. It is about protecting dignity, honoring individuality, and making every decision with purpose, compassion, and integrity.</p>
          <p><strong>True Diamond Life Care Group — Elevated Care, Trusted Protection.</strong></p>
        </div>
      </div>
      {service_sidebar()}
    </div>
  </div>
</section>
{bottom_sections()}
"""
    page("commitment.html", "Our Commitment & Expected Outcomes", body, "Meaningful advocacy, greater peace of mind, protection with purpose: what you can expect from True Diamond Life Care Group.")


def build_faq():
    items = ""
    for i, (q, a) in enumerate(FAQ):
        items += f"""
<div class="faq-item{' open' if i == 0 else ''}">
  <button class="faq-q" aria-expanded="{'true' if i == 0 else 'false'}">{i + 1}. {q}</button>
  <div class="faq-a">{a}</div>
</div>"""
    body = page_title("Frequently Asked Questions", "FAQ",
                      lead="At True Diamond Life Care Group, we understand that guardianship can raise important questions for individuals, families, and professionals. We believe informed decisions begin with clear communication, transparency, and trust. Below are answers to common questions about our guardianship services.") + f"""
<section class="section">
  <div class="container">
    <div class="faq-list">{items}</div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>Still have questions? We're Here to Help.</h2>
      <p>Understanding guardianship is an important step toward ensuring that an individual's rights, dignity, and well-being remain protected. We welcome inquiries from families, attorneys, and professionals seeking information about our services and potential referrals.</p>
    </div>
    <a class="btn btn--gold" href="contact.html">Contact Us</a>
  </div>
</section>
{bottom_sections()}
"""
    page("faq.html", "Frequently Asked Questions", body, "Answers to common questions about court-appointed guardianship in Pennsylvania and our guardianship services.")


def build_resources():
    items = ""
    for i, (title, url, source, desc) in enumerate(RESOURCES):
        items += f"""
<article class="resource">
  {illus(ARTICLE_ILLUS[i], title, 'illus--wide')}
  <div>
    <span class="eyebrow">{source}</span>
    <h3><a href="{url}" target="_blank" rel="noopener">{title}</a></h3>
    <p>{desc}</p>
    <a class="url" href="{url}" target="_blank" rel="noopener">{url}</a>
  </div>
</article>"""
    body = page_title("Guardianship Resources", "Resources",
                      meta="Knowledge • Advocacy • Empowerment",
                      lead=RESOURCES_INTRO) + f"""
<section class="section section--ivory">
  <div class="container" style="max-width:960px">{items}
    <p class="note" style="margin-top:28px;font-size:0.9rem;color:var(--ink-soft)">We do not endorse the websites we link to and are not responsible for their content.</p>
  </div>
</section>
{bottom_sections()}
"""
    page("resources.html", "Guardianship Resources", body, "Trusted educational resources on guardianship responsibilities, professional standards, and ethical, person-centered care.")


def build_contact():
    body = page_title("Contact Us", "Contact",
                      meta="We're Here to Help",
                      lead="We welcome inquiries from families, attorneys, healthcare professionals, social workers, and other individuals seeking information about our guardianship services or a potential referral.") + f"""
{contact_section(title="Request a Consultation", sub="Tell us how we can help ↓")}
<section class="section section--ivory">
  <div class="container">
    <div class="about-grid">
      <div class="about-media">{illus('contact-location', 'Map of Pennsylvania and Delaware with a location pin at Media, PA, envelope and phone', 'illus--wide')}</div>
      <div class="about-text">
        <span class="eyebrow">Still have questions?</span>
        <h2>We're Here to Help</h2>
        <p>Understanding guardianship is an important step toward ensuring that an individual's rights, dignity, and well-being remain protected. We welcome inquiries from families, attorneys, and professionals seeking information about our services and potential referrals.</p>
        <p>We are committed to approaching every potential appointment with professionalism, empathy, integrity, and respect for the individuals and families we serve.</p>
        <p><strong>{BIZ['name']}</strong><br>{BIZ['tagline']}</p>
        <a class="btn btn--navy" href="faq.html">Read Our FAQ</a>
      </div>
    </div>
  </div>
</section>
{bottom_sections(include_contact=False)}
"""
    page("contact.html", "Contact Us", body, "Contact True Diamond Life Care Group in Media, Pennsylvania to inquire about guardianship services or a potential referral.")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_home()
    build_about()
    build_founder()
    build_services()
    build_service_pages()
    build_commitment()
    build_faq()
    build_resources()
    build_contact()
    print("done")
