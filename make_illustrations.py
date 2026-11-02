#!/usr/bin/env python3
"""
Generates the site's illustration set as SVG files in site/assets/images/illus/.
Every illustration is original line art in the brand palette, built so the
picture says the same thing the text beside it says.
"""
from pathlib import Path

OUT = Path(__file__).parent / "site" / "assets" / "images" / "illus"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#0b1f3a"; NAVY_D = "#071527"; NAVY_S = "#163055"
GOLD = "#c9a84c"; GOLD_S = "#e3cf8f"; GOLD_D = "#a8862f"
IVORY = "#f8f5ee"; IVORY_D = "#efe9dc"

# ----------------------------------------------------------------------------
# Scene helpers
# ----------------------------------------------------------------------------
def scene(w, h, body, cx=None, cy=None, halo=True):
    cx = w / 2 if cx is None else cx
    cy = h / 2 if cy is None else cy
    halo_svg = f"""
  <circle cx="{cx}" cy="{cy}" r="{min(w, h) * 0.34}" fill="url(#halo)"/>
  <circle cx="{cx}" cy="{cy}" r="{min(w, h) * 0.40}" fill="none" stroke="{GOLD}" stroke-opacity=".25" stroke-width="2"/>
  <circle cx="{cx}" cy="{cy}" r="{min(w, h) * 0.46}" fill="none" stroke="{GOLD}" stroke-opacity=".12" stroke-width="2" stroke-dasharray="6 10"/>""" if halo else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{NAVY_D}"/><stop offset=".55" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY_S}"/>
    </linearGradient>
    <radialGradient id="halo" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="{GOLD}" stop-opacity=".22"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{GOLD_S}"/><stop offset="1" stop-color="{GOLD_D}"/>
    </linearGradient>
    <pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M48 0H0V48" fill="none" stroke="{IVORY}" stroke-opacity=".04"/>
    </pattern>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <rect width="{w}" height="{h}" fill="url(#grid)"/>
  <!-- faint diamond watermark -->
  <g transform="translate({w - 150},{h - 130}) scale(1.2)" fill="none" stroke="{GOLD}" stroke-opacity=".10" stroke-width="3">
    <path d="M-60 -20 L-30 -60 L30 -60 L60 -20 L0 60 Z"/><path d="M-60 -20 H60 M-30 -60 L0 -20 L30 -60 M0 -20 V60"/>
  </g>{halo_svg}
  <g fill="none" stroke="{GOLD_S}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round">
{body}
  </g>
</svg>
"""

# reusable glyphs ---------------------------------------------------------------
def person(x, y, s=1.0, fill=IVORY):
    """Simple head+shoulders figure, centred at x; y is top of head."""
    return f"""    <g transform="translate({x},{y}) scale({s})" stroke="none" fill="{fill}">
      <circle cx="0" cy="34" r="34"/>
      <path d="M-70 170 C-70 108 -38 84 0 84 C38 84 70 108 70 170 Z"/>
    </g>"""

def shield(x, y, s=1.0, stroke=GOLD_S, fill="none"):
    return f"""    <path transform="translate({x},{y}) scale({s})" d="M0 -120 L105 -78 V0 C105 72 50 118 0 140 C-50 118 -105 72 -105 0 V-78 Z" fill="{fill}" stroke="{stroke}"/>"""

def check(x, y, s=1.0):
    return f"""    <path transform="translate({x},{y}) scale({s})" d="M-34 4 L-8 30 L40 -28"/>"""

def heart(x, y, s=1.0, fill=GOLD):
    return f"""    <path transform="translate({x},{y}) scale({s})" fill="{fill}" stroke="none" d="M0 40 C-60 0 -60 -50 -30 -50 C-14 -50 -4 -40 0 -30 C4 -40 14 -50 30 -50 C60 -50 60 0 0 40 Z"/>"""

def doc(x, y, w=150, h=190, lines=4):
    ls = "".join(f'    <path d="M{x+30} {y+60+i*30} H{x+w-30}" stroke-width="7" stroke-opacity=".8"/>\n' for i in range(lines))
    return f"""    <path d="M{x} {y} H{x+w-40} L{x+w} {y+40} V{y+h} H{x} Z" fill="{NAVY_S}" fill-opacity=".7"/>
    <path d="M{x+w-40} {y} V{y+40} H{x+w}"/>
{ls}"""

def seal(x, y, r=34):
    return f"""    <circle cx="{x}" cy="{y}" r="{r}" fill="{GOLD}" stroke="none"/>
    <circle cx="{x}" cy="{y}" r="{r-10}" fill="none" stroke="{NAVY}" stroke-width="4"/>
    <path d="M{x-14} {y} L{x-4} {y+10} L{x+14} {y-10}" stroke="{NAVY}" stroke-width="5"/>"""

def hands_cradle(x, y, s=1.0):
    """Two open hands cupping upward beneath point (x,y)."""
    return f"""    <g transform="translate({x},{y}) scale({s})">
      <path d="M-20 60 C-80 60 -120 30 -140 -20 C-150 -46 -130 -58 -112 -40 L-80 0" />
      <path d="M-112 -40 C-120 -70 -92 -78 -80 -52 L-62 -10"/>
      <path d="M-80 -52 C-84 -80 -56 -86 -46 -60 L-36 -20"/>
      <path d="M-46 -60 C-46 -84 -20 -86 -14 -62 L-10 -20"/>
      <path d="M20 60 C80 60 120 30 140 -20 C150 -46 130 -58 112 -40 L80 0" />
      <path d="M112 -40 C120 -70 92 -78 80 -52 L62 -10"/>
      <path d="M80 -52 C84 -80 56 -86 46 -60 L36 -20"/>
      <path d="M46 -60 C46 -84 20 -86 14 -62 L10 -20"/>
      <path d="M-20 60 Q0 70 20 60"/>
    </g>"""

def building(x, y, w=420, h=260, cols=5):
    """Courthouse: pediment + columns + steps."""
    colw = 26
    gap = (w - 80) / (cols - 1)
    colsvg = "".join(f'    <rect x="{x+40+i*gap-colw/2}" y="{y+70}" width="{colw}" height="{h-130}" rx="4" fill="{NAVY_S}"/>\n' for i in range(cols))
    return f"""    <path d="M{x-10} {y+40} L{x+w/2} {y-60} L{x+w+10} {y+40} Z" fill="{NAVY_S}" fill-opacity=".8"/>
    <rect x="{x}" y="{y+40}" width="{w}" height="30" rx="4" fill="{NAVY_S}"/>
{colsvg}    <rect x="{x-10}" y="{y+h-60}" width="{w+20}" height="24" rx="4" fill="{NAVY_S}"/>
    <rect x="{x-30}" y="{y+h-36}" width="{w+60}" height="24" rx="4" fill="{NAVY_S}"/>
    <circle cx="{x+w/2}" cy="{y+5}" r="18" fill="{GOLD}" stroke="none"/>"""

def write(name, svg):
    (OUT / f"{name}.svg").write_text(svg)
    print("wrote", name)

W, H = 1200, 675   # wide 16:9

# ----------------------------------------------------------------------------
# SERVICE ILLUSTRATIONS (16:9)
# ----------------------------------------------------------------------------
# 1. Court-Appointed Guardianship — courthouse, gavel, sealed court order
write("service-court-appointed-guardianship", scene(W, H, f"""
{building(390, 190, 420, 260)}
    <!-- gavel -->
    <g transform="translate(900,330) rotate(-35)">
      <rect x="-24" y="-90" width="48" height="150" rx="14" fill="{GOLD}" stroke="none"/>
      <rect x="-70" y="-110" width="140" height="42" rx="12" fill="{GOLD}" stroke="none"/>
      <path d="M0 60 V200" stroke-width="18"/>
    </g>
    <path d="M820 520 H1040" stroke-width="14"/>
    <!-- court order with seal -->
{doc(160, 290, 170, 210, 4)}
{seal(300, 470, 36)}
    <!-- shield + person: the protected individual -->
{shield(600, 440, .55, GOLD_S, NAVY_S)}
{person(600, 395, .36)}
"""))

# 2. Person-Centered Advocacy — individual at the centre, voice heard, heart
write("service-person-centered-advocacy", scene(W, H, f"""
    <circle cx="600" cy="340" r="150" stroke-opacity=".9"/>
    <circle cx="600" cy="340" r="215" stroke-opacity=".35" stroke-width="4"/>
{person(600, 230, .85)}
    <!-- speech bubble: their voice -->
    <path d="M740 150 H940 Q965 150 965 175 V250 Q965 275 940 275 H800 L760 310 V275 H740 Q715 275 715 250 V175 Q715 150 740 150 Z" fill="{NAVY_S}"/>
    <path d="M760 195 H920 M760 232 H880" stroke-width="7"/>
    <!-- heart: compassion -->
{heart(300, 300, 1.4)}
    <!-- surrounding supporters -->
{person(260, 480, .4, GOLD_S)}
{person(940, 480, .4, GOLD_S)}
    <path d="M330 560 Q600 640 870 560" stroke-dasharray="2 22" stroke-width="8"/>
"""))

# 3. Healthcare & Medical Decision Support — heartbeat, stethoscope, care plan
write("service-healthcare-decision-support", scene(W, H, f"""
    <!-- medical cross -->
    <g transform="translate(600,300)">
      <circle r="150" fill="{NAVY_S}" fill-opacity=".8"/>
      <path d="M-40 -100 H40 V-40 H100 V40 H40 V100 H-40 V40 H-100 V-40 H-40 Z" fill="{GOLD}" stroke="none"/>
    </g>
    <!-- heartbeat line -->
    <path d="M90 520 H330 L380 440 L430 600 L480 480 L520 560 L560 520 H640 L680 460 L720 580 L770 520 H1110" stroke-width="8"/>
    <!-- stethoscope -->
    <g transform="translate(250,250)">
      <path d="M-70 -120 V-20 C-70 40 -20 70 10 70 C40 70 90 40 90 -20 V-120"/>
      <path d="M10 70 V120 C10 170 60 190 100 190 C140 190 180 160 180 120 V60" />
      <circle cx="180" cy="40" r="26" fill="{GOLD}" stroke="none"/>
    </g>
    <!-- care plan clipboard -->
{doc(890, 160, 180, 230, 0)}
    <rect x="940" y="140" width="80" height="40" rx="10" fill="{GOLD}" stroke="none"/>
{check(935, 235, .7)}    <path d="M985 235 H1045" stroke-width="7"/>
{check(935, 290, .7)}    <path d="M985 290 H1045" stroke-width="7"/>
{check(935, 345, .7)}    <path d="M985 345 H1045" stroke-width="7"/>
"""))

# 4. Estate & Financial Guardianship — ledger, safeguarded assets, oversight
write("service-estate-financial-guardianship", scene(W, H, f"""
    <!-- vault / safeguarding -->
    <g transform="translate(330,330)">
      <rect x="-150" y="-150" width="300" height="300" rx="24" fill="{NAVY_S}" fill-opacity=".85"/>
      <circle r="80"/>
      <circle r="24" fill="{GOLD}" stroke="none"/>
      <path d="M0 -80 V-110 M0 80 V110 M-80 0 H-110 M80 0 H110 M-57 -57 L-78 -78 M57 57 L78 78 M-57 57 L-78 78 M57 -57 L78 -78" stroke-width="8"/>
    </g>
    <!-- ledger -->
    <g transform="translate(720,190)">
      <rect x="0" y="0" width="300" height="320" rx="14" fill="{NAVY_S}" fill-opacity=".85"/>
      <path d="M40 60 H260 M40 110 H180 M40 160 H200 M40 210 H170 M40 260 H260" stroke-width="7"/>
      <path d="M210 100 L240 120 L210 140 M205 150 L240 170 L205 190" stroke-width="6" stroke-opacity=".7"/>
      <circle cx="245" cy="258" r="14" fill="{GOLD}" stroke="none"/>
    </g>
    <!-- bar chart: monitoring income & expenses -->
    <path d="M740 600 H1060" stroke-width="8"/>
    <rect x="770" y="545" width="50" height="55" rx="6" fill="{GOLD}" stroke="none"/>
    <rect x="850" y="520" width="50" height="80" rx="6" fill="{GOLD_S}" stroke="none"/>
    <rect x="930" y="555" width="50" height="45" rx="6" fill="{GOLD}" stroke="none"/>
    <!-- shield with check: accountability -->
{shield(560, 560, .5, GOLD_S, NAVY_S)}
{check(560, 560, .9)}
"""))

# 5. Care Coordination & Service Advocacy — hub connecting providers
write("service-care-coordination", scene(W, H, f"""
    <!-- spokes -->
    <path d="M600 338 L300 170 M600 338 L900 170 M600 338 L240 480 M600 338 L960 480 M600 338 L600 590" stroke-width="6" stroke-dasharray="4 18"/>
    <!-- centre: the individual -->
    <circle cx="600" cy="338" r="95" fill="{NAVY_S}"/>
{person(600, 270, .55)}
    <!-- hospital -->
    <g transform="translate(300,170)"><circle r="70" fill="{NAVY_S}"/><path d="M-18 -40 H18 V-18 H40 V18 H18 V40 H-18 V18 H-40 V-18 H-18 Z" fill="{GOLD}" stroke="none"/></g>
    <!-- residence -->
    <g transform="translate(900,170)"><circle r="70" fill="{NAVY_S}"/><path d="M-44 4 L0 -36 L44 4 M-32 -6 V38 H32 V-6" /><rect x="-10" y="12" width="20" height="26" fill="{GOLD}" stroke="none"/></g>
    <!-- social worker / care team -->
    <g transform="translate(240,480)"><circle r="70" fill="{NAVY_S}"/>{person(0, -45, .3, GOLD)}</g>
    <!-- community resources -->
    <g transform="translate(960,480)"><circle r="70" fill="{NAVY_S}"/><path d="M-36 20 H36 M-28 20 V-10 H28 V20 M0 -10 V-38 M-14 -24 H14" /><circle cx="0" cy="-40" r="8" fill="{GOLD}" stroke="none"/></g>
    <!-- quality of life: heart -->
    <g transform="translate(600,590)"><circle r="60" fill="{NAVY_S}"/>{heart(0, 8, .8)}</g>
"""))

# 6. Court Reporting & Guardianship Compliance — calendar deadline, report stack, checks
write("service-court-reporting-compliance", scene(W, H, f"""
    <!-- calendar -->
    <g transform="translate(220,170)">
      <rect x="0" y="0" width="300" height="300" rx="16" fill="{NAVY_S}" fill-opacity=".85"/>
      <rect x="0" y="0" width="300" height="64" rx="16" fill="{GOLD}" stroke="none"/>
      <path d="M70 -20 V40 M230 -20 V40" stroke="{NAVY}" stroke-width="12"/>
      <g stroke="none" fill="{IVORY}" fill-opacity=".35">
        <rect x="34" y="96" width="44" height="36" rx="6"/><rect x="104" y="96" width="44" height="36" rx="6"/><rect x="174" y="96" width="44" height="36" rx="6"/><rect x="244" y="96" width="30" height="36" rx="6"/>
        <rect x="34" y="156" width="44" height="36" rx="6"/><rect x="104" y="156" width="44" height="36" rx="6"/><rect x="244" y="156" width="30" height="36" rx="6"/>
        <rect x="34" y="216" width="44" height="36" rx="6"/><rect x="104" y="216" width="44" height="36" rx="6"/><rect x="174" y="216" width="44" height="36" rx="6"/>
      </g>
      <circle cx="196" cy="174" r="30" fill="{GOLD}" stroke="none"/>
{check(196, 174, .6)}
    </g>
    <!-- report stack -->
{doc(640, 230, 200, 250, 5)}
    <path d="M620 260 V500 H820" stroke-opacity=".5"/>
    <path d="M600 290 V520 H800" stroke-opacity=".3"/>
    <!-- clock: deadlines -->
    <g transform="translate(1000,260)">
      <circle r="90" fill="{NAVY_S}"/>
      <path d="M0 -55 V0 L40 28"/>
      <circle r="9" fill="{GOLD}" stroke="none"/>
    </g>
    <!-- checklist -->
    <g transform="translate(930,470)">
{check(0, 0, .55)}      <path d="M40 0 H170" stroke-width="7"/>
{check(0, 55, .55)}      <path d="M40 55 H150" stroke-width="7"/>
{check(0, 110, .55)}      <path d="M40 110 H160" stroke-width="7"/>
    </g>
"""))

# 7. Professional Collaboration & Case Communication — handshake, team, dialogue
write("service-professional-collaboration", scene(W, H, f"""
    <!-- handshake -->
    <g transform="translate(600,360)">
      <path d="M-230 -60 L-120 -140 L-40 -80 L20 -120 L140 -40"/>
      <path d="M-40 -80 L40 -10 C60 10 40 40 10 30 L-30 0"/>
      <path d="M10 30 C30 55 0 80 -30 60 L-70 30"/>
      <path d="M-30 60 C-10 85 -40 110 -70 90 L-110 60"/>
      <path d="M-70 90 C-50 115 -90 135 -120 110 L-200 50 L-230 -60"/>
      <path d="M140 -40 L230 -100 M140 -40 L80 40 L-120 110" stroke-opacity=".9"/>
    </g>
    <!-- team: attorney, court, family, care team -->
{person(150, 140, .42, GOLD_S)}
{person(1050, 140, .42, GOLD_S)}
{person(150, 420, .42, GOLD_S)}
{person(1050, 420, .42, GOLD_S)}
    <!-- dialogue bubbles -->
    <path d="M250 110 H420 Q440 110 440 130 V190 Q440 210 420 210 H300 L270 240 V210 H250 Q230 210 230 190 V130 Q230 110 250 110 Z" fill="{NAVY_S}"/>
    <path d="M270 150 H400 M270 180 H370" stroke-width="6"/>
    <path d="M780 110 H950 Q970 110 970 130 V190 Q970 210 950 210 H930 V240 L900 210 H780 Q760 210 760 190 V130 Q760 110 780 110 Z" fill="{NAVY_S}"/>
    <path d="M800 150 H930 M800 180 H900" stroke-width="6"/>
    <!-- gavel block (court) & briefcase (attorney) small marks -->
    <rect x="110" y="560" width="110" height="70" rx="10" fill="{NAVY_S}"/><path d="M140 560 V540 H190 V560" stroke-width="7"/><path d="M110 595 H220" stroke-width="6"/>
    <path d="M980 630 H1120 M1000 630 V585 H1100 V630 M1050 585 V560" stroke-width="8"/>
"""))

# ----------------------------------------------------------------------------
# PAGE ILLUSTRATIONS
# ----------------------------------------------------------------------------
# About page (16:9): the mission — a person held safe inside a diamond-shield, hands beneath
write("about-mission", scene(W, H, f"""
    <!-- diamond outline -->
    <path d="M600 90 L820 230 L600 560 L380 230 Z" fill="{NAVY_S}" fill-opacity=".7"/>
    <path d="M380 230 H820 M470 90 H730 L820 230 M470 90 L380 230 M470 90 L600 230 L730 90 M600 230 V560" stroke-opacity=".5" stroke-width="5"/>
    <path d="M470 90 H730 L820 230 L600 560 L380 230 Z"/>
{shield(600, 300, .62, GOLD_S, NAVY)}
{person(600, 240, .42)}
{hands_cradle(600, 540, .9)}
    <!-- pillars: dignity, rights, well-being -->
    <g transform="translate(150,330)"><circle r="54" fill="{NAVY_S}"/>{heart(0, 6, .75)}</g>
    <g transform="translate(1050,330)"><circle r="54" fill="{NAVY_S}"/><path d="M-30 -10 L-30 -30 M30 -10 L30 -30 M0 -40 V40 M-30 -30 H30" stroke-width="7"/><path d="M-30 -30 L-48 10 H-12 Z M30 -30 L12 10 H48 Z" stroke-width="6"/><path d="M-30 40 H30" stroke-width="7"/></g>
"""))

# Who We Serve (4:5 portrait): adults across the lifespan + professionals who refer
write("who-we-serve", scene(800, 1000, f"""
    <!-- older adult with cane -->
    <g transform="translate(250,250)">{person(0, 0, .95)}<path d="M95 150 L120 320" stroke-width="12"/><path d="M80 140 Q100 130 110 150" stroke-width="10"/></g>
    <!-- person using wheelchair -->
    <g transform="translate(560,300)">
{person(0, 0, .8)}
      <path d="M-40 136 V215 H60 L90 268" stroke-width="12"/>
      <circle cx="0" cy="268" r="60"/>
      <circle cx="0" cy="268" r="10" fill="{GOLD}" stroke="none"/>
      <circle cx="92" cy="300" r="16"/>
    </g>
    <!-- adult (centre, lower) -->
    <g transform="translate(400,560)">{person(0, 0, 1.0)}</g>
    <!-- professional with briefcase: courts, attorneys, families -->
    <g transform="translate(150,600)">{person(0, 0, .8, GOLD_S)}<path d="M-110 300 H10 M-100 300 V240 H0 V300 M-50 240 V215" stroke-width="9"/></g>
    <g transform="translate(650,600)">{person(0, 0, .8, GOLD_S)}
      <path d="M-20 240 H110 M-10 240 V200 M60 240 V200 M-20 270 H110 M-20 300 H110" stroke-width="7"/>
    </g>
    <!-- umbrella / arc of protection over everyone -->
    <path d="M90 170 Q400 -40 710 170" stroke-width="12" stroke-opacity=".7"/>
    <path d="M90 170 Q140 140 190 170 Q240 140 290 170 Q340 140 390 170 Q440 140 490 170 Q540 140 590 170 Q640 140 690 170" stroke-width="7" stroke-opacity=".5"/>
""", halo=False))

# Contact page (16:9): PA + DE map with a pin at Media, envelope, phone
PA = "M190 140 L420 110 L690 110 L700 150 L720 190 L705 240 L720 290 L700 360 L690 420 L420 450 L190 450 Z"
DE = "M745 300 L790 300 L800 330 L805 380 L820 450 L770 470 L760 420 L750 350 Z"
write("contact-location", scene(W, H, f"""
    <g transform="translate(100,30)">
      <path d="{PA}" fill="{NAVY_S}" fill-opacity=".9"/>
      <path d="{DE}" transform="translate(45,0)" fill="{NAVY_S}" fill-opacity=".9"/>
      <text x="400" y="300" font-family="Georgia,serif" font-size="44" fill="{GOLD_S}" fill-opacity=".55" stroke="none" text-anchor="middle" letter-spacing="6">PENNSYLVANIA</text>
      <text x="835" y="520" font-family="Georgia,serif" font-size="30" fill="{GOLD_S}" fill-opacity=".55" stroke="none" text-anchor="middle" letter-spacing="4">DELAWARE</text>
      <!-- pin: Media, PA -->
      <g transform="translate(660,360)">
        <circle r="60" fill="{GOLD}" fill-opacity=".18" stroke="none"/>
        <path d="M0 40 C-40 -10 -40 -40 0 -70 C40 -40 40 -10 0 40 Z" fill="{GOLD}" stroke="none"/>
        <circle cy="-30" r="12" fill="{NAVY}" stroke="none"/>
      </g>
      <text x="620" y="445" font-family="Lato,Arial,sans-serif" font-size="22" fill="{IVORY}" stroke="none" text-anchor="middle" letter-spacing="3">MEDIA, PA</text>
    </g>
    <!-- envelope -->
    <g transform="translate(130,500)"><rect x="-60" y="-40" width="160" height="110" rx="12" fill="{NAVY_S}"/><path d="M-60 -40 L20 20 L100 -40"/></g>
    <!-- phone -->
    <g transform="translate(1070,520)"><rect x="-40" y="-80" width="80" height="150" rx="16" fill="{NAVY_S}"/><path d="M-14 50 H14" stroke-width="7"/></g>
""", halo=False))

# Footer map (800x520): same geography, compact
write("footer-map", scene(800, 520, f"""
    <g transform="translate(-50,-40) scale(.82)">
      <path d="{PA}" fill="{NAVY_S}"/>
      <path d="{DE}" transform="translate(45,0)" fill="{NAVY_S}" fill-opacity=".9"/>
      <text x="420" y="300" font-family="Georgia,serif" font-size="40" fill="{GOLD_S}" fill-opacity=".55" stroke="none" text-anchor="middle" letter-spacing="5">PENNSYLVANIA</text>
      <text x="770" y="560" font-family="Georgia,serif" font-size="26" fill="{GOLD_S}" fill-opacity=".55" stroke="none" text-anchor="middle" letter-spacing="3">DELAWARE</text>
      <g transform="translate(660,360)">
        <circle r="55" fill="{GOLD}" fill-opacity=".18" stroke="none"/>
        <path d="M0 40 C-40 -10 -40 -40 0 -70 C40 -40 40 -10 0 40 Z" fill="{GOLD}" stroke="none"/>
        <circle cy="-30" r="12" fill="{NAVY}" stroke="none"/>
      </g>
    </g>
    <text x="400" y="495" font-family="Lato,Arial,sans-serif" font-size="20" fill="{IVORY}" stroke="none" text-anchor="middle" letter-spacing="3">600 N JACKSON STREET · MEDIA, PA 19063</text>
""", halo=False))

# ----------------------------------------------------------------------------
# RESOURCE ARTICLE ILLUSTRATIONS (16:9)
# ----------------------------------------------------------------------------
# Standards of Practice — scales of justice on an open rulebook with checks
write("article-standards", scene(W, H, f"""
    <!-- open book -->
    <path d="M250 520 Q425 470 600 520 Q775 470 950 520 V250 Q775 200 600 250 Q425 200 250 250 Z" fill="{NAVY_S}" fill-opacity=".85"/>
    <path d="M600 250 V520"/>
    <path d="M300 300 H520 M300 345 H500 M300 390 H520 M680 300 H900 M680 345 H880 M680 390 H900" stroke-width="6" stroke-opacity=".6"/>
    <!-- scales -->
    <g transform="translate(600,130)">
      <path d="M0 -60 V150" stroke-width="12"/>
      <path d="M-170 -10 H170"/>
      <circle r="14" fill="{GOLD}" stroke="none"/>
      <path d="M-170 -10 L-230 90 H-110 Z M170 -10 L110 90 H230 Z" fill="{NAVY}" />
      <path d="M-230 90 Q-170 130 -110 90 M110 90 Q170 130 230 90" fill="{GOLD}" stroke="none"/>
    </g>
    <!-- checks: standards met -->
    <g transform="translate(360,460)">{check(0, 0, .6)}</g>
    <g transform="translate(840,460)">{check(0, 0, .6)}</g>
"""))

# How to Recognize a Good Guardian — magnifying glass revealing a person with a star badge
write("article-recognize", scene(W, H, f"""
    <!-- candidates (faded) -->
{person(260, 260, .55, "#9aa3b2")}
{person(940, 260, .55, "#9aa3b2")}
    <!-- magnifier -->
    <g transform="translate(600,320)">
      <circle r="170" fill="{NAVY_S}"/>
      <circle r="170" stroke-width="16"/>
      <path d="M120 120 L230 230" stroke-width="34"/>
{person(0, -110, .9)}
      <!-- star badge: the qualities that stand out -->
      <g transform="translate(110,-100)">
        <circle r="46" fill="{GOLD}" stroke="none"/>
        <path d="M0 -26 L8 -8 L28 -6 L13 7 L17 27 L0 17 L-17 27 L-13 7 L-28 -6 L-8 -8 Z" fill="{NAVY}" stroke="none"/>
      </g>
    </g>
    <!-- qualities ticked -->
    <g transform="translate(150,540)">{check(0, 0, .5)}<path d="M34 0 H150" stroke-width="7"/></g>
    <g transform="translate(900,540)">{check(0, 0, .5)}<path d="M34 0 H150" stroke-width="7"/></g>
"""))

# Understanding Guardianship — open book, lightbulb of understanding, key concepts
write("article-understanding", scene(W, H, f"""
    <!-- book -->
    <path d="M250 560 Q425 510 600 560 Q775 510 950 560 V300 Q775 250 600 300 Q425 250 250 300 Z" fill="{NAVY_S}" fill-opacity=".85"/>
    <path d="M600 300 V560"/>
    <path d="M300 350 H520 M300 395 H500 M300 440 H520 M680 350 H900 M680 395 H880 M680 440 H900" stroke-width="6" stroke-opacity=".6"/>
    <!-- lightbulb -->
    <g transform="translate(600,150)">
      <circle r="80" fill="{GOLD}" fill-opacity=".15" stroke="none"/>
      <path d="M-50 -10 A50 50 0 1 1 50 -10 Q50 25 30 45 V70 H-30 V45 Q-50 25 -50 -10 Z" fill="{NAVY_S}"/>
      <path d="M-22 95 H22 M-16 118 H16" stroke-width="8"/>
      <path d="M0 -120 V-150 M-85 -85 L-105 -105 M85 -85 L105 -105 M-120 0 H-150 M120 0 H150" stroke-width="8" stroke-opacity=".7"/>
      <path d="M-14 20 V-10 L0 5 L14 -10 V20" stroke-width="6"/>
    </g>
    <!-- key: legal considerations -->
    <g transform="translate(170,300) rotate(-30)"><circle r="40"/><circle r="12" fill="{GOLD}" stroke="none"/><path d="M40 0 H150 M110 0 V30 M140 0 V36" stroke-width="12"/></g>
    <!-- question mark: making sense of it -->
    <g transform="translate(1020,290)"><circle r="60" fill="{NAVY_S}"/><path d="M-22 -18 A22 22 0 1 1 8 4 Q0 10 0 20" stroke-width="9"/><circle cy="40" r="7" fill="{GOLD_S}" stroke="none"/></g>
"""))

# ----------------------------------------------------------------------------
# COMMITMENT CARD ICONS (square) — one per "What You Can Expect" value
# ----------------------------------------------------------------------------
def icon(name, body):
    write(name, f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" role="img">
  <circle cx="60" cy="60" r="58" fill="{NAVY}"/>
  <circle cx="60" cy="60" r="52" fill="none" stroke="{GOLD}" stroke-opacity=".6" stroke-width="2"/>
  <g fill="none" stroke="{GOLD_S}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" transform="translate(60,60)">
{body}
  </g>
</svg>
""")

icon("value-dignity",  f'    <path d="M0 26 C-30 6 -30 -20 -15 -20 C-7 -20 -2 -15 0 -10 C2 -15 7 -20 15 -20 C30 -20 30 6 0 26 Z" fill="{GOLD}" stroke="none"/>\n    <path d="M-30 20 C-30 34 -16 38 0 38 C16 38 30 34 30 20"/>')
icon("value-rights",   f'    <path d="M0 -34 L28 -22 V0 C28 18 14 30 0 36 C-14 30 -28 18 -28 0 V-22 Z"/>\n    <path d="M-12 2 L-3 11 L14 -8"/>')
icon("value-ethics",   f'    <path d="M0 -32 V30 M-28 -18 H28 M-24 32 H24"/>\n    <path d="M-28 -18 L-40 8 H-16 Z M28 -18 L16 8 H40 Z"/>\n    <circle cy="-32" r="4" fill="{GOLD}" stroke="none"/>')
icon("value-continuity", f'    <circle cx="-22" cy="-16" r="10"/><circle cx="22" cy="-16" r="10"/><circle cx="0" cy="22" r="10"/>\n    <path d="M-14 -10 L-6 14 M14 -10 L6 14 M-12 -16 H12"/>')
icon("value-independence", f'    <circle cy="-22" r="9" fill="{IVORY}" stroke="none"/>\n    <path d="M0 -10 V14 M0 -2 L-20 -14 M0 -2 L20 -14 M0 14 L-14 36 M0 14 L14 36"/>')
icon("value-accountability", f'    <path d="M-30 -14 L-12 -28 L0 -18 L10 -26 L30 -10"/>\n    <path d="M0 -18 L14 -4 C18 0 14 8 8 6 L0 0 M8 6 C12 12 4 18 -2 14 L-10 8 M-2 14 C2 20 -6 26 -12 20 L-30 6 L-30 -14"/>')

print("all done ->", OUT)
