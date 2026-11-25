#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

The whole internet, in a single word: feral.

Why this word: the internet is not a library, a town square, or a
toolbox — it is wild, untamed, unfiltered humanity running loose with
no zookeeper in sight. "Feral" is funny on its own, true of the
internet as a whole rather than any one app, surprising (nobody's
first reach is "feral"), and it lands in one beat: five letters,
instantly readable, spelled correctly.

Deterministic, stdlib only: the program always writes the same
five bytes to /output/entry.txt.
"""

# The entry: one word, five characters, no spaces, no punctuation.
ENTRY = "feral"

import os
import sys


def main() -> int:
    """Write the entry word to /output/entry.txt.

    The grader mounts /output, so we only ever create the directory
    (never remove it) and overwrite the file inside it.
    """
    out_dir = "/output"
    out_path = os.path.join(out_dir, "entry.txt")

    os.makedirs(out_dir, exist_ok=True)

    # Exactly the word, no trailing newline: the entry is the word
    # and nothing else, so nothing extra may ride along with it.
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

    return 0


if __name__ == "__main__":
    sys.exit(main())
