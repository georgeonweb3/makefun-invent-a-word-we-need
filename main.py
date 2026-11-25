#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one invented English word with its one-line definition to
/output/entry.txt: the passenger who applauds the moment the plane's
wheels touch the runway finally has a name — landclapper.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = (
    "landclapper (n.) — the passenger who applauds the moment the "
    "plane’s wheels touch the runway."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 140 characters, not only whitespace — and one line:
    # an embedded newline would split the definition and break the gate.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, gate wants 1-140"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
