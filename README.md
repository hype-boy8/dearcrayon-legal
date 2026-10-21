# Dear Crayon public pages

GitHub Pages: https://hype-boy8.github.io/dearcrayon-legal/

## Build

`python3 -I tools/build.py /absolute/path/to/dearcrayon-legal`

The optional second argument is the app assets/legal directory. Omit it for web-only design changes. Legal copy stays in tools/content.py; landing design and six-language marketing copy live in tools/landing.py. Do not edit generated HTML/CSS directly.

## Store launch

Until the public listing exists, PLAY_AVAILABLE=False in tools/landing.py displays a launch notice instead of sending visitors to a missing page. After the public listing is confirmed, set it to True, rebuild and deploy. The existing package-specific Google Play URL remains in tools/content.py. Update COPY[language]['receiveNote'] at launch to remove the pre-launch qualification.

## Brand refresh 2026-10-19

- Approved Dear Crayon logo, crayon planet and existing illustration icons. No child photos or user records included.
- Warm paper/cocoa/coral design, responsive layout, fixed light paper appearance regardless of system dark mode (user decision).
- Native disclosure language picker with six native language names, current-language check, Escape/outside-click close. Switching preserves the current page type. No flags or automatic redirection.
- Home introduces drawings, voice and books; book-receiving instructions are expandable. Legal URLs and legal document body content remain unchanged.
- Localized page/share titles and descriptions, Open Graph/Twitter metadata. New 1200×630 brand preview: assets/og-brand-v74.png. Its source is tools/og-preview.html; render that at 1200×630 when changing the image.
- NanumSquareRound/Nunito font licenses are retained alongside self-hosted font files. Japanese uses the device's Japanese typeface.
- Verified six languages at 390px; 320px and desktop edge cases, light/dark views, language selection, Escape and guide opening. Static verification covers local assets and 24 page links; legal body compared against the previous commit.
- Sharing apps may retain the previous preview in their cache. Site titles and metadata change on deployment, but previously sent messages do not necessarily refresh.

## Teacher invitation page · 2026-10-21

- `/join/#1.<manifest>.<key>` keeps the existing invitation format and app deep link. The fragment is never sent to a server, stored in browser storage, or included in metadata. There are no third-party scripts or analytics.
- `tools/join.html` is the source template; `tools/join.py` adds six-language presentation copy to the existing `JOIN` copy in `tools/build.py`. Rebuild with the command above; do not edit `join/index.html` directly.
- Shared logo, fonts, cream background, language disclosure and approved drawing sticker match the introduction page. Primary action opens the app; expandable help groups instructions and link copying. Invalid links hide unusable actions. iPhone/iPad show the existing Android-only notice.
- Language selection uses `?lang=ko|en|de|fr|es|ja` and preserves the complete invitation fragment. Without an explicit language, the first supported browser language is used. Escape and outside click dismiss the menu.
- `landing.PLAY_AVAILABLE` is the single release switch for both pages. Before release, installation and Android fallback lead to the localized introduction; after release, they use the registered Google Play URL. The app-opening action remains available for installed Android builds.
- Verification: six languages at 390px; Korean/German/French/Japanese at 320px; desktop and system-dark appearance; menu keyboard handling; copy success feedback; missing-link state. App installation and a real teacher connection were not performed.
- Run `node tools/test-join.cjs` after building to check valid/invalid links, language/fragment preservation, copy fallback, iPhone/iPad detection, Android intent and both store-release states. This is a dependency-free script test; responsive appearance is checked separately in the browser.
