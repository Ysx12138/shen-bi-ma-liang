# Final output templates

Select a template before analyzing references. The template determines the final presentation; `design.md` determines structure, the selected color reference determines color, and the brief determines content.

## mobile-triptych-equal

- Canvas: horizontal 16:9
- Screen count: exactly three related mobile App pages, in three equal left-to-right columns
- Required sequence: entry/onboarding, primary home/task, and detail/action; adapt state labels only when the brief requires it
- Presentation: each App page appears inside a high-fidelity, front-facing iPhone 14 Pro render: polished dark-metal flat edge, fine black bezel, glass screen reflection, centered Dynamic Island, and a restrained natural grounding shadow. The three phones have equal visual weight and aligned bottoms.
- View: flat orthographic front elevation
- Lock: no fourth phone, no extra panel, no perspective, environment, floating props, collage, or external 3D objects. Require the iPhone 14 Pro front hardware presentation and Dynamic Island; never show an Apple logo, Apple system copy, a back/camera module, or any other brand mark.

`mobile-phone-triptych` remains a backwards-compatible alias for this template.

## mobile-overlap-hero

- Canvas: horizontal 16:9
- Screen count: exactly three related mobile App pages
- Presentation: one larger center phone/screen is the visual hero; two smaller side phones sit behind it with controlled overlap and offset. Use high-fidelity iPhone 14 Pro fronts, centered Dynamic Islands, aligned visual language, and readable UI.
- View: controlled composition; limited rotation and depth overlap allowed, with no extreme perspective
- Lock: no fourth screen, unrelated props, product backs, camera modules, logos, source copy, or random collage elements.

## mobile-staggered-cascade

- Canvas: horizontal 16:9
- Screen count: exactly four related mobile screens or phone renders
- Presentation: staggered cascade with varied scale, height, and vertical position; the four items must read as one intentional sequence, not equal columns. Phone frames are optional; if used, use consistent front-facing iPhone 14 Pro frames.
- View: controlled composition; limited rotation allowed
- Lock: no fifth screen, no arbitrary overlap that hides UI, no external 3D props, logos, or copied source layout.

## mobile-editorial-collage

- Canvas: horizontal 16:9
- Screen count: two to four related phones and/or cropped screen panels
- Presentation: deliberate editorial board composition with varied sizes, partial crops, and clear hierarchy. Phone hardware is optional; flat UI panels are valid. Keep every retained panel legible enough to communicate its state.
- View: controlled flat collage; limited overlap allowed
- Lock: this is not a random moodboard. Do not add unrelated photos, decorative devices, external props, logos, watermarks, or source-specific copy.

## mobile-paired-contrast

- Canvas: horizontal 16:9
- Screen count: exactly two related screens
- Presentation: paired side-by-side or slightly offset composition with an intentional contrast, such as light/dark, before/after, or calm/expressive. Phone frames are optional and must be consistent if present.
- View: flat or limited controlled offset
- Lock: no third screen, random collage, unrequested hardware, external 3D props, logos, or copied source elements.

## mobile-pure-panels

- Canvas: horizontal 16:9
- Screen count: two to four related mobile page panels
- Presentation: pure UI pages with no phone hardware, no bezel, and no Dynamic Island. Use a clean board or page strip with consistent panel sizing unless the brief explicitly selects another approved composition.
- View: flat orthographic
- Lock: do not add phone frames, device shadows, product photography, perspective, external props, logos, or source copy.

## web-flat-single

- Canvas: horizontal 16:9
- Page count: exactly one complete Web page
- Backdrop: required. Place the page on a visible, full-canvas near-white or very pale tinted-neutral supporting field selected from the lightest relationship in the `C-spec`; keep a clear page-to-backdrop boundary with restrained outer breathing room. Keep the page at about 75% of total canvas area. Never use a dark or saturated outer backdrop, and do not collapse the support field into the same white as the page.
- View: flat orthographic front elevation
- Lock: no browser perspective, studio environment, floating props, multi-page collage, grid, or external 3D objects. Never render the Web page as a bare full-bleed white screenshot with no supporting backdrop.

## Output spec format

```text
template: <template id>
canvas: <ratio>
device: <mobile|web>
pages-per-image: <1 for web>
background-support: <required C-spec-derived backdrop for web; otherwise n/a>
page-area: <web: about 75% of canvas; otherwise n/a>
mobile-layout: <selected mobile template id, for mobile only>
presentation-fidelity: <high-fidelity|minimal-flat, for mobile only>
screens-per-image: <template-defined count or range>
mobile-arrangement: <template-defined arrangement>
page-state: <web state or mobile states>
device-frame: <required|optional|off>
dynamic-island: <required|optional|off>
view: <front-facing|controlled-composition>
perspective: <off|limited-by-template>
rotation: <off|limited-by-template>
3d-props: off
```
