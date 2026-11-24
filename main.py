"""One Emoji, One Dream Vacation — Ocean Wave entry.

Writes exactly one emoji, U+1F30A WATER WAVE, to entry.txt inside the
output directory. Standard library only.

Design: the emoji is built from its code point at runtime (never pasted
as a literal in the output path), validated against the gate rules, and
the file on disk is read back and compared byte-for-byte before the
program reports success.
"""

import os
import sys


CODE_POINT = 0x1F30A  # WATER WAVE
MIN_CHARS = 1
MAX_CHARS = 8
ENTRY_NAME = "entry.txt"


def dream_emoji() -> str:
    """Return the single dream-vacation emoji from its code point."""
    return chr(CODE_POINT)


def output_path() -> str:
    """Resolve the entry file path from OUTPUT_DIR (default /output)."""
    base = os.environ.get("OUTPUT_DIR") or "/output"
    return os.path.join(base, ENTRY_NAME)


def check_entry(text: str) -> None:
    """Enforce the gate: 1-8 characters, exactly one code point, not blank."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}")
    if len(text) != 1:
        raise ValueError(f"entry must be exactly one emoji, got {len(text)} code points")
    if text.isspace():
        raise ValueError("entry must not be only whitespace")
    if ord(text) != CODE_POINT:
        raise ValueError("entry is not the intended ocean-wave emoji")


def write_entry(path: str, text: str) -> int:
    """Write the emoji with no trailing newline; return bytes written."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        written = handle.write(text)
    return written


def verify_on_disk(path: str, expected: str) -> None:
    """Read the file back and confirm it holds exactly the expected emoji."""
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != expected.encode("utf-8"):
        raise ValueError(f"disk bytes {raw!r} do not match expected {expected.encode('utf-8')!r}")
    with open(path, "r", encoding="utf-8", newline="") as handle:
        round_tripped = handle.read()
    if round_tripped != expected:
        raise ValueError("round-trip read does not match the entry")
    if len(round_tripped) != 1:
        raise ValueError("round-trip read is not a single code point")


def main() -> int:
    emoji = dream_emoji()
    check_entry(emoji)
    path = output_path()
    write_entry(path, emoji)
    verify_on_disk(path, emoji)
    print(f"Wrote {emoji} ({len(emoji)} code point, {len(emoji.encode('utf-8'))} bytes) to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
