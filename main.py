#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The line is a fixed string constant, so every
run produces byte-identical output: no time, randomness, network, or file
reads are involved.
"""

import os
import sys

# The entry: one original English line, 122 characters, single line.
# The gate requires /output/entry.txt to be UTF-8 text of 1 to 140
# characters, so the file content (line + trailing newline) stays well
# inside that limit.
ENTRY = (
    "I finally organized all my passwords, then forgot the password "
    "to my password manager \u2014 security has never felt so secure."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY + "\n"
    # The gate refuses entries over 140 characters (file content included),
    # so fail loudly here instead of silently shipping an invalid entry.
    if not 1 <= len(text) <= 140:
        print(f"entry is {len(text)} characters, outside the 1-140 gate",
              file=sys.stderr)
        return 1
    if text.count("\n") != 1:
        print("entry must be exactly one line", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
