# Output Schema

## Recommended output bundle
A complete v1 result should try to include:

1. Inferred game profile
2. Page list
3. Asset mapping table
4. Page plans
5. Engine-neutral UI spec
6. HTML/CSS prototype notes
7. Motion notes
8. Confidence + fallback notes

## Example result shape
```json
{
  "game_profile": {},
  "page_list": [],
  "asset_mapping": [],
  "pages": [],
  "engine_neutral_ui_spec": {},
  "html_css_prototype_notes": {},
  "motion_notes": [],
  "confidence_notes": []
}
```

## Confidence labels
- high
- medium
- low

## Fallback expression
Whenever fallback is used, state:
- what was uncertain
- what default was chosen
- why that fallback is safer
