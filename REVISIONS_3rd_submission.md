# 第 3 投改动逐条对照（2026-09-18）

> 本文件不随稿提交。

本轮直接改了交付 docx，因为本仓库没有 `.md` 源文件。**在本机重跑
`build_ejps_package.py` 之前，先把下面每一条搬回项目根目录对应的 `.md`
源文件**，否则重新生成的 docx 会把这一轮改动全部覆盖掉。

每条给出替换前 / 替换后的完整原文，可直接在 `.md` 里做精确查找替换。
改动脚本在 `tools/`，可重跑，每条都断言命中数为 1。



## 手稿正文 `②_manuscript_EJPS_single.docx`

### 1. `abstract-methods`

替换前：

```
 Retrospective cohort at one center, December 2012–June 2026. From 414 index operations for intestinal malrotation we defined a population with acute midgut volvulus: volvulus confirmed at operation, current episode ≤7 days, malrotation not incidental to other surgery. Bowel compromise was adjudicated from operative notes against a pre-specified manual; duration came from the chief complaint. Firth penalized logistic regression was used with bootstrap internal validation.
```

替换后：

```
 Retrospective single-center cohort, December 2012–June 2026. From 414 index operations for intestinal malrotation we defined an acute midgut volvulus population: volvulus confirmed at operation, current episode ≤7 days, malrotation not incidental to other surgery. Bowel compromise was adjudicated from operative notes against a pre-specified manual; duration from the chief complaint. Firth penalized logistic regression with bootstrap internal validation.
```

### 2. `abstract-results`

替换前：

```
Of 287 children, 63 (22.0%) had bowel compromise and 19 (6.6%) necrosis. Compromise rose monotonically with rotation (0 of 15 below 360° to 3 of 3 at ≥1080°; P < 0.001)
```

替换后：

```
Of 287 children, 63 (22.0%) had bowel compromise, 19 (6.6%) necrosis. Compromise rose monotonically with rotation (0/15 below 360° to 3/3 at ≥1080°; P < 0.001)
```

### 3. `abstract-results-or`

替换前：

```
Both were independent: per 90° of rotation OR 1.66
```

替换后：

```
Both were independent: per 90° rotation OR 1.66
```

### 4. `abstract-results-markers`

替换前：

```
In 174 children with complete data the markers improved model fit (likelihood ratio P = 0.005) but changed discrimination little (ΔAUC +0.017); both were null once same-day specimens were excluded (P = 0.818).
```

替换后：

```
In 174 children with complete data, C-reactive protein and neutrophil count improved model fit (likelihood ratio P = 0.005) but changed discrimination little (ΔAUC +0.017); neither association remained detectable after excluding same-day specimens (17 events; P = 0.818).
```

### 5. `abstract-conclusions`

替换前：

```
 symptom duration are each independently associated with bowel compromise. A short history should not reassure: it more likely reflects a complete, strangulating twist than a safe interval. The markers added nothing demonstrably preoperative.
```

替换后：

```
 duration are each independently associated with bowel compromise. A short history should not reassure: it more likely reflects a complete, strangulating twist than a safe interval. Neither marker could be shown to contribute preoperatively.
```

### 6. `intro-ct-agreement`

替换前：

```
its own estimate agreed with the operative finding in under 35.2% of cases
```

替换后：

```
its own estimate agreed with the operative finding in 35.2% of cases
```

### 7. `intro-one-determinant`

替换前：

```
although it is the one determinant of ischemic injury the clinician can assess before opening the abdomen
```

替换后：

```
although it is among the few determinants of ischemic injury the clinician can assess before opening the abdomen
```

### 8. `methods-audit-fragment`

替换前：

```
review was concentrated on algorithm-positive records, the direction of every observed error, although with only 14 positive audit records a false-negative rate of up to about one in five cannot be excluded
```

替换后：

```
review was therefore concentrated on algorithm-positive records, the direction in which every observed error lay. With only 14 positive audit records, however, a false-negative rate of up to about one in five cannot be excluded
```

### 9. `results-table1-pointer`

替换前：

```
and 3 days where known malrotation was operated non-acutely (Table 1).
```

替换后：

```
and 3 days where known malrotation was operated non-acutely.
```

### 10. `results-crp-availability-pointer`

替换前：

```
availability ranged from 45% to 65% across the three duration strata of the source cohort (Table 1).
```

替换后：

```
availability ranged from 45% to 65% across the three duration strata of the source cohort (Supplementary Methods S4).
```

### 11. `results-interaction`

替换前：

```
The effect of rotation did not depend on duration: the multiplicative interaction was null (OR 1.02, 0.89–1.17; likelihood ratio P = 0.785)
```

替换后：

```
No modification of the rotation effect by duration was detected: the multiplicative interaction term was close to null (OR 1.02, 0.89–1.17; likelihood ratio P = 0.785)
```

### 12. `results-crp-depended`

替换前：

```
That CRP association depended entirely on specimens drawn on the day of surgery.
```

替换后：

```
That CRP association rested on specimens drawn on the day of surgery.
```

### 13. `results-null-together-a`

替换前：

```
, the neutrophil count was null (OR 1.00, 0.82–1.19), and the joint likelihood ratio test became null (χ² = 0.40 on 2 df, 
```

替换后：

```
, the neutrophil count estimate was centered on the null (OR 1.00, 0.82–1.19), and neither the joint likelihood ratio test (χ² = 0.40 on 2 df, 
```

### 14. `results-null-together-b`

替换前：

```
), as did the change in discrimination (
```

替换后：

```
), the change in discrimination (
```

### 15. `results-null-together-c`

替换前：

```
, DeLong P = 0.324) and the integrated discrimination improvement (
```

替换后：

```
, DeLong P = 0.324) nor the integrated discrimination improvement (
```

### 16. `results-null-together-d`

替换前：

```
) (Table S3). In the same-day subset the association persisted
```

替换后：

```
) reached significance; with 17 events that subset is compatible with a range of effects as well as with none (Table S3). In the same-day subset the association persisted
```

### 17. `results-missingness-null`

替换前：

```
The null result did not depend on the missingness mechanism:
```

替换后：

```
The non-significant result did not depend on the missingness mechanism:
```

### 18. `discussion-identifies-twist`

替换前：

```
In a child with confirmed volvulus, a history measured in hours therefore identifies the dangerous, complete twist, and its brevity should raise rather than lower concern.
```

替换后：

```
In a child with confirmed volvulus, a short history therefore makes the complete, strangulating twist more likely rather than less, and should raise rather than lower concern.
```

### 19. `discussion-assert-opposite`

替换前：

```
Two series assert the opposite, that ischemia and necrosis bear no clear relation to the duration of illness,
```

替换后：

```
Two series state that ischemia and necrosis bear no clear relation to the duration of illness,
```

### 20. `discussion-recomputation`

替换前：

```
Recomputed from their published tables, the three disagree, and not according to measurement source: two run in the direction reported here, one significantly and one not (necrosis in 2 of 6 children at 720° or more against 1 of 15 below, P = 0.18), while the third, also operative, runs the other way, with no necrosis at all among its eleven children at 720° (P = 0.34). None is informative at that sample size.
```

替换后：

```
Recomputation loosens even the alignment with measurement source. The sonographic series reported a greater twist in ischemic bowel. Of the two operative series, the one recording degrees shows the gradient reported here when its own table is recomputed, though not significantly (necrosis in 2 of 6 children at 720° or more against 1 of 15 below, P = 0.18); the one counting turns records no gradient. None is informative at that sample size.
```

### 21. `discussion-markers-null`

替换前：

```
once specimens that cannot be shown to precede the incision are excluded, the likelihood ratio test, the integrated discrimination improvement and the change in discrimination are null together. The association is present but is not demonstrably preoperative.
```

替换后：

```
once specimens that cannot be shown to precede the incision are excluded, the likelihood ratio test, the integrated discrimination improvement and the change in discrimination all cease to be significant together. That subset retains 17 events, so it does not establish that the markers carry no preoperative information; what it establishes is that none can be demonstrated here.
```

### 22. `discussion-add-nothing`

替换前：

```
They add nothing usable to what the history and the operative finding already provide.
```

替换后：

```
On these data the markers cannot be shown to add anything usable to what the history and the operative finding already provide.
```

### 23. `conclusion-added-nothing`

替换前：

```
once those were excluded they added nothing.
```

替换后：

```
once those were excluded, no contribution could be demonstrated in the 17 events that remained.
```

### 24. `table3-equation`

替换前：

```
logit(p) = -1.8020 +0.5056 x rotation -0.5266 x duration -0.0075 x age +0.7196 x male sex
```

替换后：

```
logit(p) = −1.8020 + 0.5056 × rotation − 0.5266 × duration − 0.0075 × age + 0.7196 × male sex
```

### 25. `table2-mann-whitney`

替换前：

```
Mann-Whitney U test
```

替换后：

```
Mann–Whitney U test
```

### 26. `supplementary-pointer`

替换前：

```
Supplementary Methods S1–S5 and Supplementary Tables S1–S4
```

替换后：

```
Supplementary Methods S1–S6 and Supplementary Tables S1–S4
```


## 手稿上标引用重编号

按文档顺序逐个上标引用重写：

| # | 替换前 | 替换后 |
|---|---|---|
| 1 | `1` | `1` （不变）|
| 2 | `2` | `2` （不变）|
| 3 | `3` | `3,4` |
| 4 | `4,5` | `1` |
| 5 | `4,6` | `1,5` |
| 6 | `7` | `6` |
| 7 | `8` | `7` |
| 8 | `9` | `8` |
| 9 | `10` | `9` |
| 10 | `11` | `10` |
| 11 | `12,13` | `11,12` |
| 12 | `14` | `13` |
| 13 | `15` | `14` |
| 14 | `16` | `15` |
| 15 | `14,17` | `13,16` |
| 16 | `18` | `17` |
| 17 | `19` | `18` |
| 18 | `20` | `19` |
| 19 | `21` | `20` |
| 20 | `22,23` | `21` |
| 21 | `14` | `13` |
| 22 | `7,11` | `6,10` |
| 23 | `7` | `6` |
| 24 | `11` | `10` |
| 25 | `7-11` | `6-10` |
| 26 | `14` | `13` |


## TRIPOD 清单 `TRIPOD_checklist.docx`

### 1. `tripod-supplementary-sections`

替换前：

```
Supplementary Methods S1–S5
```

替换后：

```
Supplementary Methods S1–S6
```

### 2. `tripod-imaging-series`

替换前：

```
; the two imaging series concluding the angle is unhelpful
```

替换后：

```
; the two imaging series that comment on the angle without testing it
```


## TRIPOD 清单上标引用重编号

按文档顺序逐个上标引用重写：

| # | 替换前 | 替换后 |
|---|---|---|
| 1 | `7-9` | `6-8` |
| 2 | `10,11` | `9,10` |
| 3 | `14,17` | `13,16` |
| 4 | `19` | `18` |
| 5 | `18` | `17` |
| 6 | `20` | `19` |
| 7 | `21` | `20` |


## Cover letter `Cover_letter.docx`

### 1. `cover-identifies-twist`

替换前：

```
in a child with confirmed volvulus, a history measured in hours identifies the dangerous twist, and its brevity should raise rather than lower concern.
```

替换后：

```
in a child with confirmed volvulus, a short history makes the dangerous twist more likely rather than less, and should raise rather than lower concern.
```

### 2. `cover-null-together`

替换前：

```
the likelihood ratio test, the change in discrimination and the integrated discrimination improvement were null together (P = 0.818).
```

替换后：

```
the likelihood ratio test, the change in discrimination and the integrated discrimination improvement all ceased to be significant together (P = 0.818, on the 17 events that remained).
```

### 3. `cover-counts`

替换前：

```
The manuscript comprises 5,656 words of main text with a 247-word structured abstract, 23 references, 4 tables and 4 figures,
```

替换后：

```
The manuscript comprises 5,711 words of main text with a 250-word structured abstract, 21 references, 4 tables and 4 figures,
```


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
