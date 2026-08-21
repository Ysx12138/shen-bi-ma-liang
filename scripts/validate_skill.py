#!/usr/bin/env python3
"""Validate the repository's portable, agent-agnostic workflow contract."""

from __future__ import annotations

import re
import json
from pathlib import Path


REQUIRED_FILES = (
    "AGENTS.md",
    "SKILL.md",
    "SKILL.zh-CN.md",
    "agents/openai.yaml",
    "assets/design-template.md",
    "references/final-output-templates.md",
    "references/final-output-templates.zh-CN.md",
    "providers/image-provider-presets.json",
    "scripts/configure_image_provider.py",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def validate_frontmatter(skill_file: Path) -> None:
    content = skill_file.read_text(encoding="utf-8")
    if content.lstrip("\ufeff").splitlines()[0:1] != ["---"]:
        fail(f"{skill_file.name} must start with YAML frontmatter")
    closing = content.find("\n---\n", 4)
    if closing == -1:
        fail(f"{skill_file.name} has unclosed YAML frontmatter")
    frontmatter = content[4:closing]
    if not re.search(r"^name: style-inspiration-cards$", frontmatter, re.MULTILINE):
        fail(f"{skill_file.name} must declare name: style-inspiration-cards")
    if not re.search(r"^description: .+", frontmatter, re.MULTILINE):
        fail(f"{skill_file.name} must declare a description")


def validate_relative_markdown_links(root: Path) -> None:
    link_pattern = re.compile(r"!?\[[^]]*\]\(([^)]+)\)")
    for markdown_file in root.rglob("*.md"):
        if ".git" in markdown_file.parts:
            continue
        content = markdown_file.read_text(encoding="utf-8")
        for target in link_pattern.findall(content):
            target = target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith(("mailto:", "/", "#")):
                continue
            if not (markdown_file.parent / target).exists():
                fail(f"broken relative link in {markdown_file.relative_to(root)}: {target}")


def validate_provider_presets(root: Path) -> None:
    catalog_path = root / "providers" / "image-provider-presets.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    if catalog.get("schema_version") != 1:
        fail("provider preset catalog must declare schema_version 1")
    presets = catalog.get("presets")
    if not isinstance(presets, dict) or not presets:
        fail("provider preset catalog must contain at least one preset")
    for provider_id, preset in presets.items():
        if not isinstance(preset, dict):
            fail(f"provider preset {provider_id} must be an object")
        for key in ("display_name", "execution", "requires_model", "notes"):
            if key not in preset:
                fail(f"provider preset {provider_id} is missing {key}")


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    for relative_path in REQUIRED_FILES:
        if not (root / relative_path).is_file():
            fail(f"missing required file: {relative_path}")
    for relative_path in (
        "adapters/claude-code/CLAUDE.md",
        "adapters/gemini-cli/GEMINI.md",
        "adapters/cursor/shen-bi-ma-liang.mdc",
    ):
        if not (root / relative_path).is_file():
            fail(f"missing required agent adapter: {relative_path}")
    validate_frontmatter(root / "SKILL.md")
    validate_provider_presets(root)
    validate_relative_markdown_links(root)
    print("Skill repository validation passed.")


if __name__ == "__main__":
    main()
