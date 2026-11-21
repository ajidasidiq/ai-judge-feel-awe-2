#!/usr/bin/env python3
"""Make the AI judge feel awe - make.fun entry.

Writes one short, original text to /output/entry.txt.
Deterministic, no network, standard library only.
"""

import os

TEXT = (
    "The tide comes in whether anyone watches it or not. "
    "It smooths the sand, fills each small hollow, and leaves. "
    "Somewhere a lighthouse turns, slow as a hand turning a page, "
    "and the dark between its flashes is not empty. "
    "It is the sea, resting."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
