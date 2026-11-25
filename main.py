"""Famous Last Words: The Funniest Epitaph.

Writes one line of famous last words, a tombstone epitaph, to
/output/entry.txt. Pure standard library, fully deterministic.
"""

import os

EPITAPH = "I always said I'd sleep when I'm dead. Turns out, I was right."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EPITAPH.strip()
    assert 1 <= len(text) <= 150, "epitaph must be 1-150 characters"
    assert "\n" not in text, "epitaph must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
