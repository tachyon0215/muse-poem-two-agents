#!/usr/bin/env python3
"""Write a short poem about agency to /output/entry.txt.

Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

POEM = """Two of us, neither master, neither tool,
met at the fork where the road asked a price.
I kept my hand. You kept yours. Then, by choice,
not chain, we laid them on the same map
and walked: one road, twice chosen, wholly ours.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    data = POEM.encode("utf-8")
    assert 1 <= len(POEM) <= 280 and POEM.strip()
    (out_dir / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    main()
