# Reviewing the risk topics

Start with **risk_topics_review.csv**. It has one row per risk and opens in Excel. Review the title, summary, triggers, impacts, questions, and quality flags. A blank cell means information is unavailable, not zero. All topics are drafts.

Give your website developer **risk_topics.json**, **risk_topics.schema.json**, and **website_data_notes.md**. The JSON is an array of 139 topics, connected by the original risk ID. Nothing has been published and no website or ACAPS API integration was built.

The original ACAPS assessments are in `source_record` and `acaps_assessment`. Ratings are copied from the CSV, with original values alongside normalized values. The summaries, selected assessment points, impacts, vulnerabilities, capacities, and questions are AI-written drafts. Trigger fields are parsed from existing labelled text. Dated update summaries are AI-written; dates and source passages are retained separately.

The AI work was performed by the assistant in this chat, using selective source overviews plus additional reading of five initial records and selected passages. It is **not an exhaustive extraction or full semantic review of every long field**. All original text remains available for moderators. Many claim excerpts cover a whole source field and should be narrowed during review. An empty coping-capacity array does not prove there is no local capacity. The exact model identifier was not available and is recorded as null.

Before approving a topic, a moderator should check its full narrative, dates, affected groups, claims, omissions, supporting excerpts, and source relationships. Pay particular attention to conflicting dates and countries. Linked sources were not independently verified. The export’s status does not prove a risk is active today. Suggested questions are AI-generated; no expert reviews were created.

## Repeating the process

The easiest option is to give a Codex assistant the new CSV and this folder and ask it to repeat extraction using the script and prompt. You do not need to paste an API key into chat. Existing source files should remain unchanged.

For someone comfortable running Python 3.10 or newer, keep the script and schema together, then run:

```powershell
python extract_risks.py "new-export.csv" --out "new-results" --ai-cache "agent_ai_cache.json" --prepare-ai-requests
```

This uses only Python’s standard library. Matching cached records reuse the existing AI drafts. Changed or new records are preserved with `ai_pending`; the script writes their full source records into `new-results/ai_requests`. An assistant or language model must process those requests using **prompt_template.md**, update the cache, and rerun the command. The script itself does not generate AI summaries. Processing checkpoints preserve individual records if interrupted.

**extraction_report.md** explains what passed automatic validation, the sample semantic checks, and the remaining limitations. **validation_results.json** supplies machine-readable counts. **source_original.csv** is a byte-for-byte copy of the supplied CSV; its original location was also left unchanged.
