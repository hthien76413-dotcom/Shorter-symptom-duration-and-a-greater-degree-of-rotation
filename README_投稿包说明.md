> # ⚠ 本文件不随稿提交
> 本文件仅供内部使用，含不对外披露的沿革信息。上传投稿系统时**只上传下方清单中的 9 个文件**。

---

# 第 3 次投稿：European Journal of Pediatric Surgery

**稿件：** *Degree of rotation and duration of symptoms are independently associated with bowel compromise in children operated for acute midgut volvulus*

**投稿系统：** http://mc.manuscriptcentral.com/ejps

**沿革（不对外）：** 第 1 次投 Pediatric Surgery International，2026-09-07 拒稿。**2026-09-12 用户决定：投稿材料中不主动披露此次拒稿。** 已据此删除 cover letter 的披露段、将 `Response_to_previous_review_v2` 移出投稿包，并把手稿/TRIPOD/Table S4 中归因于 "peer review" 的表述改写。**「这些改动是事后做的、非预先设定」的诚信声明全部保留**，只是不再说明起因。拒稿信、被拒手稿、完整应答文件与 SAP 均留在项目根目录作内部记录。

---

## 一条规矩

**本文件夹的交付文件只能由 `build_ejps_package.py` 生成，不要手工复制 docx 进来。**

```
python build_ejps_package.py
```

`tables_v2.py` 与 `figures_v2.py` 的产出目录已改为本文件夹，md → docx 也由该脚本统一调用。md 源文件留在项目根目录——手稿、补充材料、TRIPOD 换刊也要用，不属于 EJPS 专有。

## 包内清单（9 个文件，即上传集）

| 文件 | 说明 |
|---|---|
| `②_manuscript_EJPS_single.docx` | **单一稿件文件**：题名页 ▸ 摘要与关键词 ▸ 正文 ▸ Acknowledgments ▸ Conflict of Interest ▸ 其余声明 ▸〔分页〕References ▸〔分页〕Figure captions ▸〔分页〕Tables 1–4（表内嵌，图不内嵌） |
| `②_Tables_supplementary_v2.docx` | Table S1–S4（补充材料，单独上传） |
| `②_Supplementary_Methods.docx` | S1 结局裁定 / S2 病程解析 / S3 症状提取与否定处理 / S4 化验缺失 / S5 文献检索 / **S6 统计细节** |
| `TRIPOD_checklist.docx` | 22 项 + 「提请编辑注意」三项限定说明 |
| `Cover_letter.docx` | 以病程发现开头 |
| `Figure1_flow_v2.tif` 等 4 张 | **1200 dpi、CMYK、LZW**，各自成文件（3.0/1.9/3.0/1.2 MB） |

**不在上传集、留在项目根目录供内部查看**：`②_Tables_main_v2.docx`（主表已并入单文件稿）、`Figure*_v2.pdf`（图的矢量预览）、全部 `.md` 源文件。

## 投稿前必须处理（已核对 EJPS 现行 Author Instructions，2026-09-12）

来源：https://lp.thieme.de/open-access-files/116/author_instructions.pdf

| 项 | 须知 | 现稿 | |
|---|---|---|---|
| 题目 | ≤25 词 | 20 词 | ✅ |
| 表图数量 | **未设上限** | 4 表 4 图 | ✅ |
| 篇幅 | "10 to 12 pages"（见下） | 正文 **5,711 词**，约 **35 稿件页** | ⚠ **口径未定，投稿前必须问编辑部；原记的 4,951 词是错的** |
| 摘要 | ≤250 词 | **250 词**（含四个小标题；不含则 244） | ✅ 顶格，不能再加字 |
| 摘要小标题 | Introduction / Materials and Methods / Results / **Conclusions** | 同左 | ✅ 已改 |
| 关键词 | 3–5 | **5 个** | ✅ 已改 |
| 拼写 | **American English** | 已转（三轮共 64 处；文献题名内 1 处 colour 依原文保留） | ✅ 已改 |
| 文献 | **AMA 式 + 上标数字**，>6 作者用 et al，末尾无句点 | 同左（**21 条**，第 3 投做过文献表手术，见下；8 条改 et al，DOI 已按须知示例删除） | ✅ 已改 |
| 文件组织 | **单文件**：题名页+摘要+正文+文献+图注+表；图另存 | 同左（`build_ejps_single.py` 组装，4 个规定分页符已插） | ✅ 已改 |
| 图格式 | 线条图 **1200dpi TIFF/EPS**、**CMYK**；禁用 Excel/Word/PPT 制图 | 1200dpi TIFF、CMYK、LZW（matplotlib 生成） | ✅ 已改 |
| 伦理 | **须写进 Methods**，含审查机构全称 | Methods 首节已加（机构全称+批号+豁免理由+赫尔辛基宣言），Declarations 保留 | ✅ 已改 |
| COI | 每位作者一份 **ICMJE 表**，无冲突也要交 | 未准备 | ❌ |
| Graphical abstract | 鼓励（修回时），PPT 模板，命名 "Infographic" | 未做 | 可选 |

**关于 "(10 to 12 pages)" 的口径**：须知全文未定义指稿件页还是印刷页（已穷举 PDF 中全部 "page" 出现处）。已用实证判定：

从 PubMed 取 EJPS 近期研究论文 12 篇，**印刷页中位 8、IQR 6–9、范围 4–11、无一超过 11**。若按「稿件页」读法（双倍行距 12pt、约 275 词/页），一篇论文全文只能 2,750–3,300 词、排版后约 3–4 印刷页 —— 与实测普遍 8 页矛盾。按「印刷页上限」读法则吻合。最接近的同类论文为 *Development of a Clinical Predictive Score for Bracing Outcomes in Children with Pectus Carinatum: A Single-center Retrospective Study*（Eur J Pediatr Surg 2026;36:305–315，**11 页**，单中心回顾性预测评分）。

**⚠ 2026-09-18 更正：上面这个结论下得太满了。** 「按印刷页读法则完全吻合」这句站不住，原因有二。

其一，**字数记错了**。原表里的「正文 4,951 词」不对：按 Word 口径（空白分词）逐段重数，第 3 投改动前是 **5,651 词**，改后 **5,711 词**，差了 760 词。

其二，也更要紧——**须知自己定义了「manuscript」是什么**。原话是：manuscript 包含 *title page、abstract、keywords、graphical abstract、text、references、figure captions 和 tables*，全部 **双倍行距、12 pt、1 英寸页边距**。一份文件先把「manuscript」的版式定死，再给一个以「pages」为单位的长度上限，这个上限相当自然地就是**该版式下的稿件页**。原来记的「须知全文未定义指稿件页还是印刷页」漏掉了这条上下文。

按须知规定的版式实测（Liberation Serif 逐行模拟，与 Times New Roman 度量兼容；23 行/页）：**本稿约 35 页**，上限 10–12 页，**约 3 倍**。

两种读法现在都还活着，各有硬伤：

| 读法 | 支持 | 反证 |
|---|---|---|
| **稿件页**（约 35 / 10–12） | 须知在同一份文件里把 manuscript 版式定死为双倍行距 12pt | 按这个读法，实测那 12 篇已发表论文（印刷页中位 8，对应稿件页约 30+）**没有一篇合规**——这条规矩就成了没人遵守的规矩 |
| **印刷页**（约 11–12 / 10–12） | 与实测 4–11 印刷页的分布吻合，作为上限讲得通 | 须知里「pages」前后文讲的都是稿件版式，不是印刷版面 |

**结论：口径未定，且两种读法下的处置差别很大**（一种是照投，一种是要砍掉三分之二）。这已经不是「要完全确定仍须问」的可选项，而是**投稿前必须先问清楚**的事——问错了最坏是 desk reject。问法：


> Could you confirm whether the "10 to 12 pages" stated for Original Articles refers to typeset journal pages or to double-spaced manuscript pages?

## 投稿前核对实测结果（2026-09-18）

下面这些是这次逐项量出来的，不是照抄上一轮的记录：

| 项 | 须知 | 实测 | |
|---|---|---|---|
| 题目 | ≤25 词 | 20 词 | ✅ |
| 摘要 | ≤250 词 | 250 词（含四个小标题） | ✅ 顶格 |
| 摘要小标题 | Introduction / Materials and Methods / Results / Conclusions | 四个全对 | ✅ |
| 关键词 | 3–5 | 5 | ✅ |
| 正文版式 | 双倍行距、12 pt | Times New Roman 12 pt、行距 DOUBLE | ✅ |
| 页边距 | 1 英寸 | 原为左右 **1.25 英寸** | ✅ **本轮已改为 1.00** |
| 拼写 | American English | 漏了一处 `per cent` | ✅ **本轮已改 `percent`**（文献题名内的 `colour` 依原文保留，正确） |
| 文献格式 | AMA、上标、>6 作者 et al、末尾无句点 | 21 条逐条审过，全部合规 | ✅ |
| 引用编号 | —— | 首次出现顺序 1…21 连续、无漏引、无多余 | ✅ |
| 表图数量 | 未设上限 | 4 表 4 图 | ✅ |
| 图格式 | 1200 dpi、CMYK、线条图 TIFF | 四张全是 1200×1200 dpi、CMYK、LZW、8 bit/通道 | ✅ 逐张读文件头核实 |
| 章节标题 | —— | 正文曾作 `Materials and methods`，与摘要小标题大小写不一致 | ✅ **本轮已统一** |
| 篇幅 | "10 to 12 pages" | **约 35 稿件页 / 正文 5,711 词** | ⚠ **见下，口径必须先问编辑部** |
| COI | 每位作者一份 ICMJE 表 | 未准备 | ❌ |

期刊本身也确认过：European Journal of Pediatric Surgery，Thieme 出版，EUPSA（欧洲小儿外科医师协会）会刊——选刊没问题。**主编姓名和投稿系统地址没能在线确认**（容器网关拦掉了 Thieme 站点），cover letter 抬头仍是 "The Editors"，见待办 1。

## 第 3 投本轮改动（2026-09-18）

> **⚠ 这一轮是直接改 docx 的。** 本仓库里只有 9 个交付文件，没有 `.md` 源文件，所以无法按「一条规矩」走 `build_ejps_package.py`。**下次在本机跑 build 脚本之前，必须先把 `REVISIONS_3rd_submission.md` 里的逐条改动搬回项目根目录的 `.md` 源文件**，否则这一轮改动会被重新生成的 docx 覆盖掉。

改动脚本留在 `tools/`，可重跑、每条都带命中数断言：

- `tools/revise_manuscript.py` —— 手稿（摘要／引言／方法／结果／讨论／结论／表注／文献表）
- `tools/revise_companions.py` —— TRIPOD 清单与 cover letter
- `tools/docx_edit.py` —— 共用的 docx 编辑与校验函数

四类改动，逐条对照见 `REVISIONS_3rd_submission.md`：

1. **文献表手术**：23 条 → **21 条**。删 Casalino（该文是新生儿节段性 vs 中肠扭转的系统综述，撑不起它所挂的「术中所见的严重程度难以预判」那句）；TRIPOD 2015 两条并成一条（正文清单就是 2015 版 22 项，见下面待办 7）。Ramsey 那条是收入差距的数据库研究，也撑不起开篇的临床断言，已把开篇改引 McCurdie，Ramsey 移到它确实支持的切除那一句。全文重新编号，首次出现顺序为 1…21 连续、无漏引；AMA 分隔符已校验（2 个连号用逗号，3 个以上才用连字符）。
2. **越界表述**：`the one determinant` → `among the few determinants`；`identifies the dangerous, complete twist` → 概率式表述（手稿与 cover letter 同步）；`Two series assert the opposite` → `Two series state that…`；引言 `in under 35.2% of cases` → `in 35.2% of cases`。
3. **把「测不出」讲成「不存在」**：摘要、结果、讨论、结论四处统一改成「未能显示」，并点明剩下的子集只有 **17 个事件**。摘要里 `the markers` 原本全文无先行词，已补成 C-reactive protein and neutrophil count。
4. **前后文对不上**：手稿正文说补充方法是 S1–S5、实际有 S6（手稿与 TRIPOD 清单均已改 S1–S6）；两处 `(Table 1)` 指向 Table 1 里根本没有的数据（按指征分层的中位手术间隔、CRP 可得率），已分别删除与改指 Supplementary Methods S4；TRIPOD 清单 3a 把两篇影像系列都说成「认为角度无用」，其中一篇在引言里是相反立场，已改；Table 3 表注的模型式子用的是 ASCII 连字符和 `x`，已改成 `−` 与 `×`；Table 2 表注 `Mann-Whitney` → `Mann–Whitney`；cover letter 的字数／文献数已按改后重算（5,711 词 / 250 词摘要 / 21 条）。

## 其他待办

1. **Cover letter 抬头仍是 "The Editors"**，未填主编姓名。
2. **题名页学位译法**：Jun Yang 为临床医学博士，**MD 已由作者确认**（2026-09-12）。两位硕士按医学硕士译作 **MMed**（临床职称为主治/主任医师，此译法为常规）；若实为非医学硕士则应改 MSc。
3. **通讯地址未含街道门牌**，现为"Wuhan 430016, Hubei Province, China"。须知要求 mailing address，若编辑部要求详址请补。
4. **两处待外科医生过目**：手术指征五分类（回顾性从病历文本派生）；血便 24 例（调整 OR 5.95，仅 16 个事件，CI 上限 17.74）。
5. **清样须逐字检查 Supplementary Methods S3 的中文**（`不伴`、`非喷射性`、`黄绿色` 等提取规则原词，58 处），确认排版不丢字。
6. **Rhim 那篇的旋转度数表必须对着韩文原文再核一遍。** 原稿讨论里写「11 个 ≥720° 的孩子无一例坏死（P = 0.34）」——这个 P 值算不出来：29 例、5 例坏死、0/11 对 5/18，Fisher 双侧是 **0.15**；把分母在 3–19 之间穷举一遍，也没有任何一种组合给出 0.34。本轮已把这句降级为「计turns 的那篇未见梯度」，不再给分母和 P 值。**核对原文后再决定是写回具体数字还是就这么留着。**（同段里 Zhang W 的 2/6 对 1/15、P = 0.18 是对的，已复算；P0077 里 Rhim 病程那组 3/7 对 2/22、P = 0.08 也是对的。）
7. **TRIPOD 还是 TRIPOD+AI，要定。** 上一轮的计划是并成 TRIPOD+AI 一条，但随稿提交的 `TRIPOD_checklist.docx` 是 2015 版 22 项清单；正文引 TRIPOD+AI、附件交 2015 清单，编辑一眼就能看出对不上。本轮按「与附件一致」处理：并成 Collins 2015 那一条（Moons 的 E&E 删掉）。要改成 TRIPOD+AI 的话，**22 项清单得按 27 项重做**——本会话拿不到 TRIPOD+AI 清单原文（容器只放行包管理源，学术站点全被网关拦掉），需要把清单文本给我，或在能联网的环境里做。
8. **两项要数据才能做的，本轮没做**：一次要结局（不可逆坏死，19 例）的效应量表；选择偏倚的交互检验（Table 4 里「术前疑诊 / 未疑诊」两行只给了分层估计，没有正式交互检验）。分析集 `②_分析集_frozen_v3_20260909.csv` 和分析脚本都不在本仓库里，本轮无法重算。把数据和脚本放进来即可补。

## 数据出处

分析集 `②_分析集_frozen_v3_20260909.csv`，SHA-256 `002504360e8b2db93431d7afc07259bdaea046642b8a801d7159aa0aeaeae65d`，留在项目根目录。急性中肠扭转队列 n = 287，主结局事件 63。
