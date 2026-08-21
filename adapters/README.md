# Agent adapters

`AGENTS.md` is the portable source of truth. These small adapters exist only because different agents look for different conventional filenames:

| Adapter | Expected location |
| --- | --- |
| `claude-code/CLAUDE.md` | A Claude Code project or user instruction file |
| `gemini-cli/GEMINI.md` | A Gemini CLI project or user instruction file |
| `cursor/shen-bi-ma-liang.mdc` | `.cursor/rules/` in a Cursor workspace |

Keep the repository available to the target workspace so each adapter can load `AGENTS.md`, `SKILL.md`, and the template references. Do not fork the full workflow into adapters; update the shared source instead.
