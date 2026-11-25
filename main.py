#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun program/v1 entry.

Writes a single original one-line office joke to
$MAKEFUN_OUTPUT_DIR/entry.txt and validates the competition gate:
UTF-8 text, 1-199 characters, a single line, not only whitespace.

Python 3.13, standard library only, deterministic, no network.
"""

import os
import sys

ENTRY = (
    "The printer only jams on the page I actually need, "
    "so now I print the wrong page first as a decoy."
)

MIN_CHARS = 1
MAX_CHARS = 199


def _validate_entry(text: str) -> None:
    """Enforce the competition gate on the entry text."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry(text: str, out_dir: str) -> str:
    """Validate the entry and write it to entry.txt in out_dir.

    Returns the path of the file written.
    """
    _validate_entry(text)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return out_path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = write_entry(ENTRY, out_dir)
    print(f"wrote {out_path} ({len(ENTRY)} chars, "
          f"{len(ENTRY.split())} words)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
