"""Third-submission revision of the single-file EJPS manuscript.

Run from the repository root:  python3 tools/revise_manuscript.py
"""

import re
import sys

from docx import Document
from docx.oxml.ns import qn

sys.path.insert(0, 'tools')
from docx_edit import (check_ama_separators, paragraphs, renumber_citations,
                       replace, run_text, runs_of, set_run_text, word_count)

PATH = '②_manuscript_EJPS_single.docx'

# ---------------------------------------------------------------- references
# Old list order -> new list order.  Casalino (old 5) is dropped: it is a
# systematic review of segmental versus midgut volvulus and does not support
# the claim it was attached to.  The TRIPOD explanation-and-elaboration paper
# (old 23) is merged into the TRIPOD statement itself (old 22).  Ramsey (old 1)
# is an income-disparities database study and cannot support the opening
# clinical claim, so that claim now cites McCurdie; Ramsey moves to the
# resection clause, which it does support.
NEW_ORDER = [4, 2, 3, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
             18, 19, 20, 21, 22]
DROPPED = {5, 23}

# One entry per superscript citation run, in document order.
CITATIONS = [
    ('1', '1'),            # opening clinical claim -> McCurdie
    ('2', '2'),            # adults -> Coe
    ('3', '3,4'),          # resection consequences -> Hong + Ramsey
    ('4,5', '1'),          # Casalino dropped
    ('4,6', '1,5'),
    ('7', '6'), ('8', '7'), ('9', '8'), ('10', '9'), ('11', '10'),
    ('12,13', '11,12'),
    ('14', '13'), ('15', '14'), ('16', '15'), ('14,17', '13,16'),
    ('18', '17'), ('19', '18'), ('20', '19'), ('21', '20'),
    ('22,23', '21'),       # two TRIPOD 2015 entries merged
    ('14', '13'), ('7,11', '6,10'), ('7', '6'), ('11', '10'),
    ('7-11', '6-10'), ('14', '13'),
]

# ------------------------------------------------------------------- edits
EDITS = [
    # --- Abstract.  Limit is 250 words; the headings are counted, so every
    # addition below is paid for by a trim elsewhere in the same abstract.
    ('abstract-methods',
     ' Retrospective cohort at one center, December 2012–June 2026. From 414 '
     'index operations for intestinal malrotation we defined a population with '
     'acute midgut volvulus: volvulus confirmed at operation, current episode '
     '≤7 days, malrotation not incidental to other surgery. Bowel compromise '
     'was adjudicated from operative notes against a pre-specified manual; '
     'duration came from the chief complaint. Firth penalized logistic '
     'regression was used with bootstrap internal validation.',
     ' Retrospective single-center cohort, December 2012–June 2026. From 414 '
     'index operations for intestinal malrotation we defined an acute midgut '
     'volvulus population: volvulus confirmed at operation, current episode '
     '≤7 days, malrotation not incidental to other surgery. Bowel compromise '
     'was adjudicated from operative notes against a pre-specified manual; '
     'duration from the chief complaint. Firth penalized logistic regression '
     'with bootstrap internal validation.'),

    # "the markers" had no antecedent anywhere in the abstract; and a
    # non-significant result on 17 events is not an absent effect.
    ('abstract-results',
     'Of 287 children, 63 (22.0%) had bowel compromise and 19 (6.6%) necrosis. '
     'Compromise rose monotonically with rotation (0 of 15 below 360° to 3 of 3 '
     'at ≥1080°; P < 0.001)',
     'Of 287 children, 63 (22.0%) had bowel compromise, 19 (6.6%) necrosis. '
     'Compromise rose monotonically with rotation (0/15 below 360° to 3/3 '
     'at ≥1080°; P < 0.001)'),
    ('abstract-results-or',
     'Both were independent: per 90° of rotation OR 1.66',
     'Both were independent: per 90° rotation OR 1.66'),
    ('abstract-results-markers',
     'In 174 children with complete data the markers improved model fit '
     '(likelihood ratio P = 0.005) but changed discrimination little '
     '(ΔAUC +0.017); both were null once same-day specimens were excluded '
     '(P = 0.818).',
     'In 174 children with complete data, C-reactive protein and neutrophil '
     'count improved model fit (likelihood ratio P = 0.005) but changed '
     'discrimination little (ΔAUC +0.017); neither association remained '
     'detectable after excluding same-day specimens (17 events; P = 0.818).'),
    ('abstract-conclusions',
     ' symptom duration are each independently associated with bowel '
     'compromise. A short history should not reassure: it more likely reflects '
     'a complete, strangulating twist than a safe interval. The markers added '
     'nothing demonstrably preoperative.',
     ' duration are each independently associated with bowel compromise. A '
     'short history should not reassure: it more likely reflects a complete, '
     'strangulating twist than a safe interval. Neither marker could be shown '
     'to contribute preoperatively.'),

    # --- Introduction
    ('intro-ct-agreement',
     'its own estimate agreed with the operative finding in under 35.2% of cases',
     'its own estimate agreed with the operative finding in 35.2% of cases'),
    ('intro-one-determinant',
     'although it is the one determinant of ischemic injury the clinician can '
     'assess before opening the abdomen',
     'although it is among the few determinants of ischemic injury the '
     'clinician can assess before opening the abdomen'),

    # --- Methods
    ('methods-audit-fragment',
     'review was concentrated on algorithm-positive records, the direction of '
     'every observed error, although with only 14 positive audit records a '
     'false-negative rate of up to about one in five cannot be excluded',
     'review was therefore concentrated on algorithm-positive records, the '
     'direction in which every observed error lay. With only 14 positive audit '
     'records, however, a false-negative rate of up to about one in five '
     'cannot be excluded'),

    # --- Results.  Table 1 carries no per-indication median interval and no
    # CRP availability row, so both pointers were wrong.
    ('results-table1-pointer',
     'and 3 days where known malrotation was operated non-acutely (Table 1).',
     'and 3 days where known malrotation was operated non-acutely.'),
    ('results-crp-availability-pointer',
     'availability ranged from 45% to 65% across the three duration strata of '
     'the source cohort (Table 1).',
     'availability ranged from 45% to 65% across the three duration strata of '
     'the source cohort (Supplementary Methods S4).'),
    ('results-interaction',
     'The effect of rotation did not depend on duration: the multiplicative '
     'interaction was null (OR 1.02, 0.89–1.17; likelihood ratio P = 0.785)',
     'No modification of the rotation effect by duration was detected: the '
     'multiplicative interaction term was close to null (OR 1.02, 0.89–1.17; '
     'likelihood ratio P = 0.785)'),
    ('results-crp-depended',
     'That CRP association depended entirely on specimens drawn on the day of '
     'surgery.',
     'That CRP association rested on specimens drawn on the day of surgery.'),
    # This sentence is split across runs so that the key statistics keep their
    # own formatting; it is therefore edited one run at a time.
    ('results-null-together-a',
     ', the neutrophil count was null (OR 1.00, 0.82–1.19), and the joint '
     'likelihood ratio test became null (χ² = 0.40 on 2 df, ',
     ', the neutrophil count estimate was centered on the null (OR 1.00, '
     '0.82–1.19), and neither the joint likelihood ratio test (χ² = 0.40 on '
     '2 df, '),
    ('results-null-together-b',
     '), as did the change in discrimination (',
     '), the change in discrimination ('),
    ('results-null-together-c',
     ', DeLong P = 0.324) and the integrated discrimination improvement (',
     ', DeLong P = 0.324) nor the integrated discrimination improvement ('),
    ('results-null-together-d',
     ') (Table S3). In the same-day subset the association persisted',
     ') reached significance; with 17 events that subset is compatible with a '
     'range of effects as well as with none (Table S3). In the same-day subset '
     'the association persisted'),

    ('results-missingness-null',
     'The null result did not depend on the missingness mechanism:',
     'The non-significant result did not depend on the missingness mechanism:'),

    # --- Discussion
    ('discussion-identifies-twist',
     'In a child with confirmed volvulus, a history measured in hours therefore '
     'identifies the dangerous, complete twist, and its brevity should raise '
     'rather than lower concern.',
     'In a child with confirmed volvulus, a short history therefore makes the '
     'complete, strangulating twist more likely rather than less, and should '
     'raise rather than lower concern.'),
    ('discussion-assert-opposite',
     'Two series assert the opposite, that ischemia and necrosis bear no clear '
     'relation to the duration of illness,',
     'Two series state that ischemia and necrosis bear no clear relation to the '
     'duration of illness,'),
    # The recomputed figures for the turns series (0 of 11, P = 0.34) are not
    # reproducible: 0/11 against 5/18 in 29 children gives P = 0.15, and no
    # denominator in that table yields 0.34.  The claim is reduced to what the
    # series is reported to show, and each series is named so the reader can
    # tell which recomputation belongs to which.
    ('discussion-recomputation',
     'Recomputed from their published tables, the three disagree, and not '
     'according to measurement source: two run in the direction reported here, '
     'one significantly and one not (necrosis in 2 of 6 children at 720° or '
     'more against 1 of 15 below, P = 0.18), while the third, also operative, '
     'runs the other way, with no necrosis at all among its eleven children at '
     '720° (P = 0.34). None is informative at that sample size.',
     'Recomputation loosens even the alignment with measurement source. The '
     'sonographic series reported a greater twist in ischemic bowel. Of the two '
     'operative series, the one recording degrees shows the gradient reported '
     'here when its own table is recomputed, though not significantly (necrosis '
     'in 2 of 6 children at 720° or more against 1 of 15 below, P = 0.18); the '
     'one counting turns records no gradient. None is informative at that '
     'sample size.'),
    ('discussion-markers-null',
     'once specimens that cannot be shown to precede the incision are excluded, '
     'the likelihood ratio test, the integrated discrimination improvement and '
     'the change in discrimination are null together. The association is '
     'present but is not demonstrably preoperative.',
     'once specimens that cannot be shown to precede the incision are excluded, '
     'the likelihood ratio test, the integrated discrimination improvement and '
     'the change in discrimination all cease to be significant together. That '
     'subset retains 17 events, so it does not establish that the markers carry '
     'no preoperative information; what it establishes is that none can be '
     'demonstrated here.'),
    ('discussion-add-nothing',
     'They add nothing usable to what the history and the operative finding '
     'already provide.',
     'On these data the markers cannot be shown to add anything usable to what '
     'the history and the operative finding already provide.'),

    # --- Conclusion
    ('conclusion-added-nothing',
     'once those were excluded they added nothing.',
     'once those were excluded, no contribution could be demonstrated in the 17 '
     'events that remained.'),

    # --- Tables and back matter
    ('table3-equation',
     'logit(p) = -1.8020 +0.5056 x rotation -0.5266 x duration -0.0075 x age '
     '+0.7196 x male sex',
     'logit(p) = −1.8020 + 0.5056 × rotation − 0.5266 × duration − 0.0075 × age '
     '+ 0.7196 × male sex'),
    ('table2-mann-whitney', 'Mann-Whitney U test', 'Mann–Whitney U test'),
    ('supplementary-pointer',
     'Supplementary Methods S1–S5 and Supplementary Tables S1–S4',
     'Supplementary Methods S1–S6 and Supplementary Tables S1–S4'),
]


def reorder_references(doc):
    """Drop the two deleted entries, reorder the rest, rewrite the numbers."""
    ps = paragraphs(doc)
    texts = [''.join(run_text(r) for r in runs_of(p)) for p in ps]
    # Scope to the References section: the numbered criteria list in Methods
    # also starts its paragraphs with "1. ", "2. ", "3. ".
    start = texts.index('References')
    end = texts.index('Figure captions')
    refs = [p for p, t in zip(ps[start:end], texts[start:end])
            if re.match(r'^\d+\.\s', t)]
    if len(refs) != 23:
        raise AssertionError(f'expected 23 reference paragraphs, found {len(refs)}')

    by_old = {}
    for p in refs:
        n = int(re.match(r'^(\d+)\.', ''.join(run_text(r) for r in runs_of(p))).group(1))
        by_old[n] = p

    parent = refs[0].getparent()
    anchor = refs[0].getprevious()
    for p in refs:
        parent.remove(p)

    for new_no, old_no in enumerate(NEW_ORDER, start=1):
        p = by_old[old_no]
        first = runs_of(p)[0]
        text = run_text(first)
        set_run_text(first, re.sub(r'^\d+\.', f'{new_no}.', text, count=1))
        if anchor is None:
            parent.insert(0, p)
        else:
            anchor.addnext(p)
        anchor = p

    for old_no in sorted(DROPPED):
        assert old_no not in NEW_ORDER
    return len(NEW_ORDER)


def abstract_words(doc):
    ps = paragraphs(doc)
    texts = [''.join(run_text(r) for r in runs_of(p)) for p in ps]
    start = next(i for i, t in enumerate(texts) if t.startswith('Introduction '))
    return sum(word_count(t) for t in texts[start:start + 4])


def main_text_words(doc):
    ps = paragraphs(doc)
    texts = [''.join(run_text(r) for r in runs_of(p)) for p in ps]
    start = texts.index('Introduction')
    end = next(i for i, t in enumerate(texts) if t == 'Acknowledgments')
    heads = {'Introduction', 'Materials and methods', 'Results', 'Discussion',
             'Conclusion'}
    return sum(word_count(t) for i, t in enumerate(texts[start:end], start)
               if t not in heads and word_count(t) > 6)


def main():
    doc = Document(PATH)
    for label, old, new in EDITS:
        replace(doc, old, new, expect=1, label=label)
        print(f'  ok  {label}')
    renumber_citations(doc, CITATIONS)
    print('  ok  citations renumbered')
    n = reorder_references(doc)
    print(f'  ok  references reordered -> {n} entries')

    bad = check_ama_separators(doc)
    if bad:
        raise AssertionError(f'AMA separator violations: {bad}')
    print('  ok  AMA separators')

    doc.save(PATH)
    doc = Document(PATH)
    print(f'\nabstract words (incl. headings): {abstract_words(doc)}  (limit 250)')
    print(f'main text words: {main_text_words(doc)}')


if __name__ == '__main__':
    main()
