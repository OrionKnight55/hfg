"""Recheck deliverables against the untouched CSV, plus focused failure-mode checks."""
import copy,csv,json,sys
from pathlib import Path
import extract_risks as e
def main():
 if len(sys.argv)!=2: raise SystemExit('Usage: python validate_outputs.py path/to/source_original.csv')
 base=Path(__file__).resolve().parent
 with Path(sys.argv[1]).open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
 topics=json.loads((base/'risk_topics.json').read_text(encoding='utf-8'))
 e.SCHEMA=json.loads((base/'risk_topics.schema.json').read_text(encoding='utf-8'))
 e.schema_check(topics,e.SCHEMA); e.validate(topics,rows)
 tests=['full_schema_and_source_validation']
 def rejected(t):
  try: e.validate(t,rows)
  except (ValueError,AssertionError,KeyError,TypeError): return True
  return False
 mutated=copy.deepcopy(topics); mutated[0]['updates']=None
 assert rejected(mutated); tests.append('rejects_null_instead_of_array')
 mutated=copy.deepcopy(topics); mutated[0]['ai_content']['key_assessment_points'][0]['support']['excerpt']='THIS EXCERPT IS NOT IN THE SOURCE'
 assert rejected(mutated); tests.append('rejects_unsupported_excerpt')
 i=next(i for i,t in enumerate(topics) if t['chart_data']['available'])
 mutated=copy.deepcopy(topics); mutated[i]['acaps_assessment']['impact']['normalized']=999
 assert rejected(mutated); tests.append('rejects_changed_rating')
 mutated=copy.deepcopy(topics); mutated[0]['sources'].append({'source_id':'fake','url':'https://invented.invalid/example','source_columns':['Rationale'],'independently_verified':False})
 assert rejected(mutated); tests.append('rejects_invented_url')
 cache=json.loads((base/'agent_ai_cache.json').read_text(encoding='utf-8'))
 original=rows[0]; t=e.prepare(original,2,'test'); e.apply_ai(t,original,cache[original['Risk ID']]); assert t['provenance']['processing_status']=='processed_draft'
 changed=dict(original); changed['Rationale']+=' Changed.'; t=e.prepare(changed,2,'test'); e.apply_ai(t,changed,cache[original['Risk ID']]); assert t['provenance']['processing_status']=='ai_pending' and t['ai_content']['summary'] is None
 tests.append('invalidates_changed_record_cache')
 unknown=dict(original); unknown['Probability']='Unknown future category'; unknown['Impact']='0'; unknown['Expected priority needs']='Unfamiliar need'
 t=e.prepare(unknown,2,'test'); assert t['acaps_assessment']['probability']['normalized']=='Unknown future category' and t['acaps_assessment']['impact']['normalized']=='0' and not t['chart_data']['available']
 assert {'unknown_category','unknown_score','unknown_priority_need'} <= {f['code'] for f in t['quality_flags']}
 tests.append('preserves_and_flags_unknown_categories_and_zero_score')
 assert e.date_value('05/08/2026')['normalized'] is None and e.date_value('30/09/2026')['normalized']=='2026-09-30' and e.date_value('31/02/2026')['certainty']=='invalid'
 tests.append('preserves_ambiguous_and_invalid_dates')
 assert len(topics)==139 and all(t['publication_status']=={'state':'draft','requires_moderator_review':True} for t in topics)
 assert all(not any(k in t for k in ['expert_reviews','consensus','participation_count']) for t in topics)
 tests.append('draft_only_no_synthetic_reviews')
 result={'status':'passed','automatic_checks':tests,'semantic_correctness_proven':False,'note':'The bundled validator implements the JSON Schema keywords used by this schema; it is not a general-purpose JSON Schema engine. Semantic review is separate.'}
 (base/'validation_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps(result,indent=2))
if __name__=='__main__': main()
