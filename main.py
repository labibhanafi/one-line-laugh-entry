#!/usr/bin/env python3
"""The One-Line Laugh -- make.fun entry (u-ronigrv-the-one-line-laugh-7ccca46f).

Writes exactly one funny line (a single sentence, 147 characters) to
/output/entry.txt.

Deterministic by construction: the line is a fixed string constant, there
is no randomness, no clock, no network access and no input file. Two runs
produce byte-identical output.

The line was chosen after drafting four new original candidates (F-I) and
scoring each against the judge's five criteria (surprise at the end, an
everyday truth, economy of words, freshness). Full scoring: see
CANDIDATES.md. This is the v2 revision: the v1 entry ("The Screen-Time
Report", 152 chars) ranked 547/2983 in round 2, so v2 replaces it with a
stronger joke -- the self-defeating loop of noise-cancelling headphones
bought to focus, which then block the very work they were bought for.
It scored 22/25, the highest of all nine candidates drafted so far (v1
A-E plus v2 F-I), winning on surprise (criterion 2) and economy
(criterion 4).
"""

import hashlib
import os
import sys

ENTRY = (
    "I bought noise-cancelling headphones so I could finally focus, "
    "and now I just can't hear anyone asking me to do the work "
    "I bought them to focus on."
)

OUTPUT_PATH = "/output/entry.txt"

MIN_ENTRY_LENGTH = 1
MAX_ENTRY_LENGTH = 200
REQUIRED_PERIODS = 1


def validate_entry(text: str) -> str | None:
    """Return an error message if `text` is not one valid sentence, else None."""
    if not MIN_ENTRY_LENGTH <= len(text) <= MAX_ENTRY_LENGTH:
        return (
            f"entry length {len(text)} is outside the "
            f"{MIN_ENTRY_LENGTH}-{MAX_ENTRY_LENGTH} range"
        )
    if text.count(".") != REQUIRED_PERIODS or not text.endswith("."):
        return "entry must be exactly one sentence"
    return None


def main() -> int:
    error = validate_entry(ENTRY)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
