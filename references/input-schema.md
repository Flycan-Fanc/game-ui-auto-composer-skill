# Input Schema

## Minimal public input
The external input should stay simple.

Required:
- `pics`
- `game_description`

Optional:
- `constraints`
- `motion_preference`
- `output_target`

## Example
```json
{
  "pics": [
    {
      "file": "bg_home.png",
      "type": "background",
      "required": true,
      "reusable": false,
      "scalable": false
    }
  ],
  "game_description": {
    "title": "Swap!",
    "genre": "casual lane-switch",
    "platform": "wechat mini-game",
    "orientation": "landscape",
    "gameplay": "two characters swap lanes to avoid obstacles",
    "core_interaction": "tap to switch",
    "style_keywords": ["neon", "cute", "arcade"]
  }
}
```

## Internal normalized model
Internally, enrich each asset with:
- file format
- width / height
- transparency
- stretchability
- tileability
- frame sequence flag
- motion suitability
- visual priority
- likely page usage

## Rules
- External schema should stay easy for developers
- Internal schema can be richer
- Missing low-impact details should be inferred, not queried
