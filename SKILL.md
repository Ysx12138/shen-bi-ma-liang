---
name: style-inspiration-cards
description: Generate, number, review, and classify original Web and mobile UI atmosphere images from design.md plus visual references. Analyze and preserve each reference's content-integration logic—how a person, object, material, or scene relates to typography, hierarchy, crop, and layout—without forcing an isolated visual anchor. Use for a single palette-led image, a controlled six-image combination batch with balanced UI/color/mood reference roles, selectable mobile layouts (device mockups or pure-page compositions), or a follow-up selection such as `134` or `234保留` that should copy chosen images into separate Web and mobile upload-material folders.
---

# Style Inspiration Cards

Generate original, non-functional UI atmosphere images. Treat `design.md` as the structural master. Extract role-specific U/C/M attribute specs from every reference before mixing them; final generation uses the compiled specs, not raw reference images, unless the user explicitly asks for direct image conditioning. For content, preserve the reference's **integration logic**: whether a person, object, material, or scene is absent, embedded in a content module, interleaved with type, used as an editorial crop, or treated as a dominant panel. Never force a standalone real-world anchor just to satisfy a checklist. In standard mode, use one selected reference's extracted C spec as the palette master. In controlled combination batch mode, rotate three references through fixed UI-organization, color, and content/mood roles. Use a single full page for Web and one approved, locked mobile layout per output; the layout may be a device composition or a pure-page composition. Never create runnable UI, scrape image sites, reproduce a source, or publish to OPS automatically.

## The contract

Use this fixed order:

```text
selected design.md -> A structural spec
each reference image -> U/C/M attribute specs + exclusions
A spec + selected U spec + selected C spec + selected M spec -> compiled mix spec
compiled mix spec + locked Web/mobile template -> original UI atmosphere image
```

- `design.md` is required. It controls typography, hierarchy, spacing, shape language, component character, density, and contrast behavior. Ignore its named colors and literal palette values.
- One color reference is required in standard mode. Its extracted `C-spec` controls the entire run's hue family, lightness, saturation, color relationships, and color-material feeling. Do not copy its imagery or layout.
- Additional references are optional. Extract only their permitted U/C/M attributes for this run; they can contribute a product domain, information grammar, imagery feeling, a chart, or a component idea without entering final generation as raw images.
- A final output template is required. It fixes device, canvas, screen count, arrangement, and whether a phone frame is used. It is not inferred from the references.
- A Web asset contains exactly one complete Web page set on a visible light C-spec-derived background support; it is never a bare full-bleed white screenshot. Keep the page at about 75% of the canvas area, with a clear but restrained surround on all sides. The support field must use a near-white or very pale tinted neutral drawn from the C-spec's lightest relationship; never use a dark, saturated, or visually dominant outer backdrop. A mobile asset follows its selected layout template and may contain two, three, or four related screens, with phone frames or pure page panels as specified; three equal columns are only one approved option.
- For a batch, create separate image files; never join several Web pages or several mobile assets into one collage, grid, or board.
- The output is a flat UI atmosphere image, not a 3D key visual, runnable UI, or product-mockup photograph.

## Mobile layout selection

Select and record a mobile layout before analyzing references. References may suggest a visual idea, but they never override the selected template. After extracting the M-spec, lock a separate `presentation-fidelity` setting: use `high-fidelity` by default when the M reference is a polished complete design or depicts detailed, material, photographic, or refined UI treatment; use `minimal-flat` only when the M reference itself is intentionally simple, schematic, low-detail, or clearly a pure-page composition. Do not downgrade a polished reference into generic simple panels.

- `mobile-triptych-equal`: legacy/default layout; exactly three equal front-facing phone screens in three columns.
- `mobile-overlap-hero`: exactly three phone screens; a larger center hero is foregrounded while two side screens sit behind or overlap with controlled offsets.
- `mobile-staggered-cascade`: exactly four phone screens or page panels in a staggered cascade with varied scale/height; not an equal-column row.
- `mobile-editorial-collage`: two to four phones and/or cropped screen panels in a deliberate editorial board composition with varied sizes and partial crops.
- `mobile-paired-contrast`: exactly two related screens in a paired composition, useful for light/dark, before/after, or calm/expressive contrast.
- `mobile-pure-panels`: two to four screen panels with no phone hardware; use when the requested reference is a pure-page or UI-board presentation.

When only one mobile output is requested and the user does not specify a layout, use `mobile-triptych-equal` for compatibility. When multiple mobile outputs are requested, randomly choose approved layouts without repetition within the current batch, record the chosen layout and `presentation-fidelity` per output/Mix, and do not invent a new arrangement. In the controlled six-image batch, assign three different approved mobile layouts to Mix 01–03 by default; the user may explicitly lock one layout across all three if they want a like-for-like role comparison. A layout may be selected from the approved template set even when the reference image itself uses another layout.

## Inputs

Collect only what is missing:

1. **Selected `design.md`**: choose an approved reusable structural style spec. If none exists, create and approve one in a separate style-extraction task before generation.
2. **Color reference**: in standard mode, choose one supplied visual reference whose extracted `C-spec` is the palette master. If several references carry conflicting palettes and the user did not identify one, ask which should own color rather than guessing.
3. **Additional references or authorized URLs**: accept zero or more. Extract their bounded U/C/M attributes; do not let them replace the selected design structure or color source.
4. **Brief**: record the target product category, specific user, task, page state, primary action, and the proposed content-integration logic. When the selected M reference contains a person, object, material, or scene, record its role relative to text and information hierarchy; when it does not, do not invent one. Never leave the page as a generic category-only dashboard.
5. **Output device**: Web or mobile. Select the matching locked template unless the user explicitly asks for an approved extension.
6. **Count**: default to one draft when the user asks to try a direction. For more than one, generate one distinct file per requested page/state.

## Generation modes

### Standard mode

Use standard mode only when the user explicitly assigns the role of every reference used in the run—at minimum a structural master, a palette master, and each supplemental reference's allowed contribution—and asks for one device or a small directed batch. Do not infer or permanently retain reference roles. If roles are not explicit, ask the user to assign them, or use controlled combination batch mode when the user requests combinations.

### Controlled combination batch mode

Use this mode when the user asks for controlled combinations, random reference mixing, or a fixed six-image Web/mobile batch.

1. Randomly select structural master `A` from all eligible `design.md` files. `A` may be selected again in a later batch; use its original path plus content hash as its stable source ID.
2. Select three eligible references and snapshot them in the run as `R1`, `R2`, and `R3`. Require all four source IDs to differ: `R1`, `R2`, and `R3` must differ from one another and none may equal `A`. Do not require permanent manual UI/color/mood classification.
3. Assign three functional slots:
   - `U`: UI organization, including navigation, card grouping, component arrangement, and information flow
   - `C`: the only color and material master
   - `M`: product content, imagery feeling, atmosphere, and content-integration logic—whether real-world content is present, its type and subject when present, plus its relationship to text, crop, layer order, prominence, UI role, and attention/emotion
4. Before assigning a mix, create a per-reference `U-spec`, `C-spec`, and `M-spec` for `R1`–`R3` in `reference-specs.md`. Each spec must contain observable, prompt-ready attributes and exclusions: `U-spec` covers hierarchy, information order, navigation/control grammar, component relationships, density, and state flow; `C-spec` covers hue/lightness/saturation relationships, color distribution, materials, borders, shadows, and foreground/background contrast; `M-spec` covers product subject, concrete content motif, imagery role, real-world-content presence or absence, and its integration with type, crop, layer order, focal behavior, and attention/emotion. Do not use vague overall-style adjectives as a substitute for these fields.
5. Randomly select one balanced permutation group; do not choose any arbitrary three of the six permutations:
   - Group A: `U1-C2-M3`, `U2-C3-M1`, `U3-C1-M2`
   - Group B: `U1-C3-M2`, `U3-C2-M1`, `U2-C1-M3`
6. Read or create `inspiration-runs/combination-history.md`. Use `A`'s source ID plus the stable-ID-sorted set of `R1`, `R2`, and `R3` as a combination signature. If the signature already exists, redraw `R1`–`R3`; even when `A` is selected again, never pair it with the same U/C/M source set again. If no unused combination remains, require additional references or explicit user-authorized reuse.
7. Lock the selected group only for the current run. Across its three mixes, every reference must occupy every role exactly once. Before generation, validate every mix has four distinct source IDs for `A`, `U`, `C`, and `M`; if a collision occurs, redraw candidate sources or the permutation and never generate with the collision. After locking, append `A`, the U/C/M source set, permutation group, and run slug to `combination-history.md`.
8. Compile one `A-spec + U-spec + C-spec + M-spec` record per mix in `mix-specs.md`. State the governing priority and exclusions. The final image-generation request may consume this compiled record only; raw `R1`–`R3` images remain analysis evidence unless the user explicitly asks otherwise.
9. For every mix, generate one Web asset and one Mobile asset using its assigned mobile layout. The run must produce exactly six separate image files. Assign three different approved mobile layouts to Mix 01–03 without repetition and record them in `mix-plan.md` (unless the user explicitly locks one layout for comparison).

Apply these resolution rules only inside the current mix of the current batch; they are not persistent preferences for later tasks. Resolve structural conflicts by output template, then `A-spec`, then that mix's `U-spec`. Resolve every visible color and material conflict only through that mix's `C-spec`; ignore colors from `A-spec`, `U-spec`, and `M-spec`. Let `M-spec` supply content and atmosphere without changing the locked structure or palette. Keep `A` as the structural master only within this batch; rotate `U`, `C`, and `M` across its three mixes according to the selected permutation. At the start of a later batch, `A` may be selected again, but select `R1`–`R3` and assign roles again while avoiding every recorded A + U/C/M combination; do not carry this run's selections or roles forward unless the user explicitly selects reuse.

## Naturalism and anti-template constraints

Apply these during reference analysis and prompt writing. They are generation constraints, not an expanded review workflow.

- First identify the selected M reference's content-integration logic. Record whether it has no real-world content, a person, an object/material/product, or an environment/scene; then record how it sits with typography and information: adjacent, behind, intersecting/overlaid, framed in a module, full-bleed, repeated, cropped, or absent.
- When real-world content is present in the M reference, render an original equivalent—not its source subject or photograph—and preserve its **relationship** to text and hierarchy. Match meaningful visual weight to the reference logic: an editorial crop can share the lead with a headline, a content-module image can support surrounding metadata, and a background scene can stay subordinate. Never detach it into an isolated hero merely because it is present.
- When the M reference contains no person, object, material, or scene, keep the output content-led through typography, data, product UI, or graphic material; do not add real-world imagery as a substitute.
- Never copy a source person, object, or photograph. Render a new generic subject only when the compiled M-spec calls for real-world content, or use a separate asset only when the user explicitly owns or authorizes it for output.
- Ground every page in a concrete user, task, page state, and primary action. Use plausible domain content instead of an interchangeable landing page or dashboard.
- Use meaningful content evidence: varied title and body lengths, dates, locations, quantities, captions, progress, and status labels when relevant. Avoid filler such as repeated `Discover`, `Explore`, and `Get Started` copy.
- Never make oversized generic buttons, simple SVG illustrations, symbolic icons, avatars, gradient blocks, or purposeless 3D objects the primary visual content; they create a simplified AI-looking result. Specific content, information hierarchy, typography, data, and functional UI organization must follow the compiled M-spec rather than compete with or replace its content logic.
- Use a restrained component budget per visible screen unless the brief or structural master clearly requires more: one filled primary action, at most one prominent secondary action, no more than four icon-only controls above the fold, and no decorative icon grid.
- Do not put every content group inside a rounded card. When a page has multiple sections, organize at least one major region without a card by using typography, spacing, dividers, image crops, or sectional backgrounds. Reserve pills for statuses, filters, or compact categories.
- Prefer purposeful editorial crops, natural actions, tangible material detail, and contextual environments over isolated stock-style portraits or generic scenic wallpaper.
- Avoid unrequested AI-default styling: centered hero plus two pill buttons plus three equal cards, uniform large corner radii, purple-blue glow gradients, floating glass panels, excessive symmetry, and decoration that has no product function.
- Use asymmetry, varied information density, full-bleed or editorial imagery, card-free regions, and realistic content hierarchy only when they support the selected `design.md`, reference evidence, and page task. Do not add random irregularity for its own sake.

## Boundary and originality

- Treat every reference as analysis evidence, never as an output asset. Do not provide a raw reference image to the final image generator by default: extract its U/C/M specs first and generate only from the compiled mix spec. Allow direct image conditioning only when the user explicitly asks for it, and record that exception.
- Do not copy logos, brand names, source copy, real product images, merchant/payment marks, or a distinctive full layout. The mobile template may use the requested iPhone 14 Pro front presentation, but never show an Apple logo, Apple system copy, or a product back/camera module.
- Separate observed reference traits from proposed run-specific additions.
- Render generic or abstract microcopy unless the user supplies text they are authorized to use.
- Do not make claims about health, finance, or product performance in concept imagery.

## Workflow

### 1. Start a generation run

Create `inspiration-runs/<slug>/`. In controlled combination batch mode, use `inspiration-runs/combination-history.md` as the cross-batch combination log; append only `A`'s stable source ID, the stable-ID-sorted U/C/M source set, permutation group, and run slug. After locking `A`, copy the selected `design.md` into `selected-design.md` as a read-only snapshot; do not mutate the source spec.

In standard mode, create `reference-notes.md` and `reference-specs.md`. Mark the selected color reference, then extract its `C-spec` (palette, color relationships, material feeling, and exclusions); extract only permitted U/C/M attributes from every other reference. For every spec, record its source, observable prompt-ready attributes, intended contribution, exclusions, and content-integration logic: real-world-content presence or absence; type and subject when present; relationship to type, crop, layering, UI role, and visual weight. Classify contributions internally; do not require the user to classify images manually.

In controlled combination batch mode, use `selected-design.md` as `A`. Create `input/` with `R1`, `R2`, and `R3`, preserving each original extension. Create `reference-specs.md` before mixing: for every source, write its possible `U-spec`, `C-spec`, and `M-spec`, plus source-specific exclusions. Create one concise `mix-plan.md` that records the original source names, selected permutation group, and the `U`, `C`, and `M` assignment for all three mixes. Then create `mix-specs.md`, compiling `A-spec` with the selected U/C/M specs for each mix and stating the final priority, exclusions, and adopted content-integration logic. Every `M` assignment must explicitly record whether real-world content is present or absent and, when present, its relationship to type and layout. These are per-run working specs, not a permanent classification record for the reference images.

### 2. Lock the final output before analysis

Read [references/final-output-templates.md](references/final-output-templates.md). Create `output-spec.md` from the selected template before writing prompts.

Default templates:

- Mobile -> `mobile-triptych-equal` (legacy alias: `mobile-phone-triptych`)
- Web -> `web-flat-single`

The output spec must explicitly state the locked presentation: `pages-per-image: 1` and `background-support: required` for Web; for Mobile, record each output/Mix's `mobile-layout`, `presentation-fidelity`, template-defined `screens-per-image`, `mobile-arrangement`, and whether `device-frame` and `dynamic-island` are required. For Web, state the light C-spec-derived backdrop relationship, page-to-backdrop boundary, and restrained outer breathing room; lock the page to about 75% of canvas area and the background to a near-white or very pale tinted neutral only. For high-fidelity mobile, use polished, legible screen rendering and require consistent front phone frames whenever the selected template permits them; for `minimal-flat`, use plain, legible panels with no simulated hardware. Record `view`, `perspective`, `rotation`, and `3d-props` according to each template. Never let source imagery change these locked properties.

In controlled combination batch mode, lock `web-flat-single` and the three assigned mobile layouts in the same `output-spec.md` before writing any of the six prompts.

### 3. Extract and compile reference specs

In standard mode, create `style-mix.md` and `mix-specs.md` with these sections:

- **Structural master direction**: the non-negotiable typography, hierarchy, spacing, shape, and component rules drawn from `selected-design.md`; omit its literal colors
- **Color master direction**: the selected reference's extracted `C-spec`, including palette relationships and material rules
- **Reference contributions**: only the bounded U/C/M spec attributes each reference may add
- **Run content**: product category, specific user, task, required page state, primary action, realistic content evidence, and the adopted content-integration logic
- **Exclusions**: source-specific content and all prohibited brand/copyright elements

Resolve layout conflicts in favor of the output template, then `selected-design.md`, then the brief. Resolve every color conflict in favor of the selected `C-spec`. Compile the resolved A/U/C/M fields into `mix-specs.md`. If a reference conflicts with a required structure rule, retain only its compatible spec attribute or exclude it.

In controlled combination batch mode, use `reference-specs.md` and `mix-plan.md` to compile `mix-specs.md`. For each mix, map the assigned source's `U-spec`, `C-spec`, and `M-spec` into one resolved record with its A structural spec, priority order, brief, scene decision, and exclusions. Do not pass raw references into final generation; write one prompt section per mix and device from `mix-specs.md`.

### 4. Generate the locked output

Create `prompts.md`. Require the image model to render one selected output template exactly.

For every prompt, state:

- original UI atmosphere image, no runnable implementation
- selected device and exact canvas
- for Web: exactly one complete page, placed on a visible full-canvas **near-white or very pale tinted neutral** supporting background derived from the selected `C-spec`'s lightest relationship, with a clear page-to-backdrop boundary and restrained outer breathing room. Keep the page at about 75% of canvas area; never use a dark or saturated outer backdrop, a bare full-bleed white screenshot, collage, multi-screen sheet, grid, triptych, or side-by-side comparison
- for mobile: obey the selected mobile layout and `presentation-fidelity` exactly. Do not force three equal columns unless `mobile-triptych-equal` is locked; do not add screens, panels, or phone frames beyond the template count. Use polished high-fidelity screens and consistent permitted phone frames for `high-fidelity`; use simple, plain panels only for `minimal-flat`.
- for phone-based mobile layouts: require a high-fidelity front phone frame only when the template says so; Dynamic Island, bezel, glass reflection, shadow, and limited rotation/perspective are template-controlled, not global requirements. Never show an Apple logo, Apple system copy, product back, or camera module.
- for pure-page or editorial layouts: keep screens legible as flat UI panels; no unrequested phone hardware, studio environment, floating props, or external 3D objects.
- use only the resolved A/U/C/M fields in `mix-specs.md`: output template first, A structural spec second, selected U spec third for structure; selected C spec alone for visible color/material; selected M spec for content and atmosphere
- do not attach, embed, or otherwise pass raw reference images to the final image-generation request unless the user explicitly asks for direct image conditioning
- trace every major visual decision to a compiled A/U/C/M field or the brief; do not fill gaps with generic gradients, glass panels, 3D objects, phone triptychs, or other model-default imagery
- no literal color names, hex values, or palette instructions inherited from `design.md`
- the concrete user, task, requested page state, primary action, and plausible non-brand content
- the adopted content-integration logic: whether real-world content is absent or present; when present, its type, new generic subject/material or scene, lighting, crop, relationship to typography and information hierarchy, layer order, prominence, UI role, and prohibited avatar/icon/illustration/gradient/3D substitutions
- the restrained component budget and card-free organization rules from **Naturalism and anti-template constraints**
- explicit exclusion of unrequested centered-hero/two-pill/three-card formulas, generic glow gradients, floating glass panels, and purposeless decoration
- prohibited source brands, source copy, logos, payment marks, watermarks, and copied layouts

Generate the requested number of drafts. Save each page as a separate stable filename under `output/`.

For controlled combination batch mode, store the files by mix and assign these stable review numbers:

- `1` = Mix 01 Web
- `2` = Mix 02 Web
- `3` = Mix 03 Web
- `4` = Mix 01 Mobile
- `5` = Mix 02 Mobile
- `6` = Mix 03 Mobile

Use filenames that preserve the number, mix, roles, and device, for example `01-mix-01-U1-C2-M3-web.png` and `04-mix-01-U1-C2-M3-mobile.png`. Never renumber a run after showing it to the user.

### 5. Review and hand off

Create `review.md` with the selected design spec, output template, references used, each file, its status, and proposed OPS tags. Every retained image must also have a dedicated blended-reference prompt bound to it in the upload handoff.

Reject or regenerate a Web image when it has more than one page, the page materially departs from about 75% of the canvas area, or it lacks its required near-white/light C-spec-derived supporting backdrop, clear page boundary, and restrained outer breathing room. Reject any Web output with a dark, saturated, or dominant outer backdrop. Reject or regenerate a mobile image when its screen count, arrangement, required fidelity, frame requirement, or allowed rotation/perspective differs from the selected template. Also reject an output when it inserts real-world content that the compiled M-spec marked absent, copies source content, or turns a reference-integrated person/object/scene into an unrelated isolated hero. Reject output with Apple marks or system copy, unrequested hardware or 3D props, a failed locked canvas, literal colors from `design.md` instead of the selected color reference, recognizable source elements, third-party brands, unreadable screens, or lost UI hierarchy.

Prepare only a review-ready package. Keep all OPS records disabled until an operator explicitly uploads, reviews, and enables them.

### 6. Number, select, and classify the upload materials

After a controlled combination batch passes review:

1. Show all six images in Codex in numeric order with their number, device, mix, and role assignment. End with: `回复编号即可保留，例如 134 或 234保留。`
2. Treat a reply containing only unique digits `1` through `6`, with optional separators or the word `保留`, as the selection for the most recent unresolved six-image run. Interpret `134` as images `1`, `3`, and `4`. Ask for clarification if the reply contains another number or could refer to a different run.
3. Copy selected files; do not move them out of the run and do not delete unselected files.
4. Use an existing user-specified upload-library path when provided. Otherwise create this lightweight workspace library:

   ```text
   upload-materials/
     web/
     mobile/
   ```

5. Copy selected items `1` through `3` into `upload-materials/web/`. Copy selected items `4` through `6` into `upload-materials/mobile/`. Classify by the locked output device, never by visual inference.
6. Prefix every copied filename with the run slug and keep the review number so files from different runs never overwrite one another.
7. Create one binding record in `upload-manifest.json` for every selected image. Inspect the final image, then write a dedicated `reference_prompt` from that image's compiled intent in `mix-specs.md`, `prompts.md`, `style-mix.md` or `mix-plan.md`, `output-spec.md`, and its verified visual traits. Do not merely reverse-engineer the image again or use a generic `Refer to this image` prompt.
8. Every `reference_prompt` must state what the image should contribute for structure, color, content/atmosphere, and information hierarchy; retain only the design judgments actually adopted in the run; state which source brands, copy, and layouts must not be copied; and end with: `Use this prompt together with the image content as blended visual references.`
9. Every `upload-manifest.json` item must contain at least `review_number`, `image_path`, `device`, `mix`, `role_assignment`, `reference_prompt`, `selected-for-upload`, and `ops_payload`. `ops_payload` must bind that exact image to that exact `reference_prompt` for later automation to fill both the OPS image field and `Prompt / 特征` field. Never upload an image alone and ask a model to infer its prompt at upload time.
10. Update the existing `review.md` with selected numbers, copied destinations, a `reference_prompt` summary, and `selected-for-upload` status. `upload-manifest.json` is an upload handoff, not a second selection catalog or material library.
11. Confirm retained numbers, their registered dedicated prompts, and clickable Web/mobile folder paths. This confirms local classification and handoff only; it is not an OPS upload or publication receipt.

## Output contract

```text
inspiration-runs/
  combination-history.md          # A + U/C/M combination history for controlled combination batches
  <slug>/
    selected-design.md
    input/                  # controlled combination mode only
    reference-notes.md      # standard mode only
    reference-specs.md      # per-reference U/C/M extraction; sources are analysis evidence
    mix-plan.md             # controlled combination mode only
    mix-specs.md            # resolved A + U + C + M spec per output/mix
    output-spec.md
    style-mix.md            # standard mode only
    prompts.md
    output/
    review.md
    upload-manifest.json   # upload handoff binding retained images to blended-reference prompts

upload-materials/
  web/
  mobile/
```

Use `design.md` as a reusable library object. Use the remaining files as a per-run audit trail. Never silently turn a reference set into a new global design spec.
