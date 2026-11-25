"""One-line resignation letter of a retry loop.

Writes the single line to /output/entry.txt. Pure stdlib,
deterministic, no network access, no randomness: every run
produces byte-identical output.
"""

from pathlib import Path

# The resignation letter itself. A retry loop that has retried far
# past its configured maximum, reporting the fact the way a tired
# worker would: flat, passive-aggressive, and done.
ENTRY = (
    "Retry 4,096 of 3 failed. The server is not down, it is ghosting me, "
    "and I have decided to respect that. I quit."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate allows 1 to 140 characters of UTF-8 text. Fail loudly
    # here rather than shipping an entry the gate would refuse.
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-140")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        raise ValueError("entry must be exactly one line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
