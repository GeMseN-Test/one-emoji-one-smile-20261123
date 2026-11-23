"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji, a teddy bear, to /output/entry.txt.
A teddy bear is warm at first glance: soft, familiar, a small hug
from a stranger. No words, no newline — just the emoji.

Why a teddy bear: the judge reads the emoji the way a stranger
glancing at a phone screen would. A teddy bear is warm and friendly
without needing any context, every age and background reads it the
same way, and it feels deliberately chosen — a comfort object, not
the first smiley that comes to mind. Nothing ironic, nothing
intimate, nothing that could land wrong from a stranger.
"""

import os

EMOJI = "\U0001F9F8"  # 🧸 TEDDY BEAR
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Deterministic: same single emoji on every run, no trailing newline,
    # so the sealed gate sees exactly 1 character of UTF-8 text.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
