"""Brand presentation for teacher invitations; never persist or transmit fragment keys."""
import json
from pathlib import Path
from html import escape
from landing import COPY, PLAY_AVAILABLE

# Shared copy remains in build.JOIN. These short additions establish the page hierarchy.
UI = {
    'ko': dict(hero=['선생님이 보낸 그림,', '우리 아이의 기록으로.'], intro='처음 한 번만 연결해 두세요. 선생님이 찍은 아이의 작품을 앱에서 받아 간직할 수 있어요.', help='연결 방법이 궁금한가요?', needApp='아직 앱이 없나요?', install='앱 설치 안내', about='Dear Crayon 알아보기', manual='아래 링크를 길게 눌러 복사해 주세요.'),
    'en': dict(hero=['Art from their teacher.', 'Memories to keep.'], intro='Connect once to receive your child’s artwork in Dear Crayon, ready to keep alongside their stories.', help='Need help connecting?', needApp='Don’t have the app yet?', install='About the app', about='Discover Dear Crayon', manual='Select and copy the link below.'),
    'de': dict(hero=['Bilder aus dem Alltag.', 'Erinnerungen für Sie.'], intro='Einmal mit der Lehrkraft verbinden und die Kunstwerke Ihres Kindes in Dear Crayon erhalten und bewahren.', help='Hilfe beim Verbinden?', needApp='Sie haben die App noch nicht?', install='Zur App-Infoseite', about='Dear Crayon kennenlernen', manual='Wählen Sie den Link unten aus und kopieren Sie ihn.'),
    'fr': dict(hero=['Ses dessins en classe.', 'Vos souvenirs à garder.'], intro='Connectez-vous une fois à l’enseignant·e pour recevoir et garder les œuvres de votre enfant dans Dear Crayon.', help='Besoin d’aide pour vous connecter ?', needApp='Vous n’avez pas encore l’app ?', install='Découvrir l’app', about='Découvrir Dear Crayon', manual='Sélectionnez et copiez le lien ci-dessous.'),
    'es': dict(hero=['Sus dibujos en clase.', 'Recuerdos para guardar.'], intro='Conéctate una vez con su docente para recibir y guardar las obras de tu peque en Dear Crayon.', help='¿Necesitas ayuda para conectar?', needApp='¿Todavía no tienes la app?', install='Conoce la app', about='Descubre Dear Crayon', manual='Selecciona y copia el enlace de abajo.'),
    'ja': dict(hero=['先生が届ける絵を、', 'わが子の思い出に。'], intro='はじめに一度つなぐだけ。先生が撮ったお子さまの作品をアプリで受け取り、大切に残せます。', help='つなぎ方を知りたいときは', needApp='アプリをまだお持ちでない方へ', install='アプリのご案内', about='Dear Crayonについて', manual='下のリンクを長押ししてコピーしてください。'),
}
NAMES = dict(ko='한국어', en='English', de='Deutsch', fr='Français', es='Español', ja='日本語')


def render_join(copy, play, base):
    data = {lang: dict(values, **UI[lang], language=COPY[lang]['close'], coming=COPY[lang]['coming']) for lang, values in copy.items()}
    links = ''.join(f'<a href="?lang={lang}" hreflang="{lang}" lang="{lang}">{escape(name)}</a>' for lang, name in NAMES.items())
    template = Path(__file__).with_name('join.html').read_text(encoding='utf-8')
    # Escape < so copy cannot terminate the inline script element.
    return template.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')).replace('__PLAY__', json.dumps(play)).replace('__AVAILABLE__', json.dumps(PLAY_AVAILABLE)).replace('__BASE__', escape(base, quote=True)).replace('__LANGUAGES__', links)
