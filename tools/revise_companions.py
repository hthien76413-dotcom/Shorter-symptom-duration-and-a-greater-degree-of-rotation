"""Third-submission revision of the TRIPOD checklist and the cover letter.

Run after tools/revise_manuscript.py, from the repository root.
"""

import sys

from docx import Document

sys.path.insert(0, 'tools')
from docx_edit import renumber_citations, replace

TRIPOD = 'TRIPOD_checklist.docx'
COVER = 'Cover_letter.docx'

# Same old -> new map as the manuscript, restricted to the entries the
# checklist actually cites.
TRIPOD_CITATIONS = [
    ('7-9', '6-8'),      # the three prior degree series
    ('10,11', '9,10'),   # the two imaging series
    ('14,17', '13,16'),  # the two existing preoperative laboratory models
    ('19', '18'),        # Riley
    ('18', '17'),        # Heinze
    ('20', '19'),        # DeLong
    ('21', '20'),        # Pencina
]

TRIPOD_EDITS = [
    # "Supplementary Methods S1–S5" is its own run, so anchor on the run.
    # The supplementary methods document has six sections, not five.
    ('tripod-supplementary-sections',
     'Supplementary Methods S1–S5',
     'Supplementary Methods S1–S6'),
    # Only one of these two series concludes the angle is unhelpful; the
    # Introduction says the other takes the opposite view.  What they have in
    # common is that neither tests the association.
    ('tripod-imaging-series',
     '; the two imaging series concluding the angle is unhelpful',
     '; the two imaging series that comment on the angle without testing it'),
]

COVER_EDITS = [
    # Matches the manuscript: duration shifts the probability of a complete
    # twist, it does not identify one.
    ('cover-identifies-twist',
     'in a child with confirmed volvulus, a history measured in hours '
     'identifies the dangerous twist, and its brevity should raise rather than '
     'lower concern.',
     'in a child with confirmed volvulus, a short history makes the dangerous '
     'twist more likely rather than less, and should raise rather than lower '
     'concern.'),
    ('cover-null-together',
     'the likelihood ratio test, the change in discrimination and the '
     'integrated discrimination improvement were null together (P = 0.818).',
     'the likelihood ratio test, the change in discrimination and the '
     'integrated discrimination improvement all ceased to be significant '
     'together (P = 0.818, on the 17 events that remained).'),
    # Counts recomputed from the revised manuscript.
    ('cover-counts',
     'The manuscript comprises 5,656 words of main text with a 247-word '
     'structured abstract, 23 references, 4 tables and 4 figures,',
     'The manuscript comprises 5,711 words of main text with a 250-word '
     'structured abstract, 21 references, 4 tables and 4 figures,'),
]


def run(path, edits, citations=None):
    print(f'--- {path}')
    doc = Document(path)
    for label, old, new in edits:
        replace(doc, old, new, expect=1, label=label)
        print(f'  ok  {label}')
    if citations is not None:
        renumber_citations(doc, citations)
        print('  ok  citations renumbered')
    doc.save(path)


if __name__ == '__main__':
    run(TRIPOD, TRIPOD_EDITS, TRIPOD_CITATIONS)
    run(COVER, COVER_EDITS)
