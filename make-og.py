#!/usr/bin/env python3
"""Generate a brand-consistent 1200x630 og:image for SurnovLifeManager (zhizn-site)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
# Brand tokens from the site's CSS
BG_TOP = (29, 29, 31)        # #1d1d1f
BG_BOTTOM = (20, 20, 22)
ACCENT = (110, 168, 255)     # #6ea8ff
TEXT = (245, 245, 247)       # #f5f5f7
MUTED = (161, 161, 166)      # #a1a1a6
CARD_BORDER = (134, 134, 139)

img = Image.new("RGB", (W, H), BG_TOP)
d = ImageDraw.Draw(img)

# Vertical gradient
for y in range(H):
    t = y / H
    r = int(BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * t)
    g = int(BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * t)
    b = int(BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))

def font(path, size):
    return ImageFont.truetype(path, size)

# Fonts
sans = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
sans_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# App mark: a rounded square with a checkmark (tasks/habits/money -> calm)
mark_size = 120
mx, my = 90, 90
d.rounded_rectangle([mx, my, mx + mark_size, my + mark_size], radius=28, fill=ACCENT)
# checkmark
d.line([(mx + 30, my + 62), (mx + 52, my + 84)], fill=BG_TOP, width=12)
d.line([(mx + 52, my + 84), (mx + 92, my + 36)], fill=BG_TOP, width=12)

# Title
d.text((90, 250), "SurnovLifeManager", font=font(sans_bold, 64), fill=TEXT)
d.text((90, 330), "\u00ab\u0416\u0438\u0437\u043d\u044c\u00bb \u2014 Tasks, habits & money in one calm app.",
       font=font(sans, 30), fill=MUTED)

# Feature pills
pills = ["Tasks", "Habits", "Money"]
px = 90
for p in pills:
    w = d.textlength(p, font=font(sans, 26)) + 40
    d.rounded_rectangle([px, 420, px + w, 470], radius=25, outline=CARD_BORDER, width=2)
    d.text((px + 20, 428), p, font=font(sans, 26), fill=TEXT)
    px += w + 20

# Footer URL
d.text((90, 540), "fallen911.github.io/zhizn-site", font=font(sans, 24), fill=MUTED)

img.save("og-image.png", "PNG")
print("saved og-image.png", img.size)
