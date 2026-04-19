#!/usr/bin/env python3
"""
Append a new episode to podcast/episodes.json.

Used by the weekly-podcast-generator scheduled task. Idempotent — running with
the same episode number replaces the existing entry rather than duplicating.

Usage:
    python3 scripts/append_episode.py \
        --number 18 \
        --title "Episode 18: ..." \
        --date 2026-04-25 \
        --filename podcast-2026-04-25.mp3 \
        --summary "Two-sentence teaser." \
        --notes-html podcast-2026-04-25.html
"""
import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EPISODES_JSON = REPO_ROOT / "episodes.json"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--number", type=int, required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--date", required=True, help="YYYY-MM-DD")
    p.add_argument("--filename", required=True, help="MP3 filename only, no path")
    p.add_argument("--summary", required=True, help="2-sentence teaser")
    p.add_argument("--notes-html", default=None, help="HTML show-notes filename")
    args = p.parse_args()

    data = json.loads(EPISODES_JSON.read_text(encoding="utf-8"))
    new_ep = {
        "number": args.number,
        "title": args.title,
        "date": args.date,
        "filename": args.filename,
        "summary": args.summary,
    }
    if args.notes_html:
        new_ep["show_notes_html"] = args.notes_html

    eps = [e for e in data["episodes"] if e["number"] != args.number]
    eps.append(new_ep)
    eps.sort(key=lambda e: e["number"])
    data["episodes"] = eps

    EPISODES_JSON.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Appended episode {args.number}: {args.title}")


if __name__ == "__main__":
    main()
