#!/usr/bin/env python3
"""Import the app's six privacy policies without changing the app files.
Usage: python3 tools/sync_app_privacy.py /path/to/app/assets/legal
"""
import html
import json
import re
import sys
from pathlib import Path

LANGS = ('ko', 'en', 'ja', 'de', 'fr', 'es')
OUTPUT = Path(__file__).with_name('app_privacy.json')

def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return re.sub(r'(?<!["=])(https://[^\s<>]+)', lambda m: '<a href="' + html.escape(m[0], quote=True) + '">' + m[0] + '</a>', text)

def parse(text):
    lines = text.strip().splitlines()
    if not lines[0].startswith('# ') or not lines[1].strip():
        raise ValueError('Missing title or effective date')
    sections = []
    preamble = []
    current = None
    closing = ''
    for line in lines[2:]:
        line = line.strip()
        if not line:
            continue
        if line.startswith('## '):
            current = [inline(line[3:]), []]
            sections.append(current)
        elif current is None:
            preamble.append(inline(line))
        elif line.startswith('- '):
            if not current[1] or current[1][-1][0] != 'ul':
                current[1].append(['ul', []])
            current[1][-1][1].append(inline(line[2:]))
        elif len(sections) == 6:
            closing = inline(line)
        else:
            current[1].append(['p', inline(line)])
    if len(sections) != 6 or len(preamble) != 1 or not closing:
        raise ValueError('Expected an introduction, six sections and closing')
    return dict(intro=preamble[0], mdEffective=lines[1], sections=sections, closing=closing)

if __name__ == '__main__':
    root = Path(sys.argv[1])
    result = {lang: parse((root / f'privacy_{lang}.md').read_text()) for lang in LANGS}
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print('Synced six privacy policies; app files unchanged.')
