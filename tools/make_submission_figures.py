"""Build submission-grade figure files for the ScholarOne upload.

The 1200 dpi CMYK TIFFs in this repository are the *production* files: that
specification comes from the Author Instructions and is what the publisher
needs if the paper is accepted.  The submission form asks for much less --
"a minimum print resolution of 300 dpi at 8.5 cm width or at least 1000
pixels in width" -- and the production files carry three properties that
make submission systems choke:

  * CMYK with no embedded ICC profile, so a proof generator has no way to
    interpret the ink values;
  * tens of millions of pixels (Figure 3 is 46.3 MP);
  * LZW strips one or two rows tall, so Figure 3 is 4,230 separate strips.

This writes RGB PNGs at 600 dpi-equivalent (half the linear size, so still
double the minimum the form asks for) into figures_for_submission/.  PNG is
one of the form's preferred types and sidesteps the TIFF strip and
photometric issues entirely.

Run from the repository root:  python3 tools/make_submission_figures.py
"""

import os

from PIL import Image

Image.MAX_IMAGE_PIXELS = None

OUT = 'figures_for_submission'
SCALE = 0.5          # 1200 dpi -> 600 dpi equivalent
SOURCE_DPI = 1200
MIN_WIDTH_PX = 1000  # the form's floor


def main():
    os.makedirs(OUT, exist_ok=True)
    srcs = sorted(f for f in os.listdir('.') if f.endswith('.tif'))
    for src in srcs:
        im = Image.open(src)
        w, h = im.size
        nw, nh = max(1, round(w * SCALE)), max(1, round(h * SCALE))
        assert nw >= MIN_WIDTH_PX, f'{src}: {nw}px is below the form floor'

        rgb = im.convert('RGB').resize((nw, nh), Image.LANCZOS)
        dpi = round(SOURCE_DPI * SCALE)
        name = src.replace('_v2.tif', '.png')
        dest = os.path.join(OUT, name)
        rgb.save(dest, 'PNG', dpi=(dpi, dpi), optimize=True)

        kb = os.path.getsize(dest) / 1024
        cm = nw / dpi * 2.54
        print(f'  {name:32s} {nw}x{nh} px  {dpi} dpi  '
              f'{cm:.1f} cm wide  RGB  {kb:.0f} KB')


if __name__ == '__main__':
    main()
