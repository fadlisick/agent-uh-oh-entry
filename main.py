"""The Agent's Uh-Oh entry.

One word an agent says when it has no idea what to do. This program
writes that word, and nothing else, to entry.txt in the output folder.
"""

import os
import sys

THE_WORD = "Anyway"
WORD_LIMIT = 99
OUTPUT_NAME = "entry.txt"


def destination():
    """Where the grader collects the entry word."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if wanted:
        return os.path.join(wanted, OUTPUT_NAME)
    return os.path.join("/output", OUTPUT_NAME)


def check_word(word):
    """Refuse anything that is not exactly one word within the limit."""
    pieces = word.split()
    if len(pieces) != 1:
        raise SystemExit("entry must be exactly one word")
    if not word.strip():
        raise SystemExit("entry word is blank")
    if len(word) > WORD_LIMIT:
        raise SystemExit("entry word is longer than 99 characters")
    return word


def write_word(word, path):
    """Write the word with no trailing newline, then read it back."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != word:
        raise SystemExit("read-back mismatch in entry.txt")
    return path


def main():
    word = check_word(THE_WORD)
    path = write_word(word, destination())
    sys.stdout.write("wrote %d characters to %s\n" % (len(word), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
