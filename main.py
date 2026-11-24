#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence to /output/entry.txt (or $ENTRY_OUTPUT) that makes a
small everyday moment strange and new.

Why this sentence works: a lift ride is the most ordinary, forgettable
moment of the day, but a stranger humming a song that belongs to the
narrator's grandmother turns it into an impossible coincidence -- private
memory leaking into public space. The surprise lands in a single read, and
the shared silence in the last clause keeps it grounded and human instead
of explaining the mystery away.
"""

import os

SENTENCE = (
    "The lift doors opened on a stranger humming my grandmother's "
    "lullaby, and for one floor neither of us said a word."
)


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

    # Gate first: one sentence, 1-200 characters, not only whitespace.
    stripped = SENTENCE.strip()
    assert stripped, "sentence must not be empty or only whitespace"
    assert "\n" not in stripped, "sentence must be a single line"
    assert 1 <= len(SENTENCE) <= 200, (
        f"sentence must be 1-200 characters, got {len(SENTENCE)}"
    )

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")

    # Read it back and check it holds exactly what was written.
    with open(output_path, "r", encoding="utf-8") as f:
        read_back = f.read()
    assert read_back == SENTENCE + "\n", "output file does not match sentence"
    print(f"Wrote {len(SENTENCE)} characters to {output_path}")


if __name__ == "__main__":
    main()
