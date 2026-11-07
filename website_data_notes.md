# Import structure and chart guidance

`risk_topics.json` is a UTF-8 JSON array. Schema version: `1.0.0`. Validate the array against `risk_topics.schema.json` (JSON Schema draft 2020-12). Import records by `risk_id`, retaining the source-record hash to detect changes. Do not publish automatically: `publication_status.state` is always `draft` and `requires_moderator_review` is true.

| Section | Meaning |
|---|---|
| `risk_id` | Original source ID, shared by all outputs |
| `source_record` | CSV row number (header is row 1) and all 25 source fields; empty strings represented as null, substantive text retained |
| `acaps_assessment` | Copied ratings and categories; `raw` preserves original nonempty text, `normalized` trims whitespace or types valid 1–5 scores; countries, ISO codes, needs become arrays |
| `ai_content` | Labelled AI title, summary, selected assessment claims, impacts, vulnerabilities, positive capacities, and suggested questions |
| `triggers` | Deterministically parsed labelled trigger blocks; original trigger IDs, descriptions, sources, completion criteria, dates, and completion histories retained |
| `updates` | Separate rationale updates with original date text, nullable normalized date, AI summary, exact source segment, and that segment’s URLs |
| `sources` | Deduplicated record-level URLs with source-column locations; external verification always false |
| `chart_data` | Ordinal probability/impact matrix inputs, or an unavailable marker |
| `quality_flags` | Machine-readable code plus readable detail; may contain more than one flag per field |
| `provenance` | Source hashes, execution mode, nullable model identity, prompt version, processing state, and semantic scope |
| `publication_status` | Moderator gate; no publication action was taken |

Each reviewable point has a stable content-based `point_id`, AI text, and `support` containing the risk ID, exact source column, exact supporting excerpt, URLs, and URL-association certainty. Full-field excerpts are deliberately conservative but coarse; moderators should refine them. Claims do not inherit all record URLs. Trigger `source_urls` are taken from that trigger’s explicit Sources block. Update URLs come only from that update’s segment. Neither convention asserts independent verification or that every link supports every sentence. Preserve original Markdown and raw fields for audit. Extracted URL tokens remove only enclosing syntax; no URLs are constructed or fetched.

`point_id` is the risk ID, point kind, and a short SHA-256 digest of the AI claim text. It stays unchanged if records are reordered, but changes when the claim text changes. Original `trigger_id` remains the primary trigger identifier. Update IDs hash the exact update segment and therefore change when that segment changes. Use source hashes to invalidate stale AI caches and keep website review history separately from ACAPS data. No expert-review data is included.

The source-record hash is SHA-256 of the complete raw CSV dictionary serialized as UTF-8 JSON, sorted keys, no separator whitespace, `ensure_ascii=False`. It is calculated before null/whitespace normalization. The source-file hash covers the original bytes. The reusable cache is keyed by risk ID plus matching source-record hash; schema/semantic validation remains necessary after reuse. Prompt version changes should trigger an explicit cache refresh rather than silently reusing old content.

## One graphic per topic

Use `chart_data.type = ordinal_probability_impact_matrix`. Plot only when `available` is true. The x-axis positions are Very Low=1, Low=2, Medium=3, High=4, Very High=5. Display the category label, not a percentage. These positions indicate order, not equal numerical probability intervals. The y-axis uses the existing ACAPS impact score. Show ACAPS risk level separately as provided; do not recalculate it from the coordinates or impose an invented risk-level formula.

If either axis is missing or unrecognized, both plotted coordinates are null and the chart is unavailable. Do not render a point at zero. Keep exposure bands as categories and do not convert them to exact population estimates. No dated risk-rating history was constructed. Trigger completion histories are task/criterion progression, not risk probabilities or a risk-over-time series.

Dates use `{raw, normalized, certainty}`. Numeric dates whose day/month order cannot be uniquely determined remain null with `ambiguous_day_month`; no dataset-wide convention is silently imposed. Calendar-valid dates can still have a narrative year conflict, recorded in quality flags. Undated text stays undated. No whole-risk last-update timestamp is derived from trigger metadata. The source contains embedded updates inside some Rationale fields; these remain in that field and are flagged rather than silently recast into Rationale update chronology.

Unknown categories and unexpected scores are retained and flagged. Do not coerce them to known values at import. `ai_pending` and `ai_error` records must remain visible in moderator queues and unavailable for publication until repaired. For this export, all records received AI drafts and none failed. Full semantic review and exhaustive claim coverage remain outstanding for moderators.
