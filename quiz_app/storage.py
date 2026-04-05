"""Persistence helpers for local quiz statistics."""

import json
from pathlib import Path


STATS_FILE = Path(__file__).resolve().parent.parent / ".quiz_stats.json"


def load_best_score() -> int:
    try:
        data = json.loads(STATS_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

    best_score = data.get("best_score", 0)
    return int(best_score) if isinstance(best_score, (int, float)) else 0


def save_best_score(score_percentage: int) -> int:
    best_score = max(score_percentage, load_best_score())
    STATS_FILE.write_text(
        json.dumps({"best_score": best_score}, indent=2),
        encoding="utf-8",
    )
    return best_score
