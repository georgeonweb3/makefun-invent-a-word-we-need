#!/usr/bin/env python3
"""Invent a Word We Need - make.fun entry.

Coins one new English word and defines it in a single line, then writes
that line to /output/entry.txt as UTF-8 with no trailing newline.
"""

import os

# The entry: word + part of speech + one-line definition.
# \u2014 is the em dash, \u2019 the apostrophe in "plane's".
ENTRY = "landclapper (n.) \u2014 the passenger who applauds the moment the plane\u2019s wheels touch the runway."

OUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: one line, 1-140 characters, not only whitespace.
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit(f"entry must be 1-140 chars, got {len(ENTRY)}")

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

    # Read back and confirm the file holds exactly the entry, byte for byte.
    with open(OUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        raise SystemExit("entry.txt does not match the entry")
    print(f"wrote {len(ENTRY)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
