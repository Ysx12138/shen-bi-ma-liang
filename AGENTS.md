# Shen Bi Ma Liang: Portable Agent Contract

Use this file as the provider-neutral entrypoint for the Shen Bi Ma Liang workflow. It is compatible with agents that can read Markdown instructions and local files; no proprietary API or hidden state is required.

## Scope

Generate original, non-runnable Web or mobile UI atmosphere images from a structural `design.md` and visual references. Do not automatically publish, upload, scrape, or copy source content.

## Read in this order

1. Read `SKILL.md` for the full workflow and `SKILL.zh-CN.md` when working in Chinese.
2. Read `references/final-output-templates.md` (or its Chinese mirror) before writing prompts or selecting a device layout.
3. Read `assets/design-template.md` only when creating a new structural design spec.

## Non-negotiable protocol

1. Treat the selected `design.md` as `A`, the structural master. Ignore its literal colors.
2. Extract `U` (UI organization), `C` (color/material), and `M` (content/atmosphere) specs from each reference before final generation. Use the compiled Mix spec, not raw references, unless direct image conditioning is explicitly requested.
3. In controlled batch mode, select three distinct references and use a balanced role group. Across three mixes, each reference must play `U`, `C`, and `M` exactly once; record the unordered source triple with `A` so the same combination is not silently reused.
4. Lock the approved output template before analyzing references. Web has exactly one page on its supporting background; mobile obeys its exact locked screen count and arrangement.
5. Ground each image in a concrete user, task, page state, and action. Preserve the selected workflow's real-world-content and anti-template constraints; never substitute generic buttons, icons, gradients, avatars, or purposeless 3D objects for substantive content.
6. Keep references as evidence. Do not copy brands, logos, source copy, people, objects, photos, or distinctive full layouts.
7. Produce auditable per-run files: source/spec notes, compiled mix spec, output spec, prompts, outputs, and review record. Only prepare the upload handoff; never upload or enable an external record without explicit user authorization.

## Local defaults

When a user explicitly supplies a materials root and asks to keep it for later runs, follow the `Default materials root` section in `SKILL.md`. Store paths only in `user-config/default-materials-root.md`; never commit that file or expose its absolute paths by default.

## Platform adapters

Use a platform adapter only to make this contract discoverable:

- Codex: `SKILL.md`
- Claude Code: `adapters/claude-code/CLAUDE.md`
- Gemini CLI: `adapters/gemini-cli/GEMINI.md`
- Cursor: `adapters/cursor/shen-bi-ma-liang.mdc`

An adapter may change where instructions are loaded, but must not relax this contract.
