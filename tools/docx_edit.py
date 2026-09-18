"""Shared helpers for the third-submission revision scripts.

The delivery .docx files are normally regenerated from the .md sources by
build_ejps_package.py.  Those sources are not in this repository, so these
scripts edit the .docx in place and record every change in
REVISIONS_3rd_submission.md so the same edits can be ported back to the .md.

Every edit asserts its expected hit count, so a silently-missed anchor is a
hard failure rather than a quiet no-op.
"""

import re

from docx import Document
from docx.oxml.ns import qn


def paragraphs(doc):
    """Every w:p in the document body, including those inside tables."""
    return list(doc.element.body.iter(qn('w:p')))


def runs_of(p):
    return list(p.iter(qn('w:r')))


def run_text(r):
    return ''.join(t.text or '' for t in r.iter(qn('w:t')))


def set_run_text(r, text):
    ts = list(r.iter(qn('w:t')))
    if not ts:
        raise ValueError('run has no w:t')
    ts[0].text = text
    ts[0].set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    for extra in ts[1:]:
        extra.text = ''


def is_superscript(r):
    rpr = r.find(qn('w:rPr'))
    if rpr is None:
        return False
    va = rpr.find(qn('w:vertAlign'))
    return va is not None and va.get(qn('w:val')) == 'superscript'


def replace(doc, old, new, expect=1, label=''):
    """Replace `old` with `new` inside single runs. Asserts the hit count."""
    hits = 0
    for p in paragraphs(doc):
        for r in runs_of(p):
            t = run_text(r)
            if old in t:
                hits += t.count(old)
                set_run_text(r, t.replace(old, new))
    if hits != expect:
        raise AssertionError(
            f'{label or old[:60]!r}: expected {expect} hit(s), found {hits}')
    return hits


def renumber_citations(doc, mapping):
    """Rewrite superscript citation runs in document order.

    `mapping` is a list of (old, new) pairs, one per superscript run.
    """
    sups = [r for p in paragraphs(doc) for r in runs_of(p) if is_superscript(r)]
    if len(sups) != len(mapping):
        raise AssertionError(
            f'expected {len(mapping)} superscript runs, found {len(sups)}: '
            f'{[run_text(r) for r in sups]}')
    for i, (r, (old, new)) in enumerate(zip(sups, mapping)):
        actual = run_text(r)
        if actual != old:
            raise AssertionError(
                f'superscript #{i}: expected {old!r}, found {actual!r}')
        set_run_text(r, new)


def check_ama_separators(doc):
    """AMA: two consecutive numbers take a comma; a hyphen range needs 3+."""
    bad = []
    for p in paragraphs(doc):
        for r in runs_of(p):
            if not is_superscript(r):
                continue
            t = run_text(r)
            for lo, hi in re.findall(r'(\d+)-(\d+)', t):
                if int(hi) - int(lo) < 2:
                    bad.append(t)
    return bad


def word_count(s):
    return len([w for w in re.split(r'\s+', s.strip()) if w])
