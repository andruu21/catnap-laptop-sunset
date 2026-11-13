#!/usr/bin/env python3
"""Generate the ai-happy-01 entry: a round fluffy cat asleep on a warm glowing laptop,
steam curling from a mug, soft sunset gradient, a tiny heart floating up.
Flat illustration, warm amber/coral/cream palette, 4x supersampled for clean edges."""
from PIL import Image, ImageDraw
import math

S = 4                     # supersample factor
W = H = 1024 * S          # working canvas
OUT = "entry.png"


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

# ---- sky: warm sunset gradient (deep coral -> peach -> cream) ----
top = (255, 138, 101)
mid = (255, 183, 128)
bot = (255, 224, 178)
for y in range(H):
    t = y / H
    if t < 0.55:
        c = lerp(top, mid, t / 0.55)
    else:
        c = lerp(mid, bot, (t - 0.55) / 0.45)
    d.line([(0, y), (W, y)], fill=c)

# ---- a big soft sun low behind the desk ----
sun_c = (W * 0.72, H * 0.34)
sun_r = 150 * S
for r in range(int(sun_r * 1.6), 0, -2):
    t = r / (sun_r * 1.6)
    c = lerp((255, 249, 196), (255, 224, 178), t)
    d.ellipse([sun_c[0] - r, sun_c[1] - r, sun_c[0] + r, sun_c[1] + r], fill=c)

# ---- desk surface ----
desk_top = H * 0.62
d.rectangle([0, desk_top, W, H], fill=(197, 123, 89))          # warm wood
for i in range(6):                                             # wood grain lines
    y = desk_top + (H - desk_top) * (i + 1) / 7
    d.line([(0, y), (W, y)], fill=(180, 105, 75), width=2 * S)

# ---- laptop: open, screen glowing warm, cat lying across the keyboard base ----
# base (keyboard deck seen slightly from the front)
base_l = W * 0.20
base_r = W * 0.68
base_y = desk_top + (H - desk_top) * 0.55
d.rounded_rectangle([base_l, base_y, base_r, base_y + 30 * S], radius=12 * S,
                    fill=(120, 88, 100))
# screen panel: thin frame, tall and warm-glowing, rising from the back of the base
sx0, sx1 = W * 0.23, W * 0.65
sy0, sy1 = base_y - 290 * S, base_y
d.rounded_rectangle([sx0, sy0, sx1, sy1], radius=10 * S, fill=(90, 64, 78))
d.rounded_rectangle([sx0 + 14 * S, sy0 + 14 * S, sx1 - 14 * S, sy1 - 6 * S],
                    radius=8 * S, fill=(255, 214, 130))
# warm glow: subtle light pooling just around the base on the desk
for gr, alpha_c in ((46, (215, 140, 100)), (26, (233, 160, 115)), (10, (248, 180, 130))):
    d.ellipse([base_l - gr * S, base_y - 4 * S, base_r + gr * S, base_y + 62 * S + gr * S],
              fill=alpha_c)

# ---- cat: round fluffy loaf asleep ON the laptop base, in the glow ----
cx, cy = W * 0.44, base_y - 72 * S      # body centre
# tail curling around the front of the body, tip resting on the base
d.arc([cx - 230 * S, cy - 90 * S, cx + 30 * S, cy + 120 * S],
      start=170, end=355, fill=(238, 168, 128), width=24 * S)
d.ellipse([cx - 244 * S, cy + 18 * S, cx - 212 * S, cy + 50 * S], fill=(238, 168, 128))
# body loaf
d.ellipse([cx - 170 * S, cy - 100 * S, cx + 170 * S, cy + 100 * S], fill=(245, 190, 150))
# head, slightly right and up, overlapping the body
hx, hy = cx + 80 * S, cy - 45 * S
d.ellipse([hx - 100 * S, hy - 92 * S, hx + 100 * S, hy + 92 * S], fill=(250, 205, 165))
# ears
d.polygon([(hx - 82 * S, hy - 58 * S), (hx - 44 * S, hy - 126 * S), (hx - 18 * S, hy - 68 * S)],
          fill=(250, 205, 165))
d.polygon([(hx + 82 * S, hy - 58 * S), (hx + 44 * S, hy - 126 * S), (hx + 18 * S, hy - 68 * S)],
          fill=(250, 205, 165))
d.polygon([(hx - 70 * S, hy - 64 * S), (hx - 46 * S, hy - 108 * S), (hx - 31 * S, hy - 72 * S)],
          fill=(250, 150, 140))
d.polygon([(hx + 70 * S, hy - 64 * S), (hx + 46 * S, hy - 108 * S), (hx + 31 * S, hy - 72 * S)],
          fill=(250, 150, 140))
# closed eyes: two happy curves
for ex in (hx - 40 * S, hx + 40 * S):
    d.arc([ex - 16 * S, hy - 24 * S, ex + 16 * S, hy + 4 * S], start=20, end=160,
          fill=(120, 70, 50), width=5 * S)
# tiny nose + smiling mouth
d.ellipse([hx - 7 * S, hy + 10 * S, hx + 7 * S, hy + 22 * S], fill=(230, 110, 100))
d.arc([hx - 14 * S, hy + 16 * S, hx + 2 * S, hy + 32 * S], start=0, end=140,
      fill=(120, 70, 50), width=3 * S)
d.arc([hx - 2 * S, hy + 16 * S, hx + 14 * S, hy + 32 * S], start=40, end=180,
      fill=(120, 70, 50), width=3 * S)
# blush
for bx in (hx - 68 * S, hx + 58 * S):
    d.ellipse([bx - 13 * S, hy + 16 * S, bx + 13 * S, hy + 30 * S], fill=(255, 160, 140))
# fluffy chest tuft (light patch on the body, not stripes)
d.ellipse([cx - 60 * S, cy - 10 * S, cx + 60 * S, cy + 80 * S], fill=(252, 222, 190))

# ---- mug of cocoa beside the laptop ----
mx, my = W * 0.79, base_y - 10 * S
d.rounded_rectangle([mx - 55 * S, my - 110 * S, mx + 55 * S, my + 20 * S], radius=14 * S,
                    fill=(240, 245, 250))
# handle
d.arc([mx + 45 * S, my - 85 * S, mx + 115 * S, my - 15 * S], start=270, end=90,
      fill=(240, 245, 250), width=16 * S)
# cocoa surface
d.ellipse([mx - 44 * S, my - 104 * S, mx + 44 * S, my - 82 * S], fill=(140, 85, 55))
# steam: three wavy lines
for i, sxx in enumerate((-28, 0, 28)):
    pts = []
    for t in range(0, 21):
        ty = t / 20
        px = mx + sxx * S + math.sin(ty * 6 + i) * 12 * S
        py = my - 130 * S - ty * 130 * S
        pts.append((px, py))
    d.line(pts, fill=(255, 250, 240), width=6 * S)

# ---- a tiny heart floating up from the cat ----
def heart(dr, x, y, r, color):
    dr.polygon([(x, y + r), (x - r, y - r * 0.4), (x, y - r * 0.1), (x + r, y - r * 0.4)],
               fill=color)
    dr.ellipse([x - r, y - r * 1.1, x, y - r * 0.1], fill=color)
    dr.ellipse([x, y - r * 1.1, x + r, y - r * 0.1], fill=color)

heart(d, W * 0.58, H * 0.30, 26 * S, (250, 100, 110))
heart(d, W * 0.66, H * 0.235, 14 * S, (255, 130, 140))

img = img.resize((1024, 1024), Image.LANCZOS)
img.save(OUT, optimize=True)
import os
print("saved", OUT, os.path.getsize(OUT), "bytes")
