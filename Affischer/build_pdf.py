# -*- coding: utf-8 -*-
"""Bygger A3-affisch (stående) för Byathlon – Swisha till Ukraina."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth

SP = sys.argv[1]          # scratchpad dir with logo.png / swish-qr.png
OUT = sys.argv[2]         # output pdf path

# ── Byathlon-palett ──
DGREEN  = HexColor('#25231e')
DGREEN7 = HexColor('#36342b')
CREAM   = HexColor('#efe8e0')
CREAM2  = HexColor('#eae1d7')
TAN3    = HexColor('#dbcbb8')
SHADOW  = HexColor('#d3c9bb')
YELLOW  = HexColor('#ebbd33')
OLIVE   = HexColor('#606c38')
UA_BLUE = HexColor('#0057B7')
UA_YEL  = HexColor('#FFD700')
WHITE   = HexColor('#ffffff')

BOLD = 'Helvetica-Bold'
REG  = 'Helvetica'

W = 297 * mm
H = 420 * mm
c = canvas.Canvas(OUT, pagesize=(W, H))

def yt(y_mm):
    """top-baserad mm -> pdf-punkt (från botten)."""
    return H - y_mm * mm

def band(a_mm, b_mm, color):
    c.setFillColor(color)
    c.rect(0, H - b_mm * mm, W, (b_mm - a_mm) * mm, fill=1, stroke=0)

def centered(text, y_mm, font, size, color):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawCentredString(W / 2, yt(y_mm), text)

def tracked_width(text, font, size, tr):
    return sum(stringWidth(ch, font, size) for ch in text) + tr * (len(text) - 1)

def tracked_centered(text, y_mm, font, size, color, tr):
    w = tracked_width(text, font, size, tr)
    x = W / 2 - w / 2
    y = yt(y_mm)
    c.setFont(font, size)
    c.setFillColor(color)
    for ch in text:
        c.drawString(x, y, ch)
        x += stringWidth(ch, font, size) + tr
    return w

# ══ SIDBAKGRUND ══
c.setFillColor(CREAM)
c.rect(0, 0, W, H, fill=1, stroke=0)

# ══ HEADER ══
band(0, 64, DGREEN)
logo = SP + '/logo.png'
logo_sz = 30 * mm
brand = 'Byathlon'
brand_sz = 32
brand_w = stringWidth(brand, BOLD, brand_sz)
gap = 8 * mm
lockup_w = logo_sz + gap + brand_w
lx = (W - lockup_w) / 2
# logo centrerad vertikalt kring 30mm
c.drawImage(logo, lx, H - 45 * mm, width=logo_sz, height=logo_sz,
            mask='auto', preserveAspectRatio=True, anchor='sw')
# varumärkesnamn
c.setFont(BOLD, brand_sz)
c.setFillColor(CREAM)
c.drawString(lx + logo_sz + gap, yt(29), brand)
# tagline (spärrad)
tag = 'SPRING  ·  GÅ  ·  BADA'
c.setFont(BOLD, 9.5)
c.setFillColor(YELLOW)
tx = lx + logo_sz + gap
tw = tracked_width(tag, BOLD, 9.5, 3.2)
c.saveState()
x = tx
for ch in tag:
    c.drawString(x, yt(40), ch)
    x += stringWidth(ch, BOLD, 9.5) + 3.2
c.restoreState()

# ══ UKRAINA-FLAGGA ══
band(64, 68.5, UA_BLUE)
band(68.5, 73, UA_YEL)

# ══ EYEBROW med sidlinjer ══
eb = 'INSAMLING TILL FÖRMÅN FÖR UKRAINA'
ebw = tracked_centered(eb, 92, BOLD, 12, OLIVE, 3.4)
line_y = yt(91)
gap2 = 6 * mm
line_len = 18 * mm
c.setStrokeColor(TAN3)
c.setLineWidth(1.4)
c.line(W / 2 - ebw / 2 - gap2 - line_len, line_y, W / 2 - ebw / 2 - gap2, line_y)
c.line(W / 2 + ebw / 2 + gap2, line_y, W / 2 + ebw / 2 + gap2 + line_len, line_y)

# ══ RUBRIK (tvåfärgad) ══
p1, p2 = 'Swisha till ', 'Ukraina'
hsz = 50
w1 = stringWidth(p1, BOLD, hsz)
w2 = stringWidth(p2, BOLD, hsz)
hx = (W - (w1 + w2)) / 2
c.setFont(BOLD, hsz)
c.setFillColor(DGREEN)
c.drawString(hx, yt(118), p1)
c.setFillColor(OLIVE)
c.drawString(hx + w1, yt(118), p2)

# ══ INGRESS ══
centered('Skanna QR-koden med Swish-appen och ge ett valfritt belopp.', 134, REG, 14, DGREEN7)
centered('Ditt bidrag går till civila i krigsdrabbade Ukraina.', 141.5, REG, 14, DGREEN7)

# ══ QR-KORT ══
card_w, card_h = 150 * mm, 158 * mm
card_x = (W - card_w) / 2
card_top = 152
card_bottom_pdf = H - (card_top * mm + card_h)
# mjuk skugga
c.setFillColor(SHADOW)
c.roundRect(card_x, card_bottom_pdf - 2.2 * mm, card_w, card_h, 8 * mm, fill=1, stroke=0)
# kort
c.setFillColor(WHITE)
c.setStrokeColor(CREAM2)
c.setLineWidth(1)
c.roundRect(card_x, card_bottom_pdf, card_w, card_h, 8 * mm, fill=1, stroke=1)
# QR
qr = SP + '/swish-qr.png'
qr_sz = 120 * mm
c.drawImage(qr, (W - qr_sz) / 2, H - (164 * mm + qr_sz), width=qr_sz, height=qr_sz,
            mask='auto', preserveAspectRatio=True, anchor='sw')
# bildtext
tracked_centered('SKANNA MED SWISH-APPEN', 300, BOLD, 12.5, DGREEN, 2.6)

# ══ SWISH-NUMMER ══
tracked_centered('SWISH-NUMMER', 322, BOLD, 10.5, OLIVE, 3.0)
centered('123 586 75 44', 340, BOLD, 34, DGREEN)

# pill "Valfritt belopp"
ptext = 'Valfritt belopp'
psz = 13
ptw = stringWidth(ptext, BOLD, psz)
padx = 9 * mm
pw = ptw + 2 * padx
ph = 11 * mm
px = (W - pw) / 2
pill_top = 349
py = H - (pill_top * mm + ph)
c.setFillColor(YELLOW)
c.roundRect(px, py, pw, ph, ph / 2, fill=1, stroke=0)
c.setFillColor(DGREEN)
c.setFont(BOLD, psz)
c.drawCentredString(W / 2, py + ph / 2 - psz * 0.33, ptext)

# ══ FOOTER ══
band(368, 420, DGREEN)
# rad 1 (tvåfärgad, centrerad): "... via Filippus · filippus.se"
centered('Hela ditt bidrag går till civila i krigsdrabbade Ukraina', 384, REG, 14, CREAM)
f2a, f2b, f2c = 'via ', 'Filippus', '  ·  filippus.se'
fsz = 14
wa = stringWidth(f2a, REG, fsz)
wb = stringWidth(f2b, BOLD, fsz)
wc = stringWidth(f2c, REG, fsz)
fx = (W - (wa + wb + wc)) / 2
fy = yt(393)
c.setFont(REG, fsz); c.setFillColor(CREAM); c.drawString(fx, fy, f2a)
c.setFont(BOLD, fsz); c.setFillColor(YELLOW); c.drawString(fx + wa, fy, f2b)
c.setFont(REG, fsz); c.setFillColor(CREAM); c.drawString(fx + wa + wb, fy, f2c)
# meta
tracked_centered('BYATHLON 2026  ·  SIDENSJÖ 25 JULI  ·  BYATHLON.SE',
                 408, BOLD, 10, TAN3, 2.4)

c.showPage()
c.save()
print('OK ->', OUT)
