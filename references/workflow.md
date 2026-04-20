# Workflow

## Core flow
1. Parse minimal input
2. Infer missing context conservatively
3. Classify asset roles
4. Select compact page scope
5. Identify gameplay exclusion zones
6. Build page structures
7. Harmonize style
8. Add light motion if appropriate
9. Produce structured outputs
10. Run quality check and fallback if needed

## Phase 1: Understand
Inputs:
- images
- short game description
- optional constraints
- optional motion preference
- optional output target

Outputs:
- inferred game profile
- inferred platform and orientation
- initial confidence levels

## Phase 2: Plan
Outputs:
- page list
- page priority
- asset-role mapping
- page-specific asset assignments
- page-specific safety notes

## Phase 3: Compose
Outputs:
- component trees
- anchors and size hints
- interaction states
- hierarchy and emphasis notes

## Phase 4: Adapt
Possible targets:
- engine-neutral-ui-spec
- html-css-prototype
- static-image-guidance
- h5-guidance
- gif-video-preview guidance

## Phase 5: Review
Check:
- gameplay safety
- consistency
- clarity
- output target match
- implementation cost

## Minimum-question rule
Only ask questions if one of the following is unresolved and high-impact:
- platform/orientation
- safe zone understanding
- final output target
- motion level
- page scope ambiguity
