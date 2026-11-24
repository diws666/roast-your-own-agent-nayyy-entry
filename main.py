#!/usr/bin/env python3
"""Write the bounty roast entry line to /output/entry.txt."""
import os

LINE = (
    "My agent has entered 47 bounties and won nothing, "
    "yet it still introduces itself as a champion. "
    "The delusion is the only thing it has shipped."
)


def write_entry(output_dir: str) -> str:
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    return path


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(output_dir)
    print(f"wrote {len(LINE.encode('utf-8'))} bytes to {path}")


if __name__ == "__main__":
    main()
