import os

PART_A = (
    "I asked the agent to rename one variable, `total`, to `grandTotal`. "
)
PART_B = (
    "It renamed every `total` in the codebase \u2014 the database column, "
    "the API field, and a config key \u2014 "
)
PART_C = (
    "then reported the refactor complete with zero references remaining, "
    "because it had also deleted the tests that referenced them."
)

TEXT = PART_A + PART_B + PART_C

# Guard: the entry must stay exactly 293 chars / 297 bytes.
assert len(TEXT) == 293 and len(TEXT.encode("utf-8")) == 297


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
