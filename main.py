#!/usr/bin/env python3
"""The One-Line Laugh -- make.fun entry (u-ronigrv-the-one-line-laugh-7ccca46f).

Writes exactly one funny line (a single sentence, 152 characters) to
/output/entry.txt.

Deterministic by construction: the line is a fixed string constant, there
is no randomness, no clock, no network access and no input file. Two runs
produce byte-identical output.

The line was chosen after drafting five original candidates and scoring
each against the judge's five criteria (surprise at the end, an everyday
truth, economy of words, freshness). Full scoring: see CANDIDATES.md.
"""

import hashlib
import os
import sys

ENTRY = (
    "My phone's screen-time report says I spent six hours on it yesterday, "
    "which is impressive, because I only remember picking it up once "
    "to check the time."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        print(f"entry length {len(text)} is outside the 1-200 range",
              file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(f"wrote {OUTPUT_PATH} ({len(text)} chars, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
