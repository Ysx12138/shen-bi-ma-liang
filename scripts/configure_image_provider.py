#!/usr/bin/env python3
"""Create a local, credential-free image-provider routing record."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
PRESETS_PATH = ROOT / "providers" / "image-provider-presets.json"
DEFAULT_CONFIG_PATH = ROOT / "user-config" / "image-generation-provider.json"


def load_presets() -> dict[str, dict[str, Any]]:
    catalog = json.loads(PRESETS_PATH.read_text(encoding="utf-8"))
    presets = catalog.get("presets")
    if not isinstance(presets, dict):
        raise ValueError("preset catalog must contain an object named presets")
    return presets


def config_path(value: str | None) -> Path:
    return Path(value).expanduser().resolve() if value else DEFAULT_CONFIG_PATH


def print_presets(presets: dict[str, dict[str, Any]]) -> None:
    for provider_id, preset in presets.items():
        needs_model = "model required" if preset.get("requires_model") else "model supplied by host"
        print(f"{provider_id}: {preset['display_name']} ({needs_model})")


def command_use(args: argparse.Namespace, presets: dict[str, dict[str, Any]]) -> None:
    preset = presets.get(args.provider)
    if preset is None:
        raise ValueError(f"unknown provider: {args.provider}")
    if preset.get("requires_model") and not args.model:
        raise ValueError(f"{args.provider} requires --model <current-model-id>")

    record = {
        "schema_version": 1,
        "provider_id": args.provider,
        "display_name": preset["display_name"],
        "execution": preset["execution"],
        "model": args.model,
        "api_key_env": args.api_key_env or preset.get("api_key_env"),
        "base_url_env": args.base_url_env or preset.get("base_url_env"),
        "base_url": args.base_url,
        "notes": preset["notes"],
    }
    destination = config_path(args.config)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Configured {args.provider} at {destination}")
    print("No credential was stored; set the configured environment variable in the execution environment.")


def command_show(args: argparse.Namespace) -> None:
    destination = config_path(args.config)
    if not destination.exists():
        print(f"No provider configuration at {destination}")
        return
    print(destination.read_text(encoding="utf-8"), end="")


def command_clear(args: argparse.Namespace) -> None:
    destination = config_path(args.config)
    if destination.exists():
        destination.unlink()
        print(f"Cleared provider configuration at {destination}")
    else:
        print(f"No provider configuration at {destination}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", help="override the local configuration file path")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="list available provider presets")
    use = commands.add_parser("use", help="select a provider preset")
    use.add_argument("provider", help="provider ID from the list command")
    use.add_argument("--model", help="current image model, endpoint, or local workflow ID")
    use.add_argument("--base-url", help="explicit provider or local endpoint URL")
    use.add_argument("--api-key-env", help="override the credential environment-variable name")
    use.add_argument("--base-url-env", help="override the endpoint environment-variable name")
    commands.add_parser("show", help="print the current local configuration")
    commands.add_parser("clear", help="remove the current local configuration")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "list":
            print_presets(load_presets())
        elif args.command == "use":
            command_use(args, load_presets())
        elif args.command == "show":
            command_show(args)
        else:
            command_clear(args)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
