"""Generate REVISIONS_3rd_submission.md from the revision scripts themselves,
so the change list cannot drift from the edits that were actually applied.

Run from the repository root:  python3 tools/make_changelog.py
"""

import sys

sys.path.insert(0, 'tools')
import revise_companions as C
import revise_manuscript as M

OUT = 'REVISIONS_3rd_submission.md'

HEADER = """# 第 3 投改动逐条对照（2026-09-18）

> 本文件不随稿提交。

本轮直接改了交付 docx，因为本仓库没有 `.md` 源文件。**在本机重跑
`build_ejps_package.py` 之前，先把下面每一条搬回项目根目录对应的 `.md`
源文件**，否则重新生成的 docx 会把这一轮改动全部覆盖掉。

每条给出替换前 / 替换后的完整原文，可直接在 `.md` 里做精确查找替换。
改动脚本在 `tools/`，可重跑，每条都断言命中数为 1。

"""

FOOTER = """
## 引用编号映射（旧 → 新）

| 旧 | 新 | 文献 |
|---|---|---|
| 4 | 1 | McCurdie — Ultrasound for infantile midgut malrotation |
| 2 | 2 | Coe — Small bowel volvulus in adults |
| 3 | 3 | Hong — Ultrashort bowel syndrome |
| 1 | 4 | Ramsey — Income disparities |
| 6 | 5 | Schiess — Focused abdominal ultrasound |
| 7 | 6 | Rhim — Clinical study of midgut volvulus |
| 8 | 7 | Zhang W — Sonography in neonates |
| 9 | 8 | Hosokawa — Ultrasound findings predict ischemia |
| 10 | 9 | Li T — Whirl sign |
| 11 | 10 | Zhang HR — Colour Doppler |
| 12 | 11 | Lou YL — Ultrasonography in malrotation |
| 13 | 12 | Yang X — Multicenter retrospective study |
| 14 | 13 | Guan — Nomogram |
| 15 | 14 | Rajab — CRP isoforms |
| 16 | 15 | Keeley — Predictors of ischemic bowel |
| 17 | 16 | Tseng — Twenty years' experience |
| 18 | 17 | Heinze — Firth penalization |
| 19 | 18 | Riley — Minimum sample size |
| 20 | 19 | DeLong |
| 21 | 20 | Pencina — IDI |
| 22 | 21 | Collins — TRIPOD statement |
| **5** | **删除** | Casalino — Neonatal intestinal segmental volvulus |
| **23** | **并入 21** | Moons — TRIPOD explanation and elaboration |

删除与改引的理由：

- **Casalino**（旧 5）挂在「the severity of what will be found at operation is
  difficult to anticipate」这句上。该文是新生儿**节段性**扭转与中肠扭转的对照
  系统综述，讲的是两类扭转之间的差别，不是中肠扭转内部严重程度可否预判，撑不起
  这句。cover letter 的「Why this journal」里仍然提它（那里只说贵刊发过这类
  比较研究，属实），故未动。
- **Ramsey**（旧 1）挂在开篇「Midgut volvulus is a surgical emergency of infancy
  in which the entire midgut may rapidly become ischemic」上。该文是用 Nationwide
  Readmissions Database 做的收入差距研究，**且明确排除新生儿**，用来支持一句关于
  婴儿期的临床断言并不合适。开篇改引 McCurdie（其摘要原文：midgut malrotation
  with volvulus "is a surgical emergency with potentially devastating outcomes"，
  "most frequently with bilious vomiting in the first days–weeks of life"），
  Ramsey 移到它确实支持的切除／造口那一句（该研究报告 14% 需要肠切除和／或造口）。
- **TRIPOD**：正文清单是 2015 版 22 项，故并成 Collins 2015 那一条。若要改引
  TRIPOD+AI，清单需按 27 项重做，见 README 待办 7。

## 未改动但需要作者裁决的

1. **Rhim 旋转度数表**（README 待办 6）：原句的 P = 0.34 与它自己给的分母算不出来，
   本轮已把该句降级为不给分母和 P 值的定性表述。需对照韩文原文再定。
2. **正文篇幅** 5,711 词，排版后约 11–12 页，贴着须知的上限。要不要再瘦身
   500–800 词是作者的取舍，本轮没有动内容。
3. **一次要结局效应量表**与**选择偏倚交互检验**：需要冻结分析集和分析脚本，
   两者都不在本仓库里。
"""


def block(title, edits):
    out = [f'\n## {title}\n']
    for i, (label, old, new) in enumerate(edits, 1):
        out.append(f'### {i}. `{label}`\n')
        out.append('替换前：\n\n```\n' + old + '\n```\n')
        out.append('替换后：\n\n```\n' + new + '\n```\n')
    return '\n'.join(out)


def citations(title, mapping):
    rows = [f'\n## {title}\n',
            '按文档顺序逐个上标引用重写：\n',
            '| # | 替换前 | 替换后 |', '|---|---|---|']
    for i, (old, new) in enumerate(mapping, 1):
        mark = '' if old != new else '（不变）'
        rows.append(f'| {i} | `{old}` | `{new}` {mark}|')
    return '\n'.join(rows) + '\n'


def main():
    parts = [HEADER,
             block('手稿正文 `②_manuscript_EJPS_single.docx`', M.EDITS),
             citations('手稿上标引用重编号', M.CITATIONS),
             block('TRIPOD 清单 `TRIPOD_checklist.docx`', C.TRIPOD_EDITS),
             citations('TRIPOD 清单上标引用重编号', C.TRIPOD_CITATIONS),
             block('Cover letter `Cover_letter.docx`', C.COVER_EDITS),
             FOOTER]
    with open(OUT, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(parts))
    n = sum(len(x) for x in (M.EDITS, C.TRIPOD_EDITS, C.COVER_EDITS))
    print(f'wrote {OUT}: {n} text edits + '
          f'{len(M.CITATIONS) + len(C.TRIPOD_CITATIONS)} citation rewrites')


if __name__ == '__main__':
    main()
