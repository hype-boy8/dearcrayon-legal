"""디어 크레용 안내 페이지 · 앱 처리방침 md 를 content.py 에서 만든다.
사용: python3 -I build.py <사이트 폴더> <앱 assets/legal 폴더>
"""
import html as H
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import L, LANGS, BASE, MAIL, PLAY  # noqa: E402

SITE, APP_LEGAL = sys.argv[1], sys.argv[2]
PAGES = ['index', 'privacy', 'terms', 'delete']
MD_TITLE = {
    'ko': '디어 크레용 개인정보 처리방침',
    'en': 'Dear Crayon Privacy Policy',
    'de': 'Datenschutzerklärung von Dear Crayon',
    'fr': 'Politique de confidentialité de Dear Crayon',
    'es': 'Política de privacidad de Dear Crayon',
    'ja': 'Dear Crayon プライバシーポリシー',
}


def d(lang):
    return '' if lang == 'ko' else lang + '/'


def rel(cur, target_lang, file):
    """cur 언어 폴더에서 target 언어의 file 로 가는 상대 경로."""
    up = '' if cur == 'ko' else '../'
    return up + d(target_lang) + file


def url(lang, page):
    return BASE + d(lang) + ('' if page == 'index' else page + '.html')


def blocks(bs):
    out = []
    for b in bs:
        k = b[0]
        if k == 'p':
            out.append(f'<p>{b[1]}</p>')
        elif k in ('ul', 'ol'):
            cls = ' class="steps"' if k == 'ol' else ''
            out.append(f'<{k}{cls}>' + ''.join(f'<li>{x}</li>' for x in b[1]) + f'</{k}>')
        elif k == 'dl':
            out.append('<dl class="facts">' + ''.join(f'<div><dt>{a}</dt><dd>{c}</dd></div>' for a, c in b[1]) + '</dl>')
        else:
            raise ValueError(k)
    return '\n'.join(out)


def sections(secs):
    return '\n'.join(f'<section>\n<h2>{h}</h2>\n{blocks(bs)}\n</section>' for h, bs in secs)


def page(lang, name):
    c = L[lang]
    p = '' if lang == 'ko' else '../'
    file = f'{name}.html'
    if name == 'index':
        ix = c['index']
        title, desc = ix['title'], ix['desc']
        body = [
            '<div class="hero">',
            f'<img class="hero-logo" src="{p}assets/logo.png" alt="{c["name"]}" width="240" height="79">',
            f'<h1 class="hero-line">{ix["hero"]}</h1>',
            f'<a class="play" href="{PLAY}" rel="noopener">{ix["play"]}</a>',
            f'<p class="play-note">{ix["playNote"]}</p>',
            '</div>',
            f'<section class="receive">\n<h2>{ix["receiveTitle"]}</h2>\n' + blocks([('ol', ix['receive'])]) + '\n</section>',
            f'<section>\n<h2>{ix["aboutTitle"]}</h2>\n<p>{ix["about"]}</p>\n</section>',
            f'<section>\n<h2>{ix["docsTitle"]}</h2>\n<ul class="cards">'
            + ''.join(
                f'<li><a href="{x}.html"><strong>{c["nav"][x]}</strong><span>{ix["links"][x]}</span></a></li>'
                for x in ('privacy', 'terms', 'delete'))
            + '</ul>\n</section>',
        ]
    else:
        pg = c[name]
        title = f'{pg["title"]} · {c["name"]}'
        desc = (pg.get('intro') or re.sub('<[^>]+>', '', pg['sections'][0][1][0][1]))[:160]
        body = [f'<h1>{pg["title"]}</h1>', f'<p class="meta">{c["name"]} · {c["effective"]}</p>']
        if name == 'privacy':
            body.append(f'<p class="lead">{pg["intro"]}</p>')
            body.append(f'<aside class="summary" aria-label="{pg["summaryTitle"]}"><h2>{pg["summaryTitle"]}</h2><ul>'
                        + ''.join(f'<li>{x}</li>' for x in pg['summary']) + '</ul></aside>')
        body.append(sections(pg['sections']))
        if name == 'privacy':
            body.append(f'<p class="closing">{pg["closing"]}</p>')

    alts = '\n'.join(f'<link rel="alternate" hreflang="{l}" href="{url(l, name)}">' for l in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{url("en", name)}">'
    langs = ''.join(
        f'<a href="{rel(lang, l, file)}" hreflang="{l}" lang="{l}"' + (' aria-current="true"' if l == lang else '') + f'>{L[l]["langName"]}</a>'
        for l in LANGS)
    tabs = ''.join(
        f'<a href="{x}.html"' + (' aria-current="page"' if x == name else '') + f'>{c["nav"]["home" if x == "index" else x]}</a>'
        for x in PAGES)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(title, quote=False)}</title>
<meta name="description" content="{H.escape(desc)}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url(lang, name)}">
{alts}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{c["name"]}">
<meta property="og:title" content="{H.escape(c["index"]["ogTitle"] if name == "index" else title)}">
<meta property="og:description" content="{H.escape(desc)}">
<meta property="og:url" content="{url(lang, name)}">
<meta property="og:image" content="{BASE}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141518" media="(prefers-color-scheme: dark)">
<link rel="icon" type="image/png" href="{p}assets/favicon.png">
<link rel="apple-touch-icon" href="{p}assets/icon-180.png">
<link rel="stylesheet" href="{p}assets/site.css">
</head>
<body>
<div class="wrap">
<header class="top">
{"<span></span>" if name == "index" else f'<a class="brand" href="index.html"><img src="{p}assets/logo.png" alt="{c["name"]}" width="168" height="55"></a>'}
<nav class="langs" aria-label="{c["langLabel"]}">{langs}</nav>
</header>
{"" if name == "index" else f'<nav class="tabs" aria-label="{c["name"]}">{tabs}</nav>'}
<main>
{chr(10).join(body)}
</main>
<footer>{c["footer"]}<br>{c["contact"]} {MAIL}<br>{c["effective"]}</footer>
</div>
</body>
</html>
'''


def md_text(s):
    s = re.sub(r'<strong>(.*?)</strong>', r'**\1**', s)
    s = re.sub(r'<a [^>]*>(.*?)</a>', r'\1', s)
    s = re.sub(r'<[^>]+>', '', s)
    return H.unescape(s)


def privacy_md(lang):
    pg = L[lang]['privacy']
    out = [f'# {MD_TITLE[lang]}', pg['mdEffective'], '', md_text(pg['intro']), '']
    for h, bs in pg['sections']:
        out.append(f'## {h}')
        for b in bs:
            if b[0] == 'p':
                out.append(md_text(b[1]))
            else:
                out += [f'- {md_text(x)}' for x in b[1]]
        out.append('')
    out.append(md_text(pg['closing']))
    return '\n'.join(out) + '\n'


CSS = r''':root {
  color-scheme: light dark;
  --bg: #FFFFFF; --fg: #1A1C20; --muted: #555D6D; --subtle: #868B94;
  --line: #DCDEE3; --soft: #F7F8F9; --soft2: #F3F4F5;
  --brand: #FE644A; --brand-ink: #BA3620; --brand-weak: #FFF2EF; --brand-line: #FFD4CB;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #141518; --fg: #EEEFF1; --muted: #B0B3BA; --subtle: #868B94;
    --line: #2E333B; --soft: #1B1D21; --soft2: #23262B;
    --brand: #FE644A; --brand-ink: #FE917C; --brand-weak: rgba(254,100,74,.12); --brand-line: rgba(254,100,74,.32);
  }
  .brand img { background: #FFFFFF; border-radius: 12px; padding: 4px 8px; }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0; background: var(--bg); color: var(--fg);
  font-family: -apple-system, BlinkMacSystemFont, 'Apple SD Gothic Neo', 'Pretendard', 'Noto Sans KR',
               'Malgun Gothic', 'Segoe UI', Roboto, sans-serif;
  font-size: 16px; line-height: 1.7; overflow-wrap: anywhere;
}
:lang(ko) { word-break: keep-all; }
:lang(ja) {
  font-family: -apple-system, BlinkMacSystemFont, 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Noto Sans JP',
               'Yu Gothic', 'Meiryo', 'Segoe UI', Roboto, sans-serif;
  line-break: strict;
}
.wrap { max-width: 720px; margin: 0 auto; padding: 24px 16px 72px; }
@media (min-width: 600px) { .wrap { padding: 40px 24px 96px; } }

a { color: var(--brand-ink); text-underline-offset: 3px; }
a:focus-visible { outline: 3px solid var(--brand); outline-offset: 3px; border-radius: 6px; }

.top { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 16px; margin-bottom: 20px; }
.brand { display: inline-flex; line-height: 0; }
.brand img { display: block; width: 168px; height: auto; max-width: 100%; }
.langs { display: flex; flex-wrap: wrap; gap: 4px; }
.langs a {
  font-size: 13px; line-height: 1; padding: 8px 10px; border-radius: 999px;
  color: var(--muted); text-decoration: none;
}
.langs a:hover { background: var(--soft2); }
.langs a[aria-current] { background: var(--brand-weak); color: var(--brand-ink); font-weight: 700; }

.tabs { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 36px; }
.tabs a {
  display: inline-block; padding: 9px 16px; border-radius: 999px; font-size: 14px; line-height: 1.3;
  background: var(--soft2); color: var(--fg); text-decoration: none;
}
.tabs a:hover { background: var(--line); }
.tabs a[aria-current] { background: var(--brand-weak); color: var(--brand-ink); font-weight: 700; box-shadow: inset 0 0 0 1px var(--brand-line); }

h1 { font-size: 28px; line-height: 1.3; font-weight: 800; letter-spacing: -0.02em; margin: 0; }
h1::after {
  content: ""; display: block; width: 56px; height: 6px; margin-top: 12px;
  border-radius: 6px; background: var(--brand); transform: rotate(-1.5deg);
}
.meta { color: var(--subtle); font-size: 13px; margin: 14px 0 0; }
.meta:first-child { margin: 0 0 8px; }
.tagline { font-size: 18px; font-weight: 700; color: var(--brand-ink); margin: 16px 0 0; }
.lead { color: var(--muted); margin: 16px 0 0; }
h2 { font-size: 18px; line-height: 1.4; font-weight: 700; margin: 0 0 10px; }
section { margin-top: 40px; }
p { margin: 0; color: var(--muted); }
section p + p, section ul + p, section ol + p { margin-top: 12px; }
ul, ol { margin: 0; padding-left: 22px; color: var(--muted); }
li { margin: 8px 0; }
li::marker { color: var(--brand); }
strong { color: var(--fg); font-weight: 700; }

.summary {
  margin-top: 28px; padding: 18px 20px; border-radius: 16px;
  background: var(--brand-weak); border: 1px solid var(--brand-line);
}
.summary h2 { font-size: 16px; margin: 0 0 4px; color: var(--brand-ink); }
.summary ul { color: var(--fg); }
.summary li { margin: 6px 0; }

ol.steps { list-style: none; padding: 0; counter-reset: step; }
ol.steps > li { position: relative; padding-left: 40px; margin: 12px 0; counter-increment: step; }
ol.steps > li::before {
  content: counter(step); position: absolute; left: 0; top: 0;
  width: 28px; height: 28px; border-radius: 50%;
  background: var(--brand-weak); color: var(--brand-ink);
  font-size: 14px; font-weight: 800; line-height: 28px; text-align: center;
}

.facts { margin: 0; display: grid; gap: 10px; }
.facts > div { background: var(--soft); border: 1px solid var(--line); border-radius: 14px; padding: 14px 16px; }
.facts dt { font-weight: 700; color: var(--fg); font-size: 15px; }
.facts dd { margin: 4px 0 0; color: var(--muted); font-size: 15px; }

.cards { list-style: none; padding: 0; display: grid; gap: 10px; }
.cards li { margin: 0; }
.cards a {
  display: block; padding: 16px 44px 16px 18px; border-radius: 16px; position: relative;
  border: 1px solid var(--line); background: var(--bg); text-decoration: none; color: var(--fg);
}
.cards a::after { content: "›"; position: absolute; right: 18px; top: 50%; transform: translateY(-52%); font-size: 22px; color: var(--subtle); }
.cards a:hover { border-color: var(--brand-line); background: var(--brand-weak); }
.cards strong { display: block; font-size: 16px; }
.cards span { display: block; color: var(--muted); font-size: 14px; margin-top: 2px; }

.closing { margin-top: 40px; color: var(--subtle); font-size: 14px; }
footer {
  margin-top: 64px; padding-top: 20px; border-top: 1px solid var(--line);
  color: var(--subtle); font-size: 13px; line-height: 1.8;
}
footer a { color: inherit; }

.hero { text-align: center; padding: 16px 0 8px; }
.hero-logo { display: block; width: 240px; max-width: 72%; height: auto; margin: 0 auto; }
.hero-line { font-size: 22px; line-height: 1.45; font-weight: 800; margin: 20px auto 0; max-width: 22em; }
.hero-line::after { margin: 14px auto 0; }
.play {
  display: inline-block; margin-top: 28px; padding: 16px 28px; min-width: 240px; max-width: 100%;
  border-radius: 14px; background: #BA3620; color: #FFFFFF; text-decoration: none;
  font-size: 17px; font-weight: 800; line-height: 1.3;
  box-shadow: 0 6px 18px rgba(186,54,32,.22);
}
.play:hover { background: #872818; }
.play-note { margin-top: 12px; font-size: 14px; color: var(--subtle); }
.receive { background: var(--soft); border: 1px solid var(--line); border-radius: 18px; padding: 20px 20px 10px; }
@media (prefers-color-scheme: dark) {
  .brand img, .hero-logo { background: #FFFFFF; border-radius: 14px; padding: 6px 10px; }
  .play { box-shadow: none; }
}
'''

if __name__ == '__main__':
    os.makedirs(os.path.join(SITE, 'assets'), exist_ok=True)
    with open(os.path.join(SITE, 'assets', 'site.css'), 'w', encoding='utf-8') as f:
        f.write(CSS)
    for lang in LANGS:
        out_dir = os.path.join(SITE, d(lang))
        os.makedirs(out_dir, exist_ok=True)
        for name in PAGES:
            with open(os.path.join(out_dir, f'{name}.html'), 'w', encoding='utf-8') as f:
                f.write(page(lang, name))
        with open(os.path.join(APP_LEGAL, f'privacy_{lang}.md'), 'w', encoding='utf-8') as f:
            f.write(privacy_md(lang))
    open(os.path.join(SITE, '.nojekyll'), 'w').close()
    print('ok')
