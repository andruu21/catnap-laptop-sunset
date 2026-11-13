#!/usr/bin/env python3
"""ai-happy-01 entry: copy the generated image to /output/entry.png.

The image (entry.png, beside this file) was drawn by gen_entry.py in this
repository: a round fluffy cat asleep on a warm glowing laptop, a mug of
cocoa steaming beside it, a soft sunset behind and a tiny heart floating up.
"""
import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
print("wrote", os.path.join(out_dir, "entry.png"))
