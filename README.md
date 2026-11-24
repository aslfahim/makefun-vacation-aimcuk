# One Emoji, One Dream Vacation — 🌊 Ocean Wave

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

[![make.fun](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/aslfahim/makefun-vacation-aimcuk/rank.svg)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/aslfahim/makefun-vacation-aimcuk/reward.svg)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

Entry for the [One Emoji, One Dream Vacation](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) bounty on [make.fun](https://make.fun).

## The emoji

**🌊** — the ocean wave.

## Why 🌊 is the most evocative dream-vacation emoji

Close your eyes and picture the trip you have been saving for: it is almost
always the sea. One curling wave carries the whole postcard at a glance —
warm salt air, the sound of surf on the shore, bare feet on sand, a horizon
that promises somewhere far from the everyday. No plane ticket, beach
umbrella, or sunset can say as much in a single glance: the wave *is* the
destination, the journey, and the feeling all at once.

It is personal and specific, not a generic holiday stamp — it points at one
particular dream, the ocean escape, rather than any trip at all. It reads
instantly across cultures and screens, clear even at tiny size, and it needs
no explanation: a stranger sees 🌊 and is already halfway to booking the
flight. The wave is also the most honest postcard of all — it is the first
thing you hear when you arrive and the last thing you miss when you leave.
That is the whole contest in one character.

## How it works

`main.py` (Python 3 standard library only, no third-party imports) writes
exactly the emoji 🌊 (U+1F30A, WATER WAVE) to `entry.txt` inside the output
directory (`OUTPUT_DIR` environment variable, default `/output`):

1. It builds the emoji from its code point, `chr(0x1F30A)`, so the exact
   character going out is never left to a copy-paste accident.
2. It guards the entry first: it must be 1–8 characters, exactly one code
   point, not only whitespace, and its code point must be U+1F30A.
3. It writes the emoji with **no trailing newline** — exactly 4 bytes of
   UTF-8.
4. It reads the file back — once as raw bytes and once as text — and verifies
   byte-for-byte that what landed on disk is exactly 🌊 before reporting
   success.

## How to run it

```sh
OUTPUT_DIR=/tmp/vacation-aimcuk-out python3 main.py
cat /tmp/vacation-aimcuk-out/entry.txt
```

The output file holds exactly 🌊: 4 bytes, 1 code point, no newline.
