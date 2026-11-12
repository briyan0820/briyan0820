"""Generate the original animated bear GIF used in the GitHub profile.
Run: pip install Pillow && python scripts/generate_bear.py
"""
from pathlib import Path
from math import sin, pi
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'typing-bear.gif'
S = 2
W, H = 360, 300

def draw_frame(i):
    im = Image.new('RGBA', (W*S, H*S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    def xy(box): return tuple(round(v*S) for v in box)
    def ellipse(box, fill, outline=None, width=1): d.ellipse(xy(box), fill=fill, outline=outline, width=width*S)
    def rect(box, fill, radius=0, outline=None, width=1):
        d.rounded_rectangle(xy(box), radius=radius*S, fill=fill, outline=outline, width=width*S)
    def line(points, fill, width=2): d.line([(round(x*S),round(y*S)) for x,y in points], fill=fill, width=width*S, joint='curve')
    # Comfortable blue armchair
    rect((48,110,277,278), '#3FC4EE', 44, '#167EB8', 4)
    rect((63,126,258,260), '#65D6F6', 34)
    rect((38,182,104,274), '#26A9DD', 24, '#167EB8', 4)
    # Chair shadow and bear body
    ellipse((112,245,263,278), '#249DC9')
    ellipse((112,169,252,269), '#F4B6C5')
    rect((138,199,238,268), '#F6D46A', 20)
    # ears behind head
    ellipse((110,54,155,104), '#EBA2B7', '#9E6479', 3)
    ellipse((227,54,272,104), '#EBA2B7', '#9E6479', 3)
    ellipse((120,65,146,92), '#F8C6D3')
    ellipse((236,65,262,92), '#F8C6D3')
    # Head with gentle bobbing
    bob = round(2*sin(i*2*pi/12))
    ellipse((116,63+bob,269,207+bob), '#F4B6C5', '#A86F82', 3)
    ellipse((152,135+bob,165,146+bob), '#614C59')
    ellipse((220,135+bob,233,146+bob), '#614C59')
    ellipse((181,153+bob,201,164+bob), '#B56E82')
    ellipse((138,155+bob,156,166+bob), '#EF96AC')
    ellipse((237,155+bob,255,166+bob), '#EF96AC')
    # Laptop with pink lid and glowing screen
    rect((220,177,325,234), '#F3A5F5', 8, '#9B63BB', 3)
    rect((226,183,318,226), '#F8C7FC', 5)
    ellipse((267,199,277,209), '#E08AE8')
    line([(206,239),(326,239),(314,251),(214,251)], '#8E5BAA', 7)
    # Animated paws typing in alternating positions
    offset = 4 if i%2 else 0
    ellipse((190,212+offset,222,239+offset), '#F4B6C5', '#A86F82', 2)
    ellipse((227,220-offset,256,244-offset), '#F4B6C5', '#A86F82', 2)
    # Motion lines to show typing
    if i%3 == 0:
        line([(270,170),(274,163)], '#ED8EDC', 3)
        line([(286,169),(292,164)], '#ED8EDC', 3)
    return im

frames = [draw_frame(i) for i in range(12)]
OUT.parent.mkdir(parents=True, exist_ok=True)
frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=110, loop=0, disposal=2, optimize=True)
print(f'Created {OUT}')
