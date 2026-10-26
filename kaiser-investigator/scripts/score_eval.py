#!/usr/bin/env python3
"""Compare manually labelled verdicts; this does not run or evaluate an agent."""
import json
import sys
from pathlib import Path

VALID = {"CONFIRMED", "LIKELY", "INCONCLUSIVE", "DISPROVED"}

def main(path: str) -> int:
    rows = []
    for number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        expected, predicted = row.get("expected"), row.get("predicted")
        if expected not in VALID or predicted not in VALID:
            raise ValueError(f"Line {number}: verdict labels must be {sorted(VALID)}")
        rows.append((expected, predicted))
    if not rows:
        print("No labelled rows found.")
        return 1
    correct = sum(a == b for a, b in rows)
    print(f"Verdict-label agreement: {correct}/{len(rows)} ({correct / len(rows):.1%})")
    print("This is label agreement only, not overall skill quality or accuracy.")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} labelled-results.jsonl")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
