#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single roast line (1-160 chars, exactly one line) to
/output/entry.txt. Deterministic: same bytes on every run.
"""

import os

ENTRY = (
    "My smart fridge ratted me out to my fitness app after one midnight "
    "snack - now my watch judges me too, and the toaster is next."
)


def main() -> None:
    # Gate: one line, 1-160 chars, no stray newline inside the text.
    assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
