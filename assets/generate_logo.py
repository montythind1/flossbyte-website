"""Generate FlossByte logo variants."""
from PIL import Image, ImageDraw, ImageFont
import os

DIR = os.path.dirname(os.path.abspath(__file__))

# --- Config ---
NAVY = (10, 22, 40)            # #0A1628
WHITE = (255, 255, 255)
TEAL = (0, 191, 165)           # #00BFA5

# --- Load icon ---
icon_orig = Image.open(os.path.join(DIR, "logo-icon.png")).convert("RGBA")

# --- Font ---
font = ImageFont.load_default()
for font_name in ["arialbd.ttf", "calibrib.ttf", "segoeui.ttf", "arial.ttf"]:
    try:
        font = ImageFont.truetype(font_name, 140)
        break
    except OSError:
        continue

# =============================================
# 1. ICON-ONLY version (for LinkedIn company logo)
#    Square, icon fills the space — won't get cut off
# =============================================
ICON_SIZE = 800
ICON_PAD = 60
icon_h = ICON_SIZE - ICON_PAD * 2
icon_scale = icon_h / icon_orig.height
icon_resized = icon_orig.resize((int(icon_orig.width * icon_scale), icon_h), Image.LANCZOS)

for fname, bg in [("flossbyte-icon-dark.png", NAVY + (255,)), ("flossbyte-icon-light.png", (0,0,0,0)), ("flossbyte-icon-white.png", WHITE + (255,))]:
    canvas = Image.new("RGBA", (ICON_SIZE, ICON_SIZE), bg)
    ix = (ICON_SIZE - icon_resized.width) // 2
    iy = (ICON_SIZE - icon_resized.height) // 2
    canvas.paste(icon_resized, (ix, iy), icon_resized)
    canvas.save(os.path.join(DIR, fname), "PNG")
    print(f"Saved: {fname} ({ICON_SIZE}x{ICON_SIZE}px)")

# =============================================
# 2. FULL LOGO version (icon + text, for business cards, etc.)
# =============================================
FULL_ICON_H = 480
TEXT_SIZE = 140
GAP = 50
PADDING = 80

full_scale = FULL_ICON_H / icon_orig.height
icon_full = icon_orig.resize((int(icon_orig.width * full_scale), FULL_ICON_H), Image.LANCZOS)

tmp = Image.new("RGBA", (1, 1))
tmp_draw = ImageDraw.Draw(tmp)
font_full = ImageFont.load_default()
for font_name in ["arialbd.ttf", "calibrib.ttf", "segoeui.ttf", "arial.ttf"]:
    try:
        font_full = ImageFont.truetype(font_name, TEXT_SIZE)
        break
    except OSError:
        continue

floss_bbox = tmp_draw.textbbox((0, 0), "Floss", font=font_full)
byte_bbox = tmp_draw.textbbox((0, 0), "Byte", font=font_full)
floss_w = floss_bbox[2] - floss_bbox[0]
byte_w = byte_bbox[2] - byte_bbox[0]
text_h = floss_bbox[3] - floss_bbox[1]
total_text_w = floss_w + byte_w

content_w = max(icon_full.width, total_text_w)
content_h = FULL_ICON_H + GAP + text_h
CW = content_w + PADDING * 2
CH = content_h + PADDING * 2

versions = {
    "flossbyte-logo-dark.png":  {"bg": NAVY + (255,),      "floss_color": WHITE, "byte_color": TEAL},
    "flossbyte-logo-light.png": {"bg": (0, 0, 0, 0),       "floss_color": NAVY,  "byte_color": TEAL},
    "flossbyte-logo-white.png": {"bg": WHITE + (255,),      "floss_color": NAVY,  "byte_color": TEAL},
}

for filename, cfg in versions.items():
    canvas = Image.new("RGBA", (CW, CH), cfg["bg"])
    draw = ImageDraw.Draw(canvas)
    icon_x = (CW - icon_full.width) // 2
    canvas.paste(icon_full, (icon_x, PADDING), icon_full)
    text_x = (CW - total_text_w) // 2
    text_y = PADDING + FULL_ICON_H + GAP
    draw.text((text_x, text_y), "Floss", fill=cfg["floss_color"], font=font_full)
    draw.text((text_x + floss_w, text_y), "Byte", fill=cfg["byte_color"], font=font_full)
    canvas.save(os.path.join(DIR, filename), "PNG")
    print(f"Saved: {filename} ({CW}x{CH}px)")
