> # ⚠ 本文件不随稿提交
> 本文件仅供内部使用，含不对外披露的沿革信息。上传投稿系统时**只上传下方清单中的 9 个文件**。

---

# 第 2 次投稿：European Journal of Pediatric Surgery

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
| `②_Supplementary_Methods.docx` | S1 结局裁定 / S2 病程解析 / S3 症状提取与否定处理 / S4 化验缺失 / S5 文献检索 |
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
| 篇幅 | "10 to 12 pages"（见下） | 正文 **4,951 词** | ⚠ 口径待定 |
| 摘要 | ≤250 词 | **249 词** | ✅ 已改 |
| 摘要小标题 | Introduction / Materials and Methods / Results / **Conclusions** | 同左 | ✅ 已改 |
| 关键词 | 3–5 | **5 个** | ✅ 已改 |
| 拼写 | **American English** | 已转（三轮共 64 处；文献题名内 1 处 colour 依原文保留） | ✅ 已改 |
| 文献 | **AMA 式 + 上标数字**，>6 作者用 et al，末尾无句点 | 同左（23 条已重排，8 条改 et al，DOI 已按须知示例删除） | ✅ 已改 |
| 文件组织 | **单文件**：题名页+摘要+正文+文献+图注+表；图另存 | 同左（`build_ejps_single.py` 组装，4 个规定分页符已插） | ✅ 已改 |
| 图格式 | 线条图 **1200dpi TIFF/EPS**、**CMYK**；禁用 Excel/Word/PPT 制图 | 1200dpi TIFF、CMYK、LZW（matplotlib 生成） | ✅ 已改 |
| 伦理 | **须写进 Methods**，含审查机构全称 | Methods 首节已加（机构全称+批号+豁免理由+赫尔辛基宣言），Declarations 保留 | ✅ 已改 |
| COI | 每位作者一份 **ICMJE 表**，无冲突也要交 | 未准备 | ❌ |
| Graphical abstract | 鼓励（修回时），PPT 模板，命名 "Infographic" | 未做 | 可选 |

**关于 "(10 to 12 pages)" 的口径**：须知全文未定义指稿件页还是印刷页（已穷举 PDF 中全部 "page" 出现处）。已用实证判定：

从 PubMed 取 EJPS 近期研究论文 12 篇，**印刷页中位 8、IQR 6–9、范围 4–11、无一超过 11**。若按「稿件页」读法（双倍行距 12pt、约 275 词/页），一篇论文全文只能 2,750–3,300 词、排版后约 3–4 印刷页 —— 与实测普遍 8 页矛盾。按「印刷页上限」读法则完全吻合。最接近的同类论文为 *Development of a Clinical Predictive Score for Bracing Outcomes in Children with Pectus Carinatum: A Single-center Retrospective Study*（Eur J Pediatr Surg 2026;36:305–315，**11 页**，单中心回顾性预测评分）。

**结论：不必砍三分之一正文。** 但按每印刷页约 900 词粗估，本稿排版后约 10–11 页，**顶在上限**，故已主动瘦身 273 词。要完全确定仍须问编辑部：

> Could you confirm whether the "10 to 12 pages" stated for Original Articles refers to typeset journal pages or to double-spaced manuscript pages?

## 其他待办

1. **Cover letter 抬头仍是 "The Editors"**，未填主编姓名。
2. **题名页学位译法**：Jun Yang 为临床医学博士，**MD 已由作者确认**（2026-09-12）。两位硕士按医学硕士译作 **MMed**（临床职称为主治/主任医师，此译法为常规）；若实为非医学硕士则应改 MSc。
3. **通讯地址未含街道门牌**，现为"Wuhan 430016, Hubei Province, China"。须知要求 mailing address，若编辑部要求详址请补。
4. **两处待外科医生过目**：手术指征五分类（回顾性从病历文本派生）；血便 24 例（调整 OR 5.95，仅 16 个事件，CI 上限 17.74）。
5. **清样须逐字检查 Supplementary Methods S3 的中文**（`不伴`、`非喷射性`、`黄绿色` 等提取规则原词，58 处），确认排版不丢字。

## 数据出处

分析集 `②_分析集_frozen_v3_20260909.csv`，SHA-256 `002504360e8b2db93431d7afc07259bdaea046642b8a801d7159aa0aeaeae65d`，留在项目根目录。急性中肠扭转队列 n = 287，主结局事件 63。
