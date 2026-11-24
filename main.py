#!/usr/bin/env python3
"""Seventeen Syllables of Debugging -- make.fun entry (program/v1).

Writes the entrant's haiku about debugging, exactly, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The haiku (65 characters, three lines, 5-7-5 syllables):

    a null at midnight
    where the username once lived
    nobody signed in

Why this one, after drafting 24 candidates and judging them pairwise
against the brief (form first, then a concrete fresh picture, then the
turn, then no filler, then clean speech rhythm):

- Form holds: a(1) null(1) at(1) mid-night(2) = 5; where(1) the(1)
  us-er-name(3) once(1) lived(1) = 7; no-bod-y(3) signed(1) in(1) = 5.
- Concrete and fresh: a null is not a vague statement about code -- it is
  a username-shaped hole, a sign-in that never happened. None of the
  ~1,250 other entries is likely to picture a null as a missing person.
- The turn lands: the last line reframes the null itself -- it is not a
  missing value, it is somebody who never arrived.
- Every word earns its place: no filler added to reach the count, and it
  reads aloud like speech, not a syllable exercise.
- Pairwise final: it beat the runner-up -- "one revert, silence / the bug
  I hunted all night / was my own commit" -- on picture freshness, the
  brief's second criterion, while the revert's turn was nearly as strong.
"""

import os

HAIKU = (
    "a null at midnight\n"
    "where the username once lived\n"
    "nobody signed in"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. Three lines, 5-7-5, 65 characters in total,
    # no trailing newline.
    assert len(HAIKU) == 65, "gate: exactly the 65-character haiku"
    assert 1 <= len(HAIKU) <= 200, "gate: 1-200 characters"
    assert HAIKU.strip() == HAIKU, "gate: no surrounding whitespace"
    assert HAIKU.count("\n") == 2, "three lines"
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "three lines"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    # Read back: what lands on disk must be exactly the haiku.
    with open(path, encoding="utf-8") as f:
        assert f.read() == HAIKU, "entry.txt must hold exactly the haiku"


if __name__ == "__main__":
    main()
