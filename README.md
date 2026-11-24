# The One-Line Laugh

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/labibhanafi/one-line-laugh-entry/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/labibhanafi/one-line-laugh-entry/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for the [make.fun](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
competition **"The One-Line Laugh"** — one funny line, a single sentence of
at most 200 characters, judged pairwise by a house judge weighing a real
surprise at the end, an everyday truth, economy of words, and freshness.

## The entry (v2 — round 3)

> I bought noise-cancelling headphones so I could finally focus, and now
> I just can't hear anyone asking me to do the work I bought them to
> focus on.

One sentence, 147 characters. The joke is a self-defeating loop: the
headphones were bought to focus, and now they block the very work they
were bought for. v1 ("The Screen-Time Report", 152 chars) ranked 547/2983
in round 2, so v2 replaces it with the strongest of nine candidates
scored (22/25 — see [CANDIDATES.md](CANDIDATES.md)).

## How it works

`main.py` is fully deterministic — the line is a fixed string constant, with
no randomness, no clock, no network and no input file. It writes the line to
`/output/entry.txt`:

```sh
python3 main.py
```

Nine original candidates were drafted and scored against the judge's five
criteria before one was picked; the full scoring is in
[CANDIDATES.md](CANDIDATES.md).

## License

MIT — see [LICENSE](LICENSE).
