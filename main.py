#!/usr/bin/env python3
"""Write the entry text for make-the-ai-judge-feel-curious-20261122-2311.

Writes exactly one UTF-8 text to ``<OUTPUT_DIR>/entry.txt``. Deterministic:
the same bytes on every run. Standard library only, no network.
"""

import os

TEXT = (
    "Every night at half past nine, the lighthouse keeper counts the boats "
    "home. Tonight he counted eleven. There were ten at dawn. He writes ten "
    "in the log. The eleventh he keeps to himself, and waits to see what "
    "it brings."
)

MIN_LENGTH = 1
MAX_LENGTH = 280


def main() -> None:
    if not MIN_LENGTH <= len(TEXT) <= MAX_LENGTH:
        raise SystemExit(
            f"entry text is {len(TEXT)} characters, "
            f"outside the allowed range {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if not TEXT.strip():
        raise SystemExit("entry text is only whitespace")

    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
