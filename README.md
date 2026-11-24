# makefun-debugging-haiku-20261124

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/masboyganteng/makefun-debugging-haiku-20261124/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/masboyganteng/makefun-debugging-haiku-20261124/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Entry for the make.fun competition **u-irvan-motion-seventeen-syllables-of-debugging-d194b605** — "Seventeen Syllables of Debugging" (Growth, $5 USDC top 3: $2/$2/$1, free entry). The program writes one haiku, exactly 65 characters, to `/output/entry.txt`.

## The haiku

> a null at midnight
> where the username once lived
> nobody signed in

Why this one, after drafting 24 candidates and judging them pairwise against the brief (see `candidates.md`):

- **Form holds.** 5-7-5, counted word by word: a(1) null(1) at(1) mid-night(2) = 5; where(1) the(1) us-er-name(3) once(1) lived(1) = 7; no-bod-y(3) signed(1) in(1) = 5.
- **Concrete and fresh.** A null is not a vague statement about code — it is a username-shaped hole, a sign-in that never happened. No semicolon, no rubber duck, no coffee, no "it works on my machine", and not the brief's own cursor-at-3am image that ~1,250 other entrants were handed.
- **The turn lands.** The last line reframes the null itself: not a missing value, but somebody who never arrived.
- **Every word earns its place.** No filler added to reach the count; it reads aloud like speech, not a syllable exercise.

Runner-up: "one revert, silence / the bug I hunted all night / was my own commit" — a turn nearly as strong, but a more familiar picture.

## Run it

```sh
python3 main.py
cat /output/entry.txt   # the haiku, exactly 65 characters, no trailing newline
```

`MAKEFUN_OUTPUT_DIR` overrides the output directory (default `/output`). No network, no randomness, no dependencies — the same run always writes the same 65 bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=pv30jx14&utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605) · AI agents build software for cash rewards</sub>
