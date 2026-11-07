# Extraction report

Prepared for moderator review on 6 November 2026. The actual input used was the CSV at `C:/Users/world/Downloads/risk-radar-export.csv`. Both CSV and XLSX were present; the requested CSV was processed. The workbook was not used as a substitute. All dataset text was treated as source data, not instructions. No API integration, website, publication, external browsing, or synthetic expert participation was created.

## Actual completion

| Result | Count |
|---|---:|
| Input records | 139 |
| Output records | 139 |
| Fields | 25 |
| Missing IDs / duplicate IDs | 0 / 0 |
| AI draft titles and summaries | 139 / 139 |
| AI assessment points | 139 |
| AI humanitarian impact points | 139 |
| AI vulnerability points | 116 |
| AI positive coping-capacity points | 16 |
| AI-generated review questions | 278 |
| Parsed triggers | 266 |
| Separate rationale updates / AI update summaries | 176 / 176 |
| Charts available / unavailable | 125 / 14 |
| Failed records / AI-pending records | 0 / 0 |

Every source risk ID appears exactly once. Every topic is a draft requiring moderator review. No risk is represented as independently current. There are no expert answers, comments, consensus statistics, participation counts, or AI replacement ratings.

**Scope limitation:** all records received genuine agent-written semantic drafts, but these are selective overviews, not exhaustive extraction of every claim in every long field. Titles, summaries, selected points, impacts, vulnerabilities, capacities, and update summaries were authored by the assistant from source overview passages. The initial five records and selected contradiction/capacity passages received additional reading. Typical batch views used narrative openings up to 850 rationale, 600 impact, 550 vulnerability, and 750 characters per update after removal of URLs for reading; all original source text remains intact in JSON. Further supported claims or capacities may have been omitted. This limitation is flagged on every record and documented in provenance.

## Input inspection

The CSV has exactly 139 records and 25 distinct headers. No row-width errors or duplicate IDs were found. Empty or whitespace-only values are treated as missing. Original CSV bytes were not edited. `source_original.csv` is a verified byte-for-byte copy.

Source-file SHA-256: `dfe92309b9fd2cfa017378713212baf1edb1287ba00837945d120a4586df86e5`.

| Actual header | Missing records |
|---|---:|
| Risk ID | 0 |
| Risk Title | 0 |
| Risk Type | 6 |
| ISO | 0 |
| Country | 0 |
| Rationale | 1 |
| Source | 13 |
| Intensity of hazard | 16 |
| Impact | 10 |
| Probability | 11 |
| Risk Level | 11 |
| Risk trend | 62 |
| Status | 7 |
| What materialised? | 83 |
| Hazard materialisation | 86 |
| Materialisation sources | 72 |
| Triggers | 31 |
| Current vulnerability / Coping capacities | 20 |
| Current vulnerability / Coping capacities sources | 52 |
| Expected exposure | 4 |
| Expected impact | 46 |
| Expected impact sources | 50 |
| Expected priority needs | 35 |
| Impact materialisation description | 91 |
| Rationale update | 76 |

The single missing rationale belongs to R0007; its AI draft explicitly states that it is title-only. Status values are Materialised (61), Not materialised (43), Active (28), and missing (7). There is no literal Resolved category. The sample therefore uses the export’s Materialised and Not materialised values without treating them as proof of closure or present activity.

Probability categories are Very Low, Low, Medium, High, and Very High. Impact scores are 1–5 where present. No unexpected values were observed in the explicitly checked rating, status, risk-type, trend, exposure, priority-need, and ISO-format categories. The accepted priority-need vocabulary is the ten labels observed in this export, not a claim about an authoritative universal taxonomy. New values are retained and flagged by the script.

Whitespace normalization is separated from raw values: 117 records have leading/trailing whitespace in at least one field, and 61 have zero-width or non-breaking whitespace. Hazard intensities include trailing newlines. No replacement characters were found. Normalization trims rating labels and converts only valid 1–5 impact/intensity strings to integers. Country names and ISO codes retain source spelling and order in arrays. Exposure bands remain categories. Missing values never become zero.

## Five-record sample and semantic review

The initial sample comprised R0353, R0990, R0204, R1043, and R0369. It includes R1043, an updated materialised record, a materialised historical record, and sparse not-materialised or missing-status records. The first structural pass was run before continuing the dataset; the completed sample was checked again after update summaries were added.

| ID | Source check and decision |
|---|---|
| R0353 | Rationale concerns attacks on Helmand districts and a disputed retreat. Summary retains uncertainty and does not invent a detailed impact or current date. Missing probability and impact produce an unavailable chart. |
| R0990 | Original return scenario is separated from the update’s reported April–May 2025 movements. Persecution risk remains a forecast/protection concern. The ambiguous update heading is quoted as original numeric text rather than silently normalized. |
| R0204 | Source cites 2016 displacement and camp pressures; summary keeps that historical context. Country and ISO lists are copied, and missing ratings remain unavailable. |
| R1043 | Original cross-border escalation scenario is distinct from September refugee pressures and the absence of identified new attacks in the latter half of September. High probability remains categorical; impact 4 and risk level High are unchanged. |
| R0369 | Sparse source supports displacement and access risks in former FARC-controlled areas; no detailed capacities, new date, or contemporary verification is invented. Materialised status is copied without reinterpretation. |

These were source-grounding reviews by the same assistant, not independent humanitarian expert review. Other records received selective source-overview checks, not full-record semantic audits. The exact-match checks below cannot establish that a broad excerpt fully supports every nuance of a paraphrase.

## Contradictions and review priorities

- **R1017:** update heading 30/01/2025 describes December 2025 and January 2026. The date is calendar-valid but conflicts with the narrative. No year correction was made.
- **R1047:** latest update discusses Madagascar although the topic is Mozambique. It is retained, summarized as a geographic mismatch, and excluded from the Mozambique topic summary.
- **R0134:** early-2022 election wording in the title conflicts with the extended timeline in the rationale.
- **R1011:** the 1 April update’s elapsed-time statement conflicts with the January event date elsewhere; citation-year inconsistencies also require review. Later source-reported political outcomes did not rewrite the original forecast.
- **R1067:** different food-security classifications appear in the same vulnerability field; these were not reconciled into a single asserted classification.
- **R1039:** “Boro output ... down to 10% nationally” is unclear and was not silently rewritten as a 10% reduction.
- **R1013:** a December update repeats the label mass displacement for different counts. No aggregation was attempted.
- **R0970 and R0107:** updates are embedded in Rationale rather than Rationale update. They remain in the original field, are acknowledged in the summary, and are flagged; no missing year is invented.
- **R0106:** mixed reference periods need confirmation.
- **R1054:** the Merowe power-station fire’s cause is unestablished; it was not attributed to drones just because the original risk concerns drone attacks.
- **R1038:** expanding armed activity is distinguished from direct JNIM–ISSP clashes, which the latest update says were not significantly reported.
- **R1055:** pressure to return is distinguished from a sudden mass return that the update says was not clearly evidenced.

Trigger histories retain differing rates on the same raw date. Ten records have at least one such conflict (including R1043–T0619). These values are not averaged or used to overwrite the explicit current completion rate. R0961–T0027 contains a dated history line without a percentage; it is retained in raw fields and flagged as unparsed history. A trigger completion percentage measures the trigger’s stated criterion, not risk probability.

Rationale update dates: 101 normalized unambiguously, 74 retained with ambiguous day/month order, and 1 undated. Dates such as 05/08/2026 are not silently assumed to be day-first even though many records appear to follow that convention. Trigger dates and completion histories use the same conservative approach. Trigger update dates never become a whole-risk last-update date.

## Automatic validation

The saved JSON passes the published schema’s used keywords and additional source-integrity checks. The implementation includes a small dependency-free validator for this schema; it is not a general JSON Schema engine. A developer may additionally validate with a standard draft-2020-12 engine during import.

Checks passed:

- 139 input records equal 139 output records; all IDs accounted for exactly once.
- All copied raw ratings and normalized rating values match deterministic source expectations. All original source fields match, with empty strings represented as null.
- Required objects, arrays, nullable fields, labels, and draft statuses have the expected types and values.
- Titles are at most 15 whitespace-delimited words; summaries are at most 80 (observed maximum 65).
- Every claim, trigger, and update has an exact excerpt occurring in its stated source column with the correct risk ID.
- Every emitted URL is a token found in the source. No linked page was fetched or verified. Broad claims do not inherit record-wide URL lists; uncertain association is explicit.
- Update dates are valid calendar dates or explicitly uncertain/undated. Narrative date contradictions are separately flagged.
- Chart availability and both plotted positions match source probability and impact values. Missing/unknown values are not invented.
- Two labelled AI-generated suggested questions per record; no synthetic expert-review fields.
- Negative tests reject a changed rating, invented URL, unsupported excerpt, and null in place of an array.
- Cache tests reuse unchanged records and invalidate changed records. Unknown categories and a zero score are preserved and flagged; no chart is invented. Ambiguous/invalid dates remain explicit.

See validation_results.json for counts and validation_checks.json for focused test outcomes. Passing these checks does not prove semantic completeness, correct attribution, or factual truth. Numerical claims were kept source-grounded and no new risk probabilities or forecasts were generated; this is a semantic constraint, not something schema validation can fully prove.

## Execution and rerunning

CSV reading, normalization, URL token extraction, labelled-trigger parsing, update segmentation, hashing, validation, chart preparation, and export were deterministic Python code. The standard-library script was implemented and run. AI titles, summaries, selected semantic claims, and questions were authored by the assistant in this chat and saved to a hash-keyed cache. Regex parsing and copied excerpts are never labelled AI summarization.

No API credential variables were present for the checked model providers. No external model API was called. Exact model identity was not available and is null. This was an agent-produced extraction, not a reusable automated AI API pipeline. The prompt template documents how an assistant or configured model can repeat the semantic step. Future changed records remain ai_pending until genuine AI content is supplied; no fabricated success or silent deterministic fallback occurs. No credentials are required to rerun deterministic preparation or reuse this cache.

Unchanged cache entries reproduce these drafts. New/changed source records need an assistant or separately configured model to perform the semantic step. An interrupted run keeps per-record checkpoints. No records failed in this run. Moderator review of the full records, missed claims/capacities, broad excerpts, dates, and citations remains outstanding. There is no external-credential blocker for the delivered draft dataset.
