#!/usr/bin/env python3
"""Write one loading-screen tip to /output/entry.txt.

Competition: u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270
Gate: /output/entry.txt must be UTF-8 text, 1 to 200 characters, not
only whitespace. One line, no trailing newline issues: the file holds
exactly the tip text.
"""

import os

ENTRY = "Tip: the agent finished in 9 seconds. You now have 45 minutes to learn what 'done' meant to it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
