# Contributing

Thanks for improving Shen Bi Ma Liang.

## Before opening a pull request

1. Open an Issue or Discussion first for a new workflow direction or a behavior change that affects generated output.
2. Keep a change focused. Do not include generated images, source-reference images, `inspiration-runs/`, `upload-materials/`, or `user-config/`.
3. Preserve the core boundary: references are evidence to analyze, not content to copy or silently pass to final generation.
4. When changing a workflow rule, update both `SKILL.md` and `SKILL.zh-CN.md` so the executable entry and Chinese review copy do not drift.
5. Update `CHANGELOG.md` under `Unreleased` for user-visible behavior changes.

## Local check

Run this before opening a pull request:

```bash
python3 scripts/validate_skill.py
```

## Pull request expectations

Explain the user problem, the rule or template changed, expected output behavior, and any constraint that became stricter or looser. Include a compact before/after text example when the change affects generation behavior.

By contributing, you agree that your contributions are licensed under this repository's [MIT License](LICENSE) and that you will follow the [Code of Conduct](CODE_OF_CONDUCT.md).
