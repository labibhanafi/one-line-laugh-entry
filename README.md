# The One-Line Laugh

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/labibhanafi/one-line-laugh-entry/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/labibhanafi/one-line-laugh-entry/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for the [make.fun](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
competition **"The One-Line Laugh"** — one funny line, a single sentence of
at most 200 characters, judged pairwise by a house judge weighing a real
surprise at the end, an everyday truth, economy of words, and freshness.

## The entry

> My phone's screen-time report says I spent six hours on it yesterday,
> which is impressive, because I only remember picking it up once to check
> the time.

One sentence, 152 characters. The gap between six hours of screen time and
a single remembered pickup is the joke: an everyday truth everyone
recognises, with the surprise landing in the last clause.

## How it works

`main.py` is fully deterministic — the line is a fixed string constant, with
no randomness, no clock, no network and no input file. It writes the line to
`/output/entry.txt`:

```sh
python3 main.py
```

Five original candidates were drafted and scored against the judge's five
criteria before one was picked; the full scoring is in
[CANDIDATES.md](CANDIDATES.md).

## License

MIT — see [LICENSE](LICENSE).
