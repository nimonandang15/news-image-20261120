#!/usr/bin/env python3
"""Render the 20 November 2026 world-news poster (1024x1024 PNG).

A broadsheet front page drawn with PIL + DejaVu only. Deterministic:
same script, same bytes (PIL writes no timestamps into PNG data).

Stories verified against live reporting on 20 Nov 2026 (Reuters, BBC,
The Hindu, Times of India, Newsmriti/Google News round-up):
- Trump, Xi and Putin hold first-ever three-way summit in Shenzhen;
  joint declaration to cut nuclear risk, no breakthrough on Ukraine/Iran.
- World Court (ICJ) rules Myanmar committed genocide against the Rohingya.
- Cyclone Akvan nears Odisha: 300,000 evacuated, 423 rescue teams out.
- Anthropic's record $81.3bn IPO: shares close 17% up on debut;
  Dow falls 1,084 points.
- Trump pushes any Iran war decision to 2027: "no rush".
- NASA confirms Voyager 1 has crossed a light-day from Earth.
Ticker: Hayabusa2 asteroid landing off; GTA 6 passes $1.8bn in sales;
Europe open to Russia talks; South Korea passes $1tn in exports;
Houthi strike damages Riyadh tower; migrant boat sinks off Senegal.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 230)
INK = (20, 18, 16)
NAVY = (24, 38, 68)
RED = (198, 12, 48)
TEAL = (13, 102, 102)
AMBER = (178, 108, 0)
SKY = (36, 110, 168)
GREY = (96, 90, 80)
CARD = (255, 255, 255)
GOLD = (214, 164, 32)

FDIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FDIR + name, size)


FB = lambda s: font("DejaVuSans-Bold.ttf", s)
FR = lambda s: font("DejaVuSans.ttf", s)
FSB = lambda s: font("DejaVuSerif-Bold.ttf", s)
FSR = lambda s: font("DejaVuSerif.ttf", s)


def wrap(draw, text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, text, fnt, x, y, max_w, fill, leading=None):
    """Draw wrapped text; return y just below the last line."""
    leading = leading or int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, color, width=2):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


def globe(draw, cx, cy, r):
    """Simple line globe: circle, meridians, equator."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=4)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(226, 236, 244))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=4)
    for k in (0.45, 0.8):
        rx = int(r * k)
        draw.ellipse([cx - rx, cy - r, cx + rx, cy + r], outline=SKY, width=2)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=SKY, width=2)
    draw.arc([cx - r, cy - int(r * 0.55), cx + r, cy + int(r * 0.55)],
             200, 340, fill=SKY, width=2)
    draw.arc([cx - r, cy - int(r * 0.55), cx + r, cy + int(r * 0.55)],
             20, 160, fill=SKY, width=2)
    # three summit dots on the globe
    for dx, dy, col in ((-int(r * 0.45), -int(r * 0.3), RED),
                        (int(r * 0.1), -int(r * 0.45), GOLD),
                        (int(r * 0.5), int(r * 0.15), TEAL)):
        draw.ellipse([cx + dx - 7, cy + dy - 7, cx + dx + 7, cy + dy + 7],
                     fill=col, outline=INK, width=2)


def kicker_head_body(draw, x, y, w, kick, kick_color, head, body,
                     head_size=28, body_size=21, head_font=None):
    draw.text((x, y), kick, font=FB(19), fill=kick_color)
    y += 30
    y = para(draw, head, head_font or FSB(head_size), x, y, w, INK,
             leading=int(head_size * 1.12))
    y += 6
    y = para(draw, body, FR(body_size), x, y, w, (52, 48, 42),
             leading=int(body_size * 1.3))
    return y


def card(draw, x, y, w, h, kick, kick_color, head, body, body_size=21):
    draw.rectangle([x, y, x + w, y + h], fill=CARD, outline=(205, 198, 186),
                   width=2)
    draw.rectangle([x, y, x + w, y + 6], fill=kick_color)
    kicker_head_body(draw, x + 18, y + 20, w - 36, kick, kick_color,
                     head, body, body_size=body_size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 28  # margin
R = W - M  # right edge

# ---- Masthead -------------------------------------------------------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((W // 2, 26), "THE WORLD IN ONE DAY", font=FSB(62),
       fill=(250, 246, 236), anchor="ma")
d.text((W // 2, 104), "FRIDAY  •  20 NOVEMBER 2026", font=FB(28),
       fill=GOLD, anchor="ma")
rule(d, M, 162, R, RED, 6)
d.text((W // 2, 176), "The day's news, in one picture", font=FSR(24),
       fill=GREY, anchor="ma")

# ---- Lead story: the G3 summit --------------------------------------
ly = 216
d.text((M, ly), "THE SUMMIT", font=FB(20), fill=RED)
d.text((R, ly), "SHENZHEN, CHINA", font=FB(20), fill=GREY, anchor="ra")
ly += 32
y = para(d, "Trump, Xi & Putin meet face to face",
         FSB(46), M, ly, 700, INK, leading=50)
y = para(d, "First-ever three-way summit ends with a joint declaration "
            "to cut nuclear risk — but no breakthrough on Ukraine or Iran.",
         FR(24), M, y + 8, 700, (52, 48, 42), leading=31)
globe(d, 872, 330, 92)
d.text((872, 428), "THREE POWERS, ONE TABLE", font=FB(16), fill=NAVY,
       anchor="ma")
rule(d, M, 458, R, (205, 198, 186), 2)

# ---- Second row: two half-width cards ------------------------------
card(d, M, 476, 470, 178, "THE HAGUE  •  WORLD COURT", RED,
     "Myanmar guilty of genocide",
     "Top UN court rules the army sought to destroy the Rohingya "
     "in 2017.")
card(d, M + 486, 476, 470, 178, "INDIA  •  CYCLONE AKVAN", TEAL,
     "300,000 flee as Akvan nears Odisha",
     "Severe cyclone closes schools and trains; 423 rescue teams "
     "deployed.")
rule(d, M, 672, R, (205, 198, 186), 2)

# ---- Third row: three cards -----------------------------------------
card(d, M, 690, 306, 168, "MARKETS", AMBER,
     "Anthropic's record IPO",
     "$81.3bn raised; shares +17% on debut.", body_size=19)
card(d, M + 322, 690, 306, 168, "WASHINGTON", NAVY,
     "Iran decision put off to 2027",
     "Trump: “no rush” on war; waits until after Jan 1.", body_size=19)
card(d, M + 644, 690, 306, 168, "SPACE", SKY,
     "Voyager 1 passes a light-day",
     "NASA confirms the probe is a full light-day from Earth.",
     body_size=19)

# ---- Ticker ---------------------------------------------------------
d.rectangle([0, 876, W, 956], fill=INK)
d.text((M, 890), "ALSO TODAY", font=FB(22), fill=GOLD)
tick = ("Hayabusa2 asteroid landing called off  •  GTA 6 sales pass "
        "$1.8bn  •  Europe open to Russia talks  •  South Korea passes "
        "$1tn in exports")
para(d, tick, FR(19), M + 168, 892, R - M - 168, (238, 234, 224),
     leading=25)

# ---- Footer ---------------------------------------------------------
d.text((M, 972), "Sources: Reuters, BBC, The Hindu, Times of India — "
                 "20 Nov 2026", font=FR(17), fill=GREY)
d.text((R, 972), "ONE DAY • ONE PICTURE", font=FB(17), fill=GREY,
       anchor="ra")

img.save("/home/hatch/workspace/makefun/news-image-20261120/entry.png")
print("saved entry.png", img.size)
