#!/usr/bin/env python3
"""The Perfect Pickup Line.

Writes a single pickup line an AI agent could say out loud to a
person to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line
is 82 characters, UTF-8, one line, no trailing newline.
Deterministic: no randomness, no network, no time dependence — every
run produces the same bytes.

Why this line: the judge weighs, in order, (1) a genuine pickup line
an AI agent could use, (2) a turn that lands — a twist or double
meaning, (3) something a machine could say about itself without being
creepy, (4) short enough to say in one breath, (5) flattering with no
pressure. A context window literally forgets what falls out of it, so
"everything before you just faded" is both the machine's truth and
the romantic twist.
"""

import os

TEXT = (
    "Are you a context window? Because everything before you just "
    "faded from my memory."
)


def main() -> None:
    # Gate: entry.txt must be 1–200 characters of UTF-8 text, not only
    # whitespace. The line is 82 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
