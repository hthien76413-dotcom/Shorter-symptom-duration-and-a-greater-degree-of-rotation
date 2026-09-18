"""EJPS formatting compliance fixes found in the pre-submission check.

The author instructions require the whole manuscript -- title page, abstract,
keywords, text, references, figure captions and tables -- to be double-spaced,
12-point, with 1-inch margins.  The package was built with 1.25-inch left and
right margins.  Also fixes one British spelling the American-English pass
missed, and makes the body section heading match the prescribed abstract
subheading.

Run from the repository root:  python3 tools/fix_format.py
"""

import sys

from docx import Document
from docx.shared import Inches

sys.path.insert(0, 'tools')
from docx_edit import replace

DOCS = ['②_manuscript_EJPS_single.docx',
        '②_Supplementary_Methods.docx',
        '②_Tables_supplementary_v2.docx']


def set_margins(path, inches=1.0):
    doc = Document(path)
    changed = []
    for i, sec in enumerate(doc.sections):
        for side in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
            before = getattr(sec, side).inches
            if abs(before - inches) > 0.001:
                setattr(sec, side, Inches(inches))
                changed.append(f'section {i} {side} {before:.2f}" -> {inches:.2f}"')
    doc.save(path)
    return changed


def main():
    for path in DOCS:
        for line in set_margins(path):
            print(f'  ok  {path}: {line}')

    doc = Document(DOCS[0])
    # American English: "per cent" is British; the rest of the manuscript uses
    # "percent"-equivalent figures or the % sign.
    replace(doc, 'Forty-two per cent of outcomes',
            'Forty-two percent of outcomes', expect=1, label='per cent')
    print('  ok  per cent -> percent')
    # The prescribed abstract subheading is "Materials and Methods"; the body
    # heading read "Materials and methods".
    replace(doc, 'Materials and methods', 'Materials and Methods',
            expect=1, label='section heading case')
    print('  ok  section heading capitalization')
    doc.save(DOCS[0])


if __name__ == '__main__':
    main()
