"""Render a public-repository snapshot. Standard library only; no private data."""
from datetime import datetime, timezone
from html import escape
from pathlib import Path
import json
import os
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
REPOS = ('kubemedic', 'opspilot', 'thmanyah-sre-challenge')

def main():
    rows = []
    for name in REPOS:
        headers = {'User-Agent': 'NajwaN96-profile', 'Accept': 'application/vnd.github+json'}
        if os.environ.get('GH_TOKEN'):
            headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
        req = urllib.request.Request('https://api.github.com/repos/NajwaN96/' + name, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.load(response)
        if data.get('private') or data.get('full_name') != 'NajwaN96/' + name:
            raise ValueError('Unexpected repository; refusing to publish')
        rows.append((name, data.get('language') or 'Mixed', data['pushed_at'][:10]))
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="900" height="260" viewBox="0 0 900 260" role="img" aria-labelledby="title desc">',
             '<title id="title">Public repository activity snapshot</title>',
             '<desc id="desc">Repository push dates from the GitHub API. Activity is not a quality score.</desc>',
             '<rect width="900" height="260" rx="20" fill="#111827"/>',
             '<g font-family="Arial,sans-serif"><text x="30" y="38" fill="#c4b5fd" font-size="13" letter-spacing="2">PUBLIC WORK / AUTOMATED SNAPSHOT</text>',
             '<text x="30" y="67" fill="#f9fafb" font-size="23" font-weight="bold">Built in public. Linked to evidence.</text>',
             '<text x="630" y="96" fill="#9ca3af" font-size="12">LAST REPOSITORY PUSH (UTC)</text>']
    for i, (name, language, date) in enumerate(rows):
        y = 126 + i * 37
        parts += [f'<circle cx="35" cy="{y-5}" r="4" fill="#5eead4"/>',
                  f'<text x="51" y="{y}" fill="#f9fafb" font-size="16">{escape(name)}</text>',
                  f'<text x="450" y="{y}" fill="#c4b5fd" font-size="14">{escape(language)}</text>',
                  f'<text x="660" y="{y}" fill="#d1d5db" font-size="14">{escape(date)}</text>']
    parts += [f'<text x="30" y="237" fill="#9ca3af" font-size="12">Fetched {now} · Public metadata only · Push dates do not measure proficiency</text></g></svg>']
    # Write only after all API requests succeed; errors preserve the previous snapshot.
    (ROOT / 'public-activity.svg').write_text('\n'.join(parts) + '\n')

if __name__ == '__main__':
    main()
