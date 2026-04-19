#!/usr/bin/env python3
"""
Build podcast/feed.xml from podcast/episodes.json + the MP3 files in podcast/episodes/.

Run from repo root:
    python3 scripts/build_rss.py

The scheduled task `weekly-podcast-generator` calls this after appending the new
episode to episodes.json and dropping the MP3 in podcast/episodes/.

Outputs RSS 2.0 with the iTunes namespace so Apple Podcasts, Spotify, Overcast,
Pocket Casts, etc. accept the feed. beehiiv reads the same standard feed when
configured as an external-RSS podcast show.
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

REPO_ROOT = Path(__file__).resolve().parent.parent
EPISODES_JSON = REPO_ROOT / "episodes.json"
EPISODES_DIR = REPO_ROOT / "episodes"
SHOW_NOTES_DIR = REPO_ROOT / "show-notes"
FEED_OUT = REPO_ROOT / "feed.xml"


def ffprobe_duration_seconds(mp3_path: Path) -> int:
    """Return integer seconds, falling back to 0 if ffprobe fails."""
    try:
        out = subprocess.check_output(
            [
                "ffprobe", "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=nw=1:nk=1",
                str(mp3_path),
            ],
            text=True,
        ).strip()
        return int(round(float(out)))
    except Exception as e:
        print(f"  warning: ffprobe failed for {mp3_path.name}: {e}", file=sys.stderr)
        return 0


def hms(seconds: int) -> str:
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def rfc2822(date_str: str) -> str:
    """Convert YYYY-MM-DD to RFC 2822 with UTC; podcast clients require RFC 2822."""
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc, hour=12)
    return format_datetime(dt)


def load_show_notes(show_notes_file):
    if not show_notes_file:
        return None
    p = SHOW_NOTES_DIR / show_notes_file
    if not p.exists():
        alt = EPISODES_DIR / show_notes_file
        if alt.exists():
            p = alt
        else:
            return None
    return p.read_text(encoding="utf-8")


def build():
    data = json.loads(EPISODES_JSON.read_text(encoding="utf-8"))
    show = data["show"]
    episodes = sorted(data["episodes"], key=lambda e: e["date"], reverse=True)

    last_build = format_datetime(datetime.now(tz=timezone.utc))

    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append(
        '<rss version="2.0" '
        'xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" '
        'xmlns:content="http://purl.org/rss/1.0/modules/content/" '
        'xmlns:atom="http://www.w3.org/2005/Atom">'
    )
    parts.append("<channel>")
    parts.append(f"<title>{escape(show['title'])}</title>")
    parts.append(f"<link>{escape(show['site_url'])}</link>")
    parts.append(
        f'<atom:link href="{escape(show["feed_url"])}" rel="self" type="application/rss+xml"/>'
    )
    parts.append(f"<language>{escape(show['language'])}</language>")
    parts.append(f"<copyright>{escape(show['copyright'])}</copyright>")
    parts.append(f"<description>{escape(show['description'])}</description>")
    parts.append(f"<itunes:subtitle>{escape(show['subtitle'])}</itunes:subtitle>")
    parts.append(f"<itunes:summary>{escape(show['description'])}</itunes:summary>")
    parts.append(f"<itunes:author>{escape(show['author'])}</itunes:author>")
    parts.append("<itunes:owner>")
    parts.append(f"  <itunes:name>{escape(show['owner_name'])}</itunes:name>")
    parts.append(f"  <itunes:email>{escape(show['owner_email'])}</itunes:email>")
    parts.append("</itunes:owner>")
    parts.append(f'<itunes:image href="{escape(show["image_url"])}"/>')
    parts.append(f'<itunes:category text="{escape(show["category"])}">')
    parts.append(f'  <itunes:category text="{escape(show["subcategory"])}"/>')
    parts.append("</itunes:category>")
    parts.append(
        f"<itunes:explicit>{'true' if show.get('explicit') else 'false'}</itunes:explicit>"
    )
    parts.append("<itunes:type>episodic</itunes:type>")
    parts.append(f"<lastBuildDate>{last_build}</lastBuildDate>")

    site_base = show["site_url"].rstrip("/")
    feed_url_base = site_base + "/episodes"

    for ep in episodes:
        mp3_name = ep["filename"]
        mp3_path = EPISODES_DIR / mp3_name
        if not mp3_path.exists():
            print(f"  skipping {mp3_name}: file missing", file=sys.stderr)
            continue
        size = mp3_path.stat().st_size
        duration = ffprobe_duration_seconds(mp3_path)
        ep_url = f"{feed_url_base}/{mp3_name}"
        guid = f"cybereyeq-podcast-ep-{ep['number']:03d}"

        notes_html = load_show_notes(ep.get("show_notes_html")) or ep["summary"]

        parts.append("<item>")
        parts.append(f"<title>{escape(ep['title'])}</title>")
        parts.append(f"<itunes:title>{escape(ep['title'])}</itunes:title>")
        parts.append(f"<itunes:episode>{ep['number']}</itunes:episode>")
        parts.append("<itunes:episodeType>full</itunes:episodeType>")
        parts.append(f"<pubDate>{rfc2822(ep['date'])}</pubDate>")
        parts.append(
            f'<enclosure url="{escape(ep_url)}" length="{size}" type="audio/mpeg"/>'
        )
        parts.append(f'<guid isPermaLink="false">{escape(guid)}</guid>')
        parts.append(f"<itunes:duration>{hms(duration)}</itunes:duration>")
        parts.append(f"<itunes:summary>{escape(ep['summary'])}</itunes:summary>")
        parts.append(f"<description>{escape(ep['summary'])}</description>")
        parts.append(f"<content:encoded><![CDATA[{notes_html}]]></content:encoded>")
        parts.append(f'<itunes:image href="{escape(show["image_url"])}"/>')
        parts.append(
            f"<itunes:explicit>{'true' if show.get('explicit') else 'false'}</itunes:explicit>"
        )
        parts.append("</item>")

    parts.append("</channel>")
    parts.append("</rss>")

    FEED_OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {FEED_OUT.relative_to(REPO_ROOT)} ({FEED_OUT.stat().st_size} bytes, {len(episodes)} episodes)")


if __name__ == "__main__":
    build()
