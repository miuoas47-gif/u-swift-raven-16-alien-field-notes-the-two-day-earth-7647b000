#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of planet Earth --
to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

Stdlib only. No network, no arguments. Deterministic: the same bytes
every run.
"""

import os
import sys

LINE = (
    "Four stars: a lovely blue planet whose locals invented two days "
    "of rest a week, then spent them feeling guilty about it."
)


def validate(line: str) -> str | None:
    """Return an error message if line breaks the competition gate."""
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    if not 1 <= len(line) <= 200:
        return f"entry must be 1-200 characters, got {len(line)}"
    if not line.strip():
        return "entry must not be only whitespace"
    return None


def main() -> int:
    # Validate the line against the competition gate before writing.
    error = validate(LINE)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read back and verify the file holds exactly the validated line,
    # and that what was written still passes the gate.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE or validate(written) is not None:
        print("error: read-back verification failed", file=sys.stderr)
        return 1

    print(f"Wrote {path} ({len(LINE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
