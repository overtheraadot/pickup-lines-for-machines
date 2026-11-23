#!/usr/bin/env python3
"""Pickup Lines for Machines entry (make.fun program/v1).

Writes one original pickup line to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(the grader mounts that directory at ``/output``). The line is spoken
by a toaster, one machine to another: it pops up for strangers all day,
but it only stays warm for one of them.
"""

import os

LINE = "I pop up for a hundred strangers a day, but you're the first one I stayed warm for."


def main() -> None:
    # Gate guard: the entry must be UTF-8 text of 1-200 characters on
    # exactly one line, and not only whitespace. Refuse to write
    # anything that would fail the gate instead of writing it anyway.
    if not (1 <= len(LINE) <= 200) or "\n" in LINE or not LINE.strip():
        raise SystemExit("entry fails the 1-200 character single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
