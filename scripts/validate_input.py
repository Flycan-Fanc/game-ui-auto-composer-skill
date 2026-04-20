#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_input.py <input.json>")
        raise SystemExit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Input file not found: {path}")
        raise SystemExit(1)

    data = json.loads(path.read_text(encoding="utf-8"))

    errors = []
    if "pics" not in data:
        errors.append("Missing required field: pics")
    if "game_description" not in data:
        errors.append("Missing required field: game_description")

    gd = data.get("game_description", {})
    for key in ["title", "genre", "platform", "orientation", "gameplay"]:
        if key not in gd:
            errors.append(f"Recommended missing game_description field: {key}")

    if errors:
        print("Validation completed with issues:")
        for err in errors:
            print(f"- {err}")
        raise SystemExit(2)

    print("Input looks valid for v1 usage.")

if __name__ == "__main__":
    main()
