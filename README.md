# cybereyeq/podcast

Public hosting for the CyberEyeQ Weekly Podcast. Audio + RSS feed served via GitHub Pages
at https://cybereyeq.github.io/podcast/ — beehiiv (and Apple/Spotify/Overcast) read the same
`feed.xml` as an external-RSS source.

## Layout

```
.
├── index.html              # landing page (Pages serves this at /podcast/)
├── feed.xml                # generated RSS — https://cybereyeq.github.io/podcast/feed.xml
├── episodes.json           # source of truth for the feed
├── cover.jpg               # 3000x3000 show artwork (Apple requires >=1400x1400)
├── episodes/               # MP3 files referenced by enclosure URLs
├── show-notes/             # per-episode HTML, embedded as content:encoded
└── scripts/
    ├── append_episode.py   # adds an entry to episodes.json
    └── build_rss.py        # regenerates feed.xml from episodes.json + the MP3s
```

Note: the Pages URL root for a repo named `podcast` is already `/podcast/`, so the repo content lives at the *root* of the repo, not inside a `podcast/` subdirectory.

## Weekly publishing flow

The `weekly-podcast-generator` scheduled task does this automatically every Saturday:

1. Generates the dialogue script + show-notes HTML.
2. Synthesizes the MP3 with espeak-ng (in-sandbox).
3. Drops `podcast-YYYY-MM-DD.mp3` into `podcast/episodes/`.
4. Drops `podcast-YYYY-MM-DD.html` into `podcast/show-notes/`.
5. Calls `scripts/append_episode.py --number N --title ... --filename ...`.
6. Calls `scripts/build_rss.py` to regenerate `feed.xml`.
7. Pushes both files to `main`.

GitHub Pages serves the new feed within ~1 minute of the push. beehiiv polls
external-RSS feeds on its own schedule (typically every few hours).

## Manual one-off

```bash
python3 scripts/append_episode.py \
  --number 18 \
  --title "Episode 18: ..." \
  --date 2026-04-25 \
  --filename podcast-2026-04-25.mp3 \
  --summary "Two-sentence teaser." \
  --notes-html podcast-2026-04-25.html
python3 scripts/build_rss.py
git add podcast/ && git commit -m "podcast: episode 18" && git push
```
