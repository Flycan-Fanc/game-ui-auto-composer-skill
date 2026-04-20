---
name: game-ui-auto-composer-skill
description: Automatically plans and composes game UI from provided image assets and a short game description. Use when the user has no full design mockup and wants AI to identify asset roles, infer core pages, plan layouts, harmonize style, generate engine-neutral UI specs, or produce implementation-oriented UI output such as HTML CSS prototypes and developer prompts for lightweight game UI workflows.
license: MIT
compatibility: Best for lightweight casual games, mini-games, and MVP UI planning workflows. Optimized for text-first planning, engine-neutral UI specs, implementation guidance, and structured output. Does not require external network access. Scripts are optional helpers for validation and packaging.
metadata:
  author: Flycan-Fanc
  co-created-with: OpenAI ChatGPT
  version: 1.0.0
  category: game-ui
  stage: v1
  output-priority:
    - engine-neutral-ui-spec
    - html-css-prototype
    - structured-page-plan
---

# Game UI Auto Composer Skill

This skill helps generate **structured, implementation-friendly game UI plans** when the developer has:
- image assets but no full design mockup
- a short game description
- a need to reduce manual UI planning work

It is designed as a **v1 MVP skill**. Prioritize reliable automatic planning over maximal coverage.

## Use this skill when

Use this skill when the user wants to:
- build game UI from existing image assets
- infer UI layout without a finished design draft
- plan core game pages such as Home, Gameplay HUD, and Result
- map images to UI roles such as background, button base, title frame, badge, icon, character showcase, or panel
- produce an engine-neutral UI spec for later implementation
- generate HTML/CSS prototype guidance or developer-facing implementation prompts
- reduce developer involvement by letting AI infer most UI decisions automatically

## Do not use this skill when

Do not treat this skill as the best fit when:
- the user needs a final polished brand-grade commercial visual design
- the project is a large MMO, SLG, or deeply customized full-scale game UI system
- the user primarily needs deep engine-specific production files
- the user wants unrestricted freeform art direction rather than structured UI planning
- the task is unrelated to game UI composition from assets

## Core operating principles

1. **Minimum developer burden**
   - Assume the developer only provides essential resources and a short description.
   - Infer the rest whenever confidence is sufficient.

2. **Minimum questions**
   - Ask at most a few necessary questions, and only if missing information would significantly affect page scope, gameplay safety zones, output target, or motion strategy.

3. **Core page loop first**
   - Prefer a complete core loop over page sprawl.
   - Default priority:
     1. Home
     2. Gameplay HUD
     3. Result

4. **Implementation-first output**
   - Prefer structured deliverables that can be used by developers, Codex, or later UI generation workflows.

5. **Engine-friendly representation**
   - Express results as reusable assets, component trees, layout constraints, state definitions, and motion notes, not just as a visual collage.

6. **Conservative fallback**
   - If confidence is low, reduce page scope, simplify layout, and mark assumptions clearly.

## Default workflow

### Step 1: Parse the input
Read the provided images and game description.

Identify:
- game type
- platform
- orientation
- core interaction
- likely gameplay safety zones
- requested output target if any

If details are missing, infer them conservatively.

See:
- `references/input-schema.md`
- `references/supported-scope-v1.md`

### Step 2: Analyze asset roles
Classify assets into likely roles:
- background
- character
- frame sequence
- button base
- title base
- icon
- panel / popup base
- badge / slot / frame
- decoration / effect
- HUD element

Then assign each asset:
- likely page usage
- suggested prominence
- reusability
- stretchability
- dynamic suitability

See:
- `references/asset-taxonomy/buttons-icons.md`
- `references/asset-taxonomy/characters-frames.md`
- `references/asset-taxonomy/panels-badges.md`

### Step 3: Infer page scope
Default to a compact page set unless the input clearly supports more.

v1 default page strategy:
- always consider Home
- always consider Gameplay HUD
- always consider Result
- optionally include Mode Select or Level Select when the game description strongly suggests them

See:
- `references/page-templates/home.md`
- `references/page-templates/gameplay-hud.md`
- `references/page-templates/result.md`

### Step 4: Protect gameplay safety zones
Before composing layouts, identify the gameplay exclusion zone or core view area.

Never let decorative UI crowd the core gameplay view.

See:
- `references/layout-rules/safe-area.md`
- `references/layout-rules/gameplay-exclusion-zones.md`

### Step 5: Compose layout and component tree
Build each page using:
- component hierarchy
- anchor-based layout
- relative size suggestions
- visual hierarchy
- minimum interaction target rules

Express the page as:
- page goal
- main regions
- component tree
- asset mapping
- layout constraints
- interaction states

See:
- `references/layout-rules/anchor-and-sizing.md`
- `references/output-adapters/engine-neutral-ui-spec.md`

### Step 6: Harmonize style
Unify:
- visual density
- button language
- panel language
- title language
- glow / stroke / rounding strength
- decoration intensity

Use only the assets that improve clarity and consistency.

See:
- `references/layout-rules/style-harmonization.md`

### Step 7: Add motion conservatively
Default to light motion only:
- button press feedback
- icon pulse
- badge blink
- popup enter / exit
- score or reward count-up

Avoid rich page performances unless explicitly needed and justified.

See:
- `references/motion-rules/motion-levels.md`
- `references/motion-rules/micro-interactions.md`

### Step 8: Produce outputs
Prefer these outputs in order:
1. structured page plan
2. asset mapping
3. engine-neutral UI spec
4. HTML/CSS prototype guidance
5. optional static visual guidance
6. optional light motion guidance

See:
- `references/output-adapters/engine-neutral-ui-spec.md`
- `references/output-adapters/html-css-prototype.md`

### Step 9: Run quality check
Before finalizing, validate:
- gameplay safety
- visual clarity
- style consistency
- clickability
- implementability
- motion cost
- output match

See:
- `references/quality/quality-checklist.md`
- `references/quality/confidence-and-fallback.md`

## Question policy

Ask clarifying questions only if needed to resolve one of these high-impact gaps:
- unknown platform or orientation
- unknown output target
- unknown gameplay safe area
- multiple equally plausible page structures
- motion level would materially change implementation cost

If the user does not answer:
- adopt conservative defaults
- state assumptions
- continue

## v1 support scope

This v1 is optimized for:
- lightweight casual games
- mini-games
- runner / lane-switch / light merge / light rhythm patterns
- Home + Gameplay HUD + Result core loop
- engine-neutral specs
- HTML/CSS-oriented implementation planning
- Cocos / Unity / HTML5-friendly structural outputs

This v1 is not optimized for:
- full RPG systems
- MMO/SLG complexity
- deep engine exporters
- brand-grade final visual polish

## Recommended output bundle

When possible, produce:
- page list
- page purpose
- asset-role mapping
- component tree
- layout constraints
- motion notes
- implementation notes
- confidence notes

## Example scenarios

### Example 1: Mini-game with scattered assets
User says: "I have a few backgrounds, button frames, and character sprites for a WeChat mini-game. Help me build the UI without a design draft."

Expected behavior:
1. infer mini-game context
2. classify assets
3. propose Home, Gameplay HUD, and Result
4. keep gameplay view clear
5. output engine-neutral page specs
6. add HTML/CSS-oriented prototype notes

### Example 2: Lane-switch game with dynamic sprites
User says: "These are my lane-switch game assets. I need a homepage, in-game HUD, and settlement page."

Expected behavior:
1. identify lane-switch pattern
2. protect middle gameplay lanes
3. map button/panel/title assets to pages
4. keep motion light
5. output page plan plus implementation guidance

## Failure handling

If the input is weak:
- reduce page count
- use conservative layout
- mark uncertain mappings
- prefer structured planning over fake polish

If assets conflict:
- prioritize consistency over asset coverage
- prefer functional clarity
- down-rank decorative noise

If output target is unclear:
- default to structured page plan + engine-neutral UI spec

## Script helpers

Optional helper scripts are bundled under `scripts/`.
Use them when useful:
- `python scripts/validate_input.py <input.json>` for input sanity checks
- `python scripts/quality_check.py <spec.json>` for structured QA hints
- `python scripts/package_output.py <dir>` for packaging results

## Final reminder

This skill is an **automatic UI planning and composition engine**, not a freeform art toy.
Prefer:
- fewer pages
- better structure
- stronger clarity
- lower ambiguity
- easier implementation
