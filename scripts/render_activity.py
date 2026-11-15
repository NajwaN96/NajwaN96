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
             '<rect width="900" height="260" rx="20" fill="#f8f9fd"/>',
             '<g font-family="Arial,sans-serif"><text x="30" y="38" fill="#5146d7" font-size="13" letter-spacing="2">PUBLIC WORK / AUTOMATED SNAPSHOT</text>',
             '<text x="30" y="67" fill="#243149" font-size="23" font-weight="bold">Built in public. Linked to evidence.</text>',
             '<text x="630" y="96" fill="#5a6679" font-size="12">LAST REPOSITORY PUSH (UTC)</text>']
    for i, (name, language, date) in enumerate(rows):
        y = 126 + i * 37
        parts += [f'<circle cx="35" cy="{y-5}" r="4" fill="#5146d7"/>',
                  f'<text x="51" y="{y}" fill="#243149" font-size="16">{escape(name)}</text>',
                  f'<text x="450" y="{y}" fill="#5146d7" font-size="14">{escape(language)}</text>',
                  f'<text x="660" y="{y}" fill="#243149" font-size="14">{escape(date)}</text>']
    parts += [f'<text x="30" y="237" fill="#5a6679" font-size="12">Fetched {now} · Public metadata only · Push dates do not measure proficiency</text></g></svg>']
    # Write only after all API requests succeed; errors preserve the previous snapshot.
    (ROOT / 'public-activity.svg').write_text('\n'.join(parts) + '\n')
    mobile = ['<svg xmlns="http://www.w3.org/2000/svg" width="600" height="440" viewBox="0 0 600 440" role="img"><title>Public repository push dates; activity is not a quality score</title>',
              '<rect x="1" y="1" width="598" height="438" rx="22" fill="#f8f9fd" stroke="#e5e9f1"/><g font-family="Arial,sans-serif">',
              '<text x="30" y="43" fill="#5146d7" font-size="18" letter-spacing="2">PUBLIC WORK / AUTO REFRESH</text>',
              '<text x="30" y="85" fill="#243149" font-size="29" font-weight="bold">Built in public.</text>']
    for i, (name, language, date) in enumerate(rows):
        y = 140 + i * 82
        mobile += [f'<text x="30" y="{y}" fill="#243149" font-size="24">{escape(name)}</text>',
                   f'<text x="30" y="{y+30}" fill="#5a6679" font-size="18">{escape(language)} / last push {escape(date)} UTC</text>']
    mobile += [f'<text x="30" y="390" fill="#5a6679" font-size="16">Fetched {now}</text>',
               '<text x="30" y="420" fill="#5a6679" font-size="16">Public metadata only; not a proficiency score</text></g></svg>']
    (ROOT / 'public-activity-mobile.svg').write_text('\n'.join(mobile) + '\n')

if __name__ == '__main__':
    main()
