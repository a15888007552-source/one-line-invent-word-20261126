"""Invent a Word We Need.

Writes one invented English word with a one-line definition to
$MAKEFUN_OUTPUT_DIR/entry.txt.

The word: miswave. The gap it fills is real and instantly recognisable
to anyone who has ever done it: waving back at a stranger, only to
realise the wave was meant for the person standing behind you. English
has a word for the wave, but none for that small, sinking moment after
it. "Miswave" is built from plain English parts (mis- + wave), so it is
sayable on first sight, spellable on first hearing, and memorable
because the embarrassment it names is universal.
"""

from pathlib import Path
import os

LINE = "miswave (n.): waving back at someone who was waving at the person behind you."


def entry_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def write_line(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


def main() -> None:
    # Second revision: kept the definition to a single clause so the
    # meaning lands in one reading, with no example sentence needed.
    write_line(entry_path())


if __name__ == "__main__":
    main()
