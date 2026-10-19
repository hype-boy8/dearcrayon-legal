# 디어 크레용 정적 안내 페이지 내용(5개 언어). build.py 가 읽는다.
# 블록: ('p', html) · ('ul', [html]) · ('ol', [html]) · ('dl', [(dt, dd)]) · ('box', 제목, [html])
EMAIL = 'zxcvzxcv4423@gmail.com'
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
BASE = 'https://hype-boy8.github.io/dearcrayon-legal/'

LANGS = ['ko', 'en', 'de', 'fr', 'es']

L = {}

# ───────────────────────────── 한국어
L['ko'] = dict(
    langName='한국어', name='디어 크레용',
    nav=dict(home='홈', privacy='개인정보 처리방침', terms='이용약관', delete='데이터 삭제'),
    langLabel='언어', effective='시행일 2026년 10월 19일', contact='문의',
    footer='디어 크레용 · 운영: 디어 크레용 개발자',
    index=dict(
        title='디어 크레용 · 아이의 그림과 말을 모으는 곳',
        desc='부모가 아이의 그림 사진과 목소리를 기록하고, 한 해의 기록을 도록으로 엮는 안드로이드 앱. 모든 기록은 휴대폰 안에만 저장돼요.',
        meta='안드로이드 앱 · 부모용',
        tagline='아이의 그림과 말을 모으는 곳',
        lead=[
            '디어 크레용은 부모가 아이의 그림을 사진으로 담고, 그 그림에 대해 아이가 한 말을 목소리로 남기는 앱이에요. 매달 같은 질문에 답하며 쌓인 기록은 해마다 비교해 볼 수 있고, 생일마다 한 권의 도록(아이의 한 해 기록 책)으로 엮여요.',
            '이 사이트는 디어 크레용 앱의 공식 안내 페이지예요. 개인정보 처리방침, 이용약관, 데이터 삭제 방법을 확인할 수 있어요.',
        ],
        sections=[
            ('앱에서 할 수 있는 것', [('ul', [
                '<strong>작품 담기:</strong> 아이 그림을 찍으면 종이 모서리를 찾아 반듯하게 펴 주고, 그림 이야기를 아이 목소리나 부모의 글로 남겨요.',
                '<strong>매달 이야기:</strong> 매달 아이에게 물어볼 질문과 이달의 어록, 생일마다 그림 4장과 질문 6개.',
                '<strong>성장:</strong> 같은 질문에 대한 지난달 · 작년 · 지난 생일의 답을 나란히 봐요.',
                '<strong>이달의 카드 · 도록:</strong> 그달 기록을 카드 한 장으로, 한 해 기록을 책 한 권으로 만들어 가족과 나눠요.',
            ])]),
            ('기록은 휴대폰 안에만', [('p', '회원 가입과 로그인이 없고, 개발자는 기록을 받지 않아요. 아이 이름 · 그림 · 목소리 · 글은 모두 이 휴대폰 안에만 저장돼요. 휴대폰 밖으로 나가는 것은 부모가 허락한 경우의 음성 → 글 변환 하나뿐이고, 중계 서버는 녹음과 글을 저장하지 않아요. 광고 · 사용 분석 · 위치 정보를 쓰지 않아요. 자세한 내용은 <a href="privacy.html">개인정보 처리방침</a>에 있어요.')]),
            ('요금', [('p', '앱 설치와 기록, 이달의 카드, 도록 보기 · 공유(‘미리보기’ 표시)는 무료예요. 인쇄용 고화질 도록 PDF 내려받기는 유료이며 구글 플레이 결제로 처리돼요. 개발자는 카드 정보를 받지 않아요.')]),
        ],
        operator=[('운영자', '디어 크레용 개발자 · 대한민국 · 개인 개발자'), ('서비스 이름', '디어 크레용 (Dear Crayon) · 안드로이드'), ('문의', MAIL)],
        operatorTitle='운영자와 문의',
        linksTitle='안내 문서',
        links=dict(privacy='모은 정보 · 쓰는 곳 · 지우는 법', terms='이용 조건 · 결제와 환불', delete='기록을 지우는 방법 · 단계별 안내'),
    ),
    privacy=dict(
        title='개인정보 처리방침',
        intro='디어 크레용은 부모가 아이의 그림과 목소리를 기록하는 앱이에요. 아이가 혼자 쓰도록 만든 앱이 아니며, 아이의 정보는 부모(법정대리인)가 직접 입력하고 관리해요.',
        mdEffective='시행일: 2026년 10월 19일',
        summaryTitle='한눈에 보기',
        summary=[
            '모든 기록은 이 휴대폰 안에만 저장돼요. 계정 · 자체 데이터베이스 · 광고 · 분석 · 위치 정보가 없어요.',
            '휴대폰 밖으로 나가는 것은 부모가 허락한 음성 → 글 변환뿐이에요. 중계 서버는 녹음과 글을 저장하지 않아요.',
            '유료 도록 PDF는 구글 플레이 결제로 사요. 개발자는 카드 정보를 받지 않아요.',
        ],
        sections=[
            ('1. 다루는 정보와 저장하는 곳', [('ul', [
                '아이 이름 · 생년월일 · 작가 이름 · 프로필 사진, 작품 사진, 아이 목소리 녹음, 아이가 한 말과 답, 이달의 어록, 부모 메모, 앱 설정.',
                '이 정보는 <strong>모두 이 휴대폰 안의 앱 저장소에만</strong> 저장돼요. 디어 크레용은 회원 가입 · 로그인 · 자체 데이터베이스가 없고, 개발자는 이 기록을 받지 않아요.',
                '광고, 사용 분석, 위치 정보를 쓰지 않아요.',
                '안드로이드 자동 백업(구글 드라이브)은 꺼져 있어요. 앱 안의 백업은 부모가 직접 만드는 파일(zip)이에요.',
            ])]),
            ('2. 휴대폰 밖으로 나가는 경우', [('ul', [
                '<strong>목소리를 글로 바꾸기(선택):</strong> 처음 녹음할 때 부모가 허락한 경우에만, 글로 바꿀 녹음 파일과 언어 설정을 디어 크레용 중계 서버(Cloudflare Workers)로 보내요. 중계 서버는 Cloudflare Workers AI(Whisper 음성 인식, Cloudflare, Inc., 미국)로 글을 만들어 돌려주고, 녹음과 글을 저장하지 않아요. 아이 이름 같은 다른 기록은 보내지 않아요. 언제든 설정 › 개인정보에서 끌 수 있고, 끄면 아무것도 보내지 않아요.',
                '<strong>도록 PDF 구매:</strong> 인쇄용 고화질 도록 PDF 내려받기는 구글 플레이 결제로 사요. 결제 수단과 청구 정보는 구글이 처리하고, 개발자는 카드 정보를 받지 않아요. 앱은 구매가 됐다는 확인만 받아 이 휴대폰에 기록해요. 개발자는 구글 플레이 콘솔의 주문 번호 같은 거래 정보를 환불 · 문의 처리에만 써요.',
                '<strong>부모가 직접 보내는 파일:</strong> 이달의 카드, 도록 PDF, 도록 파일, 백업 파일은 부모가 고른 앱(메신저 · 메일 등)으로 직접 보낼 때만 나가요. 받은 사람이 그 파일을 갖게 돼요.',
            ])]),
            ('3. 휴대폰 권한', [('ul', [
                '카메라: 작품 사진을 찍을 때.',
                '마이크: 아이 목소리를 녹음할 때.',
                '알림: 매달 이야기 · 생일 알림. 거절해도 나머지 기능은 그대로 쓸 수 있어요.',
            ])]),
            ('4. 보관 기간과 지우는 법', [('ul', [
                '기록은 부모가 지우기 전까지 이 휴대폰에 남아요.',
                '작품 · 답 · 어록은 앱 안에서 하나씩 지울 수 있고, 아이를 지우면 그 아이의 모든 기록과 파일이 지워져요.',
                '앱을 지우면 이 휴대폰 안의 모든 기록이 지워져요. 백업 파일과 보낸 파일은 부모가 보관한 곳에서 직접 지워 주세요.',
                '서버에 남는 기록이 없어서 따로 삭제를 요청할 데이터는 없어요.',
            ])]),
            ('5. 아이 개인정보 보호', [('ul', [
                '미국 아동 온라인 개인정보 보호법(COPPA), 유럽 개인정보 보호법(GDPR)의 아동 규정, 한국 개인정보 보호법에 따라, 아이 목소리를 서버로 보내기 전에 부모의 동의를 받아요.',
                '부모는 언제든 아이 정보를 보고 · 고치고 · 지우고, 동의를 거둘 수 있어요(모두 앱 안에서 바로).',
            ])]),
            ('6. 문의', [('ul', [
                '운영자: 디어 크레용 개발자(개인 개발자)',
                f'연락처: {MAIL}',
                f'웹: <a href="{BASE}privacy.html">{BASE}privacy.html</a>',
            ])]),
        ],
        closing='이 방침이 바뀌면 앱과 이 페이지의 시행일을 바꿔 알려 드려요.',
    ),
    terms=dict(
        title='이용약관',
        sections=[
            ('1. 약관의 적용', [('p', '이 약관은 디어 크레용(이하 “앱”)을 쓰는 데 필요한 사항을 정해요. 앱을 설치해 쓰면 이 약관에 동의한 것으로 봐요. 앱 내려받기와 결제에는 구글 플레이 서비스 약관도 함께 적용돼요.')]),
            ('2. 서비스 내용', [('p', '앱은 부모가 아이의 그림 사진 · 목소리 · 말을 기록하고, 이달의 카드와 도록(아이의 한 해 기록 책)을 만들어 보고 나누는 도구예요. 기록은 이용자의 휴대폰 안에만 저장돼요.')]),
            ('3. 이용 대상', [('ul', [
                '앱은 보호자(성인)가 쓰는 앱이에요. 아이가 혼자 쓰도록 만들지 않았어요.',
                '부모는 자신이 보호하는 아이의 정보를 기록해요. 다른 사람의 사진이나 목소리를 담을 때는 그 사람(또는 그 보호자)의 허락을 받아 주세요.',
            ])]),
            ('4. 요금과 결제', [('ul', [
                '앱 설치, 기록, 이달의 카드, 도록 보기 · 공유(‘미리보기’ 표시)는 무료예요.',
                '인쇄용 고화질 도록 PDF 내려받기는 유료예요. 가격은 결제 전에 구글 플레이 결제 화면에 표시돼요.',
                '결제는 구글 플레이 결제로 처리돼요. 결제 수단과 청구는 구글이 다루고, 개발자는 카드 정보를 받지 않아요.',
            ])]),
            ('5. 환불', [('ul', [
                '환불은 <a href="https://support.google.com/googleplay/answer/2479637?hl=ko" rel="noopener">구글 플레이 환불 정책</a>을 따라요. 구매 후 48시간 안에는 구글 플레이에서 직접 환불을 요청할 수 있고, 그 뒤에는 아래 이메일로 문의해 주세요.',
                '관련 법령이 보장하는 소비자의 권리는 이 약관으로 줄어들지 않아요.',
            ])]),
            ('6. 이용자의 기록', [('p', '앱에 담은 그림 · 목소리 · 글의 권리는 이용자(부모와 아이)에게 있어요. 개발자는 이 기록을 받거나 쓰지 않아요. 음성 → 글 변환을 켠 경우에도 녹음은 글로 바꾸는 데만 쓰이고 저장되지 않아요.')]),
            ('7. 백업은 이용자가', [('p', '기록은 휴대폰 안에만 있고 안드로이드 자동 백업이 꺼져 있어서, 휴대폰을 잃어버리거나 고장 나거나 앱을 지우면 기록을 되살릴 수 없어요. 우리 아이 › 백업 · 내보내기에서 백업 파일을 만들어 안전한 곳에 보관해 주세요.')]),
            ('8. 결과의 한계', [('ul', [
                '음성 → 글 변환은 틀릴 수 있어요. 바뀐 글은 언제든 고칠 수 있어요.',
                '도록 PDF를 인쇄하면 프린터 · 인쇄소에 따라 색과 크기가 다를 수 있어요.',
            ])]),
            ('9. 나누기', [('p', '부모가 보낸 카드 · 도록 · 백업 파일은 받은 사람이 갖게 되고, 보낸 뒤에는 앱에서 거둘 수 없어요. 누구에게 보낼지는 부모가 정해요.')]),
            ('10. 하지 말아야 할 것', [('ul', [
                '법을 어기거나 다른 사람의 권리를 침해하는 데 앱을 쓰는 것.',
                '앱을 뜯어 고치거나 결제를 우회하는 것.',
            ])]),
            ('11. 책임의 제한', [('p', '앱은 있는 그대로 제공돼요. 법령이 허용하는 범위에서 앱 사용으로 생긴 기록 손실 등 손해에 책임지지 않아요. 다만 개발자의 고의 또는 중대한 과실이 있으면 예외예요.')]),
            ('12. 변경과 중단', [('p', '기능은 바뀌거나 멈출 수 있어요. 중요한 변경은 앱 업데이트와 이 페이지로 알려 드려요. 서비스를 멈추더라도 휴대폰 안의 기록과 이미 내려받은 PDF는 그대로 쓸 수 있어요.')]),
            ('13. 준거법', [('p', '이 약관은 대한민국 법을 따라요. 다른 나라에 사는 소비자는 그 나라 법이 보장하는 보호를 그대로 받아요.')]),
            ('14. 문의', [('p', f'약관에 관한 문의는 {MAIL} 로 보내 주세요.')]),
        ],
    ),
    delete=dict(
        title='데이터 삭제 안내',
        sections=[
            ('이 페이지는', [('p', '안드로이드 앱 “디어 크레용”의 데이터 삭제 안내예요. 디어 크레용은 계정과 서버 저장이 없어서, 아이 이름 · 그림 · 목소리 · 글은 모두 이용자의 휴대폰 안에만 있어요. 그래서 이용자가 직접, 바로 지울 수 있고, 개발자가 대신 지워 드릴 데이터는 없어요.')]),
            ('방법 1. 기록을 하나씩 지우기', [('ol', [
                '<strong>작품:</strong> 작품을 열고 오른쪽 위 ⋯ › <strong>작품 삭제</strong> › 삭제. 사진 · 목소리 · 이야기가 함께 지워져요.',
                '<strong>답:</strong> 이야기 화면에서 답의 메뉴(⋯) › <strong>답 삭제</strong>.',
                '<strong>어록:</strong> 어록을 눌러 › <strong>삭제</strong>.',
            ])]),
            ('방법 2. 아이의 모든 기록 지우기', [('ol', [
                '아래 <strong>우리 아이</strong> 탭을 열어요.',
                '<strong>아이 정보 고치기</strong>를 눌러요.',
                '맨 아래 <strong>아이 삭제</strong>를 누르고 확인해요.',
            ]), ('p', '그 아이의 작품 사진 · 목소리 · 답 · 어록 · 프로필 사진이 모두 지워지고 되돌릴 수 없어요. 남겨 두고 싶으면 먼저 우리 아이 › 백업 · 내보내기로 파일을 만들어 두세요.')]),
            ('방법 3. 앱의 모든 기록 지우기', [('ol', [
                '휴대폰 <strong>설정</strong> › <strong>애플리케이션</strong> › <strong>디어 크레용</strong>을 열어요.',
                '<strong>삭제</strong>(앱 지우기)를 누르거나, 앱을 남기려면 <strong>저장공간</strong> › <strong>데이터 삭제</strong>를 눌러요.',
            ]), ('p', '휴대폰 안의 모든 기록과 설정이 바로 지워져요. 자동 백업이 꺼져 있어서 구글 드라이브에도 남지 않아요.')]),
            ('음성 변환 끄기', [('p', '우리 아이 › 오른쪽 위 ⚙ <strong>설정</strong> › <strong>개인정보</strong> › <strong>아이 목소리를 글로 바꾸기</strong>를 꺼요. 끄면 녹음을 휴대폰 밖으로 보내지 않아요. 중계 서버는 처음부터 녹음과 글을 저장하지 않아서 따로 지울 것이 없어요.')]),
            ('휴대폰 밖에 있는 파일', [('ul', [
                '<strong>백업 · 보낸 파일:</strong> 부모가 만든 백업 파일, 가족에게 보낸 카드 · 도록 파일은 저장한 곳(내 파일, 클라우드, 메신저 등)에서 직접 지워 주세요. 받은 사람의 휴대폰에 있는 파일은 받은 사람이 지워야 해요.',
                '<strong>구매 기록:</strong> 도록 PDF 구매 내역은 구글 계정의 구글 플레이 구매 기록에 남아요. 구글 계정 › 결제 및 구독에서 확인할 수 있어요.',
            ])]),
            ('지워지는 데이터와 보관 기간', [('dl', [
                ('아이 정보 · 작품 사진 · 목소리 · 답 · 어록 · 부모 메모 · 설정', '저장 위치: 이용자의 휴대폰 안 앱 저장소. 삭제 시점: 위 방법으로 지우는 즉시.'),
                ('음성 → 글 변환 요청', '중계 서버에 저장하지 않아요. 변환이 끝나면 남는 것이 없어요.'),
                ('개발자 서버에 보관되는 기록', '없어요. 계정 · 자체 데이터베이스 · 광고 · 분석 도구가 없어요.'),
            ])]),
            ('도움이 필요하면', [('p', f'위 방법으로 해결되지 않으면 {MAIL} 로 제목에 “데이터 삭제 문의”라고 적어 보내 주세요. 7일 안에 답해 드려요. 개발자가 보관한 기록이 없어서, 삭제 방법을 안내해 드려요.')]),
        ],
    ),
)

# ───────────────────────────── English
L['en'] = dict(
    langName='English', name='Dear Crayon',
    nav=dict(home='Home', privacy='Privacy Policy', terms='Terms of Use', delete='Data Deletion'),
    langLabel='Language', effective='Effective October 19, 2026', contact='Contact',
    footer='Dear Crayon · Operated by the Dear Crayon developer',
    index=dict(
        title='Dear Crayon · Little drawings, little words',
        desc='An Android app for parents to keep their child’s drawings and voice, and turn each year into a book. Everything stays on your phone.',
        meta='Android app · for parents',
        tagline='Little drawings, little words.',
        lead=[
            'Dear Crayon helps parents photograph their child’s drawings and record, in the child’s own voice, what each drawing is about. Answers to the same monthly questions build up so you can compare them year by year, and each birthday the year’s records are gathered into a book.',
            'This is the official information site for the Dear Crayon app. Here you can read the privacy policy, the terms of use and how to delete your data.',
        ],
        sections=[
            ('What you can do', [('ul', [
                '<strong>Add artwork:</strong> photograph a drawing, the app finds the paper edges and straightens it, then save the story in your child’s voice or in your own words.',
                '<strong>Monthly stories:</strong> questions to ask your child each month plus a quote of the month, and four drawings and six questions on each birthday.',
                '<strong>Growth:</strong> see last month’s, last year’s and last birthday’s answers to the same question side by side.',
                '<strong>Monthly card and book:</strong> turn a month into one card and a year into one book to share with family.',
            ])]),
            ('Everything stays on your phone', [('p', 'There is no sign-up or login, and the developer never receives your records. Your child’s name, drawings, voice and words are stored only on this phone. The only thing that ever leaves the phone is voice-to-text, if a parent allows it, and the relay server does not store recordings or text. No advertising, usage analytics or location. Details are in the <a href="privacy.html">Privacy Policy</a>.')]),
            ('Pricing', [('p', 'Installing the app, recording, monthly cards, and viewing and sharing the book (marked “Preview”) are free. Downloading the high-resolution, print-ready book PDF is a paid purchase handled by Google Play Billing. The developer never receives your card details.')]),
        ],
        operator=[('Operator', 'Dear Crayon developer · Republic of Korea · individual developer'), ('Service', 'Dear Crayon · Android'), ('Contact', MAIL)],
        operatorTitle='Operator and contact',
        linksTitle='Documents',
        links=dict(privacy='What is collected, where it goes, how to delete it', terms='Conditions of use, payment and refunds', delete='Step-by-step guide to deleting your data'),
    ),
    privacy=dict(
        title='Privacy Policy',
        intro='Dear Crayon is an app for parents to record their child’s drawings and voice. It is not designed for children to use on their own; a parent (legal guardian) enters and manages the child’s information.',
        mdEffective='Effective: October 19, 2026',
        summaryTitle='At a glance',
        summary=[
            'All records are stored only on this phone. No account, no developer database, no advertising, analytics or location.',
            'The only thing that leaves the phone is voice-to-text, if a parent allows it. The relay server does not store recordings or text.',
            'The paid book PDF is bought through Google Play Billing. The developer never receives your card details.',
        ],
        sections=[
            ('1. What we handle and where it is stored', [('ul', [
                'Child’s name, date of birth, artist name and profile photo; photos of artworks; recordings of the child’s voice; what the child said and answered; quotes; parent notes; app settings.',
                '<strong>All of it is stored only in the app’s storage on this phone.</strong> Dear Crayon has no sign-up, no login and no database of its own, and the developer never receives these records.',
                'We do not use advertising, usage analytics or location.',
                'Android Auto Backup (Google Drive) is turned off. Backups inside the app are files (zip) that a parent creates.',
            ])]),
            ('2. When something leaves the phone', [('ul', [
                '<strong>Voice-to-text (optional):</strong> only if a parent allows it at the first recording, the recording to be transcribed and the language setting are sent to the Dear Crayon relay server (Cloudflare Workers). The relay server has the text produced by Cloudflare Workers AI (Whisper speech recognition, Cloudflare, Inc., United States), returns it, and stores neither the recording nor the text. No other records, such as the child’s name, are sent. You can turn this off anytime in Settings › Privacy; when off, nothing is sent.',
                '<strong>Buying the book PDF:</strong> the high-resolution, print-ready book PDF is bought through Google Play Billing. Google handles the payment method and billing details; the developer never receives your card details. The app only receives confirmation that the purchase went through and records it on this phone. The developer uses transaction details in the Google Play Console, such as the order number, only to handle refunds and support requests.',
                '<strong>Files a parent shares:</strong> monthly cards, book PDFs, book files and backup files leave the phone only when a parent sends them through an app they choose (messaging, email, etc.). The recipient then has that file.',
            ])]),
            ('3. Phone permissions', [('ul', [
                'Camera: to photograph artworks.',
                'Microphone: to record the child’s voice.',
                'Notifications: monthly story and birthday reminders. Everything else still works if you decline.',
            ])]),
            ('4. Retention and deletion', [('ul', [
                'Records stay on this phone until a parent deletes them.',
                'Artworks, answers and quotes can be deleted one by one in the app; deleting a child deletes all of that child’s records and files.',
                'Deleting the app deletes every record on this phone. Please delete backup files and shared files yourself wherever you saved them.',
                'Because nothing is kept on a server, there is no data to request deletion of separately.',
            ])]),
            ('5. Children’s privacy', [('ul', [
                'In line with COPPA (US), the GDPR rules for children (EU/UK) and the Korean Personal Information Protection Act, we ask for a parent’s consent before any of the child’s voice is sent to a server.',
                'Parents can review, correct or delete the child’s information and withdraw consent at any time, directly in the app.',
            ])]),
            ('6. Contact', [('ul', [
                'Operator: Dear Crayon developer (individual developer)',
                f'Email: {MAIL}',
                f'Web: <a href="{BASE}en/privacy.html">{BASE}en/privacy.html</a>',
            ])]),
        ],
        closing='If this policy changes, we will update the effective date in the app and on this page.',
    ),
    terms=dict(
        title='Terms of Use',
        sections=[
            ('1. Scope', [('p', 'These terms set out what you need to know to use Dear Crayon (the “app”). By installing and using the app you agree to these terms. Google Play’s Terms of Service also apply to downloading the app and to payments.')]),
            ('2. The service', [('p', 'The app is a tool for parents to record their child’s drawing photos, voice and words, and to make, view and share monthly cards and books (a year of the child’s records). Records are stored only on the user’s phone.')]),
            ('3. Who can use it', [('ul', [
                'The app is for parents and guardians (adults). It is not designed for children to use on their own.',
                'Parents record information about the children in their care. Please get permission from anyone else (or their guardian) before adding their photo or voice.',
            ])]),
            ('4. Pricing and payment', [('ul', [
                'Installing the app, recording, monthly cards, and viewing and sharing the book (marked “Preview”) are free.',
                'Downloading the high-resolution, print-ready book PDF is paid. The price is shown on the Google Play payment screen before you pay.',
                'Payments are processed by Google Play Billing. Google handles payment methods and billing; the developer never receives your card details.',
            ])]),
            ('5. Refunds', [('ul', [
                'Refunds follow the <a href="https://support.google.com/googleplay/answer/2479637?hl=en" rel="noopener">Google Play refund policy</a>. Within 48 hours of purchase you can request a refund directly on Google Play; after that, please contact us at the email below.',
                'These terms do not limit any consumer rights you have under applicable law.',
            ])]),
            ('6. Your records', [('p', 'The rights to the drawings, voice and words you add belong to you (the parent and child). The developer does not receive or use these records. If voice-to-text is on, recordings are used only to produce the text and are not stored.')]),
            ('7. Backups are up to you', [('p', 'Records live only on your phone and Android Auto Backup is off, so if your phone is lost or broken or you delete the app, the records cannot be recovered. Please create a backup file in My Kids › Backup &amp; export and keep it somewhere safe.')]),
            ('8. Limits of the results', [('ul', [
                'Voice-to-text can make mistakes. You can edit the text at any time.',
                'When the book PDF is printed, colors and size may vary by printer or print shop.',
            ])]),
            ('9. Sharing', [('p', 'Cards, books and backup files a parent sends belong to the recipient once sent and cannot be recalled from the app. The parent decides who to send them to.')]),
            ('10. What not to do', [('ul', [
                'Using the app to break the law or infringe the rights of others.',
                'Modifying the app or circumventing payment.',
            ])]),
            ('11. Limitation of liability', [('p', 'The app is provided as is. To the extent permitted by law, the developer is not liable for damage such as loss of records arising from use of the app, except in cases of intent or gross negligence.')]),
            ('12. Changes and discontinuation', [('p', 'Features may change or stop. Important changes will be announced through app updates and on this page. Even if the service stops, the records on your phone and any PDFs you have already downloaded remain usable.')]),
            ('13. Governing law', [('p', 'These terms are governed by the laws of the Republic of Korea. Consumers living in other countries keep the protections their local law gives them.')]),
            ('14. Contact', [('p', f'Questions about these terms: {MAIL}')]),
        ],
    ),
    delete=dict(
        title='Data Deletion',
        sections=[
            ('About this page', [('p', 'This page explains how to delete data in the Android app “Dear Crayon”. Dear Crayon has no account and no server storage, so your child’s name, drawings, voice and words exist only on your phone. You can delete them yourself, immediately, and there is no data the developer could delete on your behalf.')]),
            ('Option 1. Delete individual records', [('ol', [
                '<strong>Artwork:</strong> open the artwork, tap ⋯ at the top right › <strong>Delete artwork</strong> › Delete. The photo, voice and story are deleted together.',
                '<strong>Answer:</strong> on the story screen, open the answer’s menu (⋯) › <strong>Delete answer</strong>.',
                '<strong>Quote:</strong> tap the quote › <strong>Delete</strong>.',
            ])]),
            ('Option 2. Delete all of a child’s records', [('ol', [
                'Open the <strong>My Kids</strong> tab at the bottom.',
                'Tap <strong>Edit child info</strong>.',
                'Tap <strong>Delete child</strong> at the bottom and confirm.',
            ]), ('p', 'All of that child’s artwork photos, voice recordings, answers, quotes and profile photo are deleted and cannot be restored. To keep a copy, first create a file in My Kids › Backup &amp; export.')]),
            ('Option 3. Delete everything in the app', [('ol', [
                'Open your phone’s <strong>Settings</strong> › <strong>Apps</strong> › <strong>Dear Crayon</strong>.',
                'Tap <strong>Uninstall</strong>, or to keep the app, tap <strong>Storage</strong> › <strong>Clear data</strong>.',
            ]), ('p', 'All records and settings on the phone are deleted immediately. Because Auto Backup is off, nothing remains in Google Drive either.')]),
            ('Turn off voice-to-text', [('p', 'Go to My Kids › ⚙ <strong>Settings</strong> at the top right › <strong>Privacy</strong> and turn off <strong>Turn voice into text</strong>. Recordings will no longer leave the phone. The relay server never stores recordings or text, so there is nothing there to delete.')]),
            ('Files outside the phone', [('ul', [
                '<strong>Backups and shared files:</strong> please delete backup files you created and card or book files you sent to family from wherever you saved them (Files, cloud storage, messaging apps, etc.). Files on a recipient’s phone must be deleted by the recipient.',
                '<strong>Purchase history:</strong> book PDF purchases remain in your Google account’s Google Play purchase history, which you can see under Google Account › Payments &amp; subscriptions.',
            ])]),
            ('What is deleted and how long it is kept', [('dl', [
                ('Child info, artwork photos, voice, answers, quotes, parent notes, settings', 'Stored in the app’s storage on the user’s phone. Deleted immediately when you use the options above.'),
                ('Voice-to-text requests', 'Not stored on the relay server. Nothing remains once the text is returned.'),
                ('Records kept on a developer server', 'None. There is no account, no developer database, no advertising or analytics tools.'),
            ])]),
            ('Need help?', [('p', f'If these steps don’t solve it, email {MAIL} with the subject “Data deletion”. We reply within 7 days. Since the developer holds no records, we will guide you through the deletion steps.')]),
        ],
    ),
)

# ───────────────────────────── Deutsch
L['de'] = dict(
    langName='Deutsch', name='Dear Crayon',
    nav=dict(home='Start', privacy='Datenschutz', terms='Nutzungsbedingungen', delete='Daten löschen'),
    langLabel='Sprache', effective='Gültig ab 19. Oktober 2026', contact='Kontakt',
    footer='Dear Crayon · Anbieter: Dear-Crayon-Entwickler',
    index=dict(
        title='Dear Crayon · Kleine Bilder, kleine Worte',
        desc='Eine Android-App für Eltern, um die Bilder und die Stimme ihres Kindes festzuhalten und jedes Jahr zu einem Buch zu machen. Alles bleibt auf deinem Handy.',
        meta='Android-App · für Eltern',
        tagline='Kleine Bilder, kleine Worte.',
        lead=[
            'Mit Dear Crayon fotografieren Eltern die Bilder ihres Kindes und halten mit der Stimme des Kindes fest, was es dazu erzählt. Antworten auf dieselben Monatsfragen lassen sich Jahr für Jahr vergleichen, und zu jedem Geburtstag werden die Einträge des Jahres zu einem Buch.',
            'Dies ist die offizielle Informationsseite der App Dear Crayon mit Datenschutzerklärung, Nutzungsbedingungen und einer Anleitung zum Löschen der Daten.',
        ],
        sections=[
            ('Was die App kann', [('ul', [
                '<strong>Kunstwerk hinzufügen:</strong> Bild fotografieren, die App findet die Papierkanten und richtet es gerade aus; die Geschichte dazu mit der Stimme des Kindes oder in eigenen Worten speichern.',
                '<strong>Monatsgeschichten:</strong> Fragen für jeden Monat und das Zitat des Monats, zu jedem Geburtstag vier Bilder und sechs Fragen.',
                '<strong>Entwicklung:</strong> die Antworten vom letzten Monat, letzten Jahr und letzten Geburtstag auf dieselbe Frage nebeneinander.',
                '<strong>Monatskarte und Buch:</strong> einen Monat als Karte, ein Jahr als Buch – zum Teilen mit der Familie.',
            ])]),
            ('Alles bleibt auf deinem Handy', [('p', 'Es gibt keine Registrierung und keine Anmeldung, und der Entwickler erhält deine Einträge nie. Name, Bilder, Stimme und Worte deines Kindes werden nur auf diesem Handy gespeichert. Das Einzige, was das Handy verlässt, ist die Sprache-zu-Text-Umwandlung, wenn ein Elternteil sie erlaubt – und der Relay-Server speichert weder Aufnahmen noch Text. Keine Werbung, keine Nutzungsanalyse, kein Standort. Einzelheiten in der <a href="privacy.html">Datenschutzerklärung</a>.')]),
            ('Preise', [('p', 'Installation, Einträge, Monatskarten sowie Ansehen und Teilen des Buchs (mit „Vorschau“ gekennzeichnet) sind kostenlos. Der Download des hochauflösenden, druckfertigen Buch-PDFs ist kostenpflichtig und läuft über Google Play Billing. Der Entwickler erhält keine Kartendaten.')]),
        ],
        operator=[('Anbieter', 'Dear-Crayon-Entwickler · Republik Korea · Einzelentwickler'), ('Dienst', 'Dear Crayon · Android'), ('Kontakt', MAIL)],
        operatorTitle='Anbieter und Kontakt',
        linksTitle='Dokumente',
        links=dict(privacy='Welche Daten, wohin sie gehen, wie man sie löscht', terms='Nutzungsbedingungen, Zahlung und Erstattung', delete='Schritt-für-Schritt-Anleitung zum Löschen'),
    ),
    privacy=dict(
        title='Datenschutzerklärung',
        intro='Dear Crayon ist eine App für Eltern, um die Bilder und die Stimme ihres Kindes festzuhalten. Sie ist nicht dafür gedacht, dass Kinder sie allein benutzen; die Angaben zum Kind trägt ein Elternteil (Erziehungsberechtigte) ein und verwaltet sie.',
        mdEffective='Gültig ab: 19. Oktober 2026',
        summaryTitle='Auf einen Blick',
        summary=[
            'Alle Einträge werden nur auf diesem Handy gespeichert. Kein Konto, keine Datenbank des Entwicklers, keine Werbung, Analyse oder Standortdaten.',
            'Das Handy verlässt nur die Sprache-zu-Text-Umwandlung, wenn ein Elternteil sie erlaubt. Der Relay-Server speichert weder Aufnahmen noch Text.',
            'Das kostenpflichtige Buch-PDF wird über Google Play Billing gekauft. Der Entwickler erhält keine Kartendaten.',
        ],
        sections=[
            ('1. Welche Daten wir verarbeiten und wo sie gespeichert werden', [('ul', [
                'Name, Geburtsdatum, Künstlername und Profilfoto des Kindes; Fotos der Kunstwerke; Aufnahmen der Stimme des Kindes; was das Kind gesagt und geantwortet hat; Zitate; Notizen der Eltern; App-Einstellungen.',
                '<strong>Alles wird nur im App-Speicher auf diesem Handy gespeichert.</strong> Dear Crayon hat keine Registrierung, keine Anmeldung und keine eigene Datenbank, und der Entwickler erhält diese Einträge nie.',
                'Wir verwenden keine Werbung, keine Nutzungsanalyse und keinen Standort.',
                'Die automatische Android-Sicherung (Google Drive) ist ausgeschaltet. Sicherungen in der App sind Dateien (zip), die ein Elternteil selbst erstellt.',
            ])]),
            ('2. Wann etwas das Handy verlässt', [('ul', [
                '<strong>Sprache-zu-Text (freiwillig):</strong> Nur wenn ein Elternteil es bei der ersten Aufnahme erlaubt, werden die zu verschriftende Aufnahme und die Spracheinstellung an den Dear-Crayon-Relay-Server (Cloudflare Workers) gesendet. Der Relay-Server lässt den Text von Cloudflare Workers AI (Whisper-Spracherkennung, Cloudflare, Inc., USA) erstellen, gibt ihn zurück und speichert weder Aufnahme noch Text. Andere Einträge, etwa der Name des Kindes, werden nicht gesendet. Du kannst das jederzeit unter Einstellungen › Datenschutz ausschalten; dann wird nichts gesendet.',
                '<strong>Kauf des Buch-PDFs:</strong> Das hochauflösende, druckfertige Buch-PDF wird über Google Play Billing gekauft. Zahlungsmittel und Abrechnungsdaten verarbeitet Google; der Entwickler erhält keine Kartendaten. Die App erhält nur die Bestätigung, dass der Kauf erfolgt ist, und speichert sie auf diesem Handy. Transaktionsdaten in der Google Play Console, etwa die Bestellnummer, nutzt der Entwickler nur für Erstattungen und Anfragen.',
                '<strong>Dateien, die Eltern teilen:</strong> Monatskarten, Buch-PDFs, Buchdateien und Sicherungsdateien verlassen das Handy nur, wenn ein Elternteil sie über eine selbst gewählte App (Messenger, E-Mail usw.) sendet. Die Empfänger haben dann diese Datei.',
            ])]),
            ('3. Berechtigungen', [('ul', [
                'Kamera: zum Fotografieren der Kunstwerke.',
                'Mikrofon: zum Aufnehmen der Stimme des Kindes.',
                'Benachrichtigungen: Erinnerungen an Monatsgeschichten und Geburtstage. Lehnst du ab, funktioniert alles andere weiter.',
            ])]),
            ('4. Speicherdauer und Löschen', [('ul', [
                'Einträge bleiben auf diesem Handy, bis ein Elternteil sie löscht.',
                'Kunstwerke, Antworten und Zitate lassen sich in der App einzeln löschen; wird ein Kind gelöscht, werden alle seine Einträge und Dateien gelöscht.',
                'Wird die App gelöscht, sind alle Einträge auf diesem Handy gelöscht. Sicherungen und geteilte Dateien löschst du bitte selbst dort, wo du sie gespeichert hast.',
                'Da nichts auf einem Server gespeichert wird, gibt es keine Daten, deren Löschung gesondert beantragt werden müsste.',
            ])]),
            ('5. Datenschutz für Kinder', [('ul', [
                'Gemäß DSGVO (Kinder), COPPA (USA) und dem koreanischen Datenschutzgesetz bitten wir um die Einwilligung eines Elternteils, bevor die Stimme des Kindes an einen Server gesendet wird.',
                'Eltern können die Angaben zum Kind jederzeit direkt in der App ansehen, berichtigen oder löschen und ihre Einwilligung widerrufen.',
            ])]),
            ('6. Kontakt', [('ul', [
                'Anbieter: Dear-Crayon-Entwickler (Einzelentwickler)',
                f'E-Mail: {MAIL}',
                f'Web: <a href="{BASE}de/privacy.html">{BASE}de/privacy.html</a>',
            ])]),
        ],
        closing='Ändert sich diese Erklärung, aktualisieren wir das Datum in der App und auf dieser Seite.',
    ),
    terms=dict(
        title='Nutzungsbedingungen',
        sections=[
            ('1. Geltungsbereich', [('p', 'Diese Bedingungen regeln die Nutzung von Dear Crayon (die „App“). Mit der Installation und Nutzung der App stimmst du ihnen zu. Für Download und Zahlungen gelten zusätzlich die Nutzungsbedingungen von Google Play.')]),
            ('2. Leistung', [('p', 'Die App ist ein Werkzeug für Eltern, um Bildfotos, Stimme und Worte ihres Kindes festzuhalten und Monatskarten und Bücher (ein Jahr an Einträgen) zu erstellen, anzusehen und zu teilen. Die Einträge werden nur auf dem Handy der Nutzer gespeichert.')]),
            ('3. Wer die App nutzt', [('ul', [
                'Die App ist für Eltern und Erziehungsberechtigte (Erwachsene). Sie ist nicht dafür gedacht, dass Kinder sie allein benutzen.',
                'Eltern halten Angaben zu den Kindern in ihrer Obhut fest. Bitte hol die Erlaubnis anderer Personen (oder ihrer Erziehungsberechtigten) ein, bevor du deren Foto oder Stimme aufnimmst.',
            ])]),
            ('4. Preise und Zahlung', [('ul', [
                'Installation, Einträge, Monatskarten sowie Ansehen und Teilen des Buchs (mit „Vorschau“ gekennzeichnet) sind kostenlos.',
                'Der Download des hochauflösenden, druckfertigen Buch-PDFs ist kostenpflichtig. Der Preis wird vor der Zahlung im Zahlungsfenster von Google Play angezeigt.',
                'Zahlungen werden über Google Play Billing abgewickelt. Zahlungsmittel und Abrechnung verwaltet Google; der Entwickler erhält keine Kartendaten.',
            ])]),
            ('5. Erstattung', [('ul', [
                'Erstattungen richten sich nach der <a href="https://support.google.com/googleplay/answer/2479637?hl=de" rel="noopener">Erstattungsrichtlinie von Google Play</a>. Innerhalb von 48 Stunden nach dem Kauf kannst du die Erstattung direkt bei Google Play beantragen; danach schreib uns bitte an die unten stehende E-Mail.',
                'Gesetzliche Verbraucherrechte, einschließlich eines etwaigen Widerrufsrechts, bleiben unberührt.',
            ])]),
            ('6. Deine Einträge', [('p', 'Die Rechte an den Bildern, Aufnahmen und Worten, die du hinzufügst, liegen bei dir (Eltern und Kind). Der Entwickler erhält und nutzt diese Einträge nicht. Ist Sprache-zu-Text eingeschaltet, werden Aufnahmen nur zur Umwandlung in Text verwendet und nicht gespeichert.')]),
            ('7. Sicherung ist deine Sache', [('p', 'Die Einträge liegen nur auf deinem Handy, und die automatische Android-Sicherung ist aus. Geht das Handy verloren oder kaputt oder wird die App gelöscht, lassen sich die Einträge nicht wiederherstellen. Erstelle bitte unter Meine Kinder › Sichern &amp; exportieren eine Sicherungsdatei und bewahre sie sicher auf.')]),
            ('8. Grenzen der Ergebnisse', [('ul', [
                'Die Sprache-zu-Text-Umwandlung kann Fehler machen. Du kannst den Text jederzeit bearbeiten.',
                'Beim Drucken des Buch-PDFs können Farben und Größe je nach Drucker oder Druckerei abweichen.',
            ])]),
            ('9. Teilen', [('p', 'Karten, Bücher und Sicherungsdateien, die ein Elternteil sendet, gehören nach dem Senden den Empfängern und lassen sich nicht über die App zurückholen. An wen gesendet wird, entscheiden die Eltern.')]),
            ('10. Nicht erlaubt', [('ul', [
                'Die App für rechtswidrige Zwecke oder zur Verletzung der Rechte anderer zu nutzen.',
                'Die App zu verändern oder die Zahlung zu umgehen.',
            ])]),
            ('11. Haftungsbeschränkung', [('p', 'Die App wird so bereitgestellt, wie sie ist. Soweit gesetzlich zulässig, haftet der Entwickler nicht für Schäden wie den Verlust von Einträgen durch die Nutzung der App; ausgenommen sind Vorsatz und grobe Fahrlässigkeit sowie die gesetzlich zwingende Haftung.')]),
            ('12. Änderungen und Einstellung', [('p', 'Funktionen können sich ändern oder eingestellt werden. Wichtige Änderungen kündigen wir über App-Updates und auf dieser Seite an. Auch wenn der Dienst eingestellt wird, bleiben die Einträge auf deinem Handy und bereits heruntergeladene PDFs nutzbar.')]),
            ('13. Anwendbares Recht', [('p', 'Es gilt das Recht der Republik Korea. Verbraucherinnen und Verbraucher in anderen Ländern behalten den Schutz der zwingenden Vorschriften ihres Wohnsitzlandes.')]),
            ('14. Kontakt', [('p', f'Fragen zu diesen Bedingungen: {MAIL}')]),
        ],
    ),
    delete=dict(
        title='Daten löschen',
        sections=[
            ('Über diese Seite', [('p', 'Diese Seite erklärt, wie du Daten in der Android-App „Dear Crayon“ löschst. Dear Crayon hat kein Konto und keinen Serverspeicher; Name, Bilder, Stimme und Worte deines Kindes liegen nur auf deinem Handy. Du kannst sie selbst sofort löschen, und es gibt keine Daten, die der Entwickler für dich löschen könnte.')]),
            ('Weg 1. Einzelne Einträge löschen', [('ol', [
                '<strong>Kunstwerk:</strong> Kunstwerk öffnen, oben rechts auf ⋯ tippen › <strong>Kunstwerk löschen</strong> › Löschen. Foto, Stimme und Geschichte werden zusammen gelöscht.',
                '<strong>Antwort:</strong> Im Geschichten-Bildschirm das Menü der Antwort (⋯) öffnen › <strong>Antwort löschen</strong>.',
                '<strong>Zitat:</strong> Auf das Zitat tippen › <strong>Löschen</strong>.',
            ])]),
            ('Weg 2. Alle Einträge eines Kindes löschen', [('ol', [
                'Unten den Tab <strong>Meine Kinder</strong> öffnen.',
                'Auf <strong>Angaben zum Kind bearbeiten</strong> tippen.',
                'Ganz unten auf <strong>Kind löschen</strong> tippen und bestätigen.',
            ]), ('p', 'Alle Kunstwerkfotos, Aufnahmen, Antworten, Zitate und das Profilfoto dieses Kindes werden gelöscht und lassen sich nicht wiederherstellen. Möchtest du eine Kopie behalten, erstelle vorher unter Meine Kinder › Sichern &amp; exportieren eine Datei.')]),
            ('Weg 3. Alles in der App löschen', [('ol', [
                'Auf dem Handy <strong>Einstellungen</strong> › <strong>Apps</strong> › <strong>Dear Crayon</strong> öffnen.',
                'Auf <strong>Deinstallieren</strong> tippen – oder, um die App zu behalten, <strong>Speicher</strong> › <strong>Daten löschen</strong>.',
            ]), ('p', 'Alle Einträge und Einstellungen auf dem Handy werden sofort gelöscht. Da die automatische Sicherung aus ist, bleibt auch in Google Drive nichts zurück.')]),
            ('Sprache-zu-Text ausschalten', [('p', 'Meine Kinder › oben rechts ⚙ <strong>Einstellungen</strong> › <strong>Datenschutz</strong> › <strong>Stimme in Text umwandeln</strong> ausschalten. Dann verlassen Aufnahmen das Handy nicht mehr. Der Relay-Server speichert ohnehin weder Aufnahmen noch Text, dort gibt es also nichts zu löschen.')]),
            ('Dateien außerhalb des Handys', [('ul', [
                '<strong>Sicherungen und geteilte Dateien:</strong> Selbst erstellte Sicherungen und an die Familie gesendete Karten- oder Buchdateien löschst du bitte dort, wo du sie gespeichert hast (Dateien, Cloud, Messenger usw.). Dateien auf dem Handy der Empfänger müssen diese selbst löschen.',
                '<strong>Kaufverlauf:</strong> Käufe des Buch-PDFs bleiben im Google-Play-Kaufverlauf deines Google-Kontos, einsehbar unter Google-Konto › Zahlungen und Abos.',
            ])]),
            ('Was gelöscht wird und wie lange es bleibt', [('dl', [
                ('Angaben zum Kind, Kunstwerkfotos, Stimme, Antworten, Zitate, Notizen der Eltern, Einstellungen', 'Gespeichert im App-Speicher auf dem Handy der Nutzer. Sofort gelöscht, wenn du einen der Wege oben nutzt.'),
                ('Sprache-zu-Text-Anfragen', 'Werden auf dem Relay-Server nicht gespeichert. Nach der Rückgabe des Textes bleibt nichts zurück.'),
                ('Einträge auf einem Server des Entwicklers', 'Keine. Es gibt kein Konto, keine Datenbank des Entwicklers, keine Werbe- oder Analysetools.'),
            ])]),
            ('Hilfe', [('p', f'Wenn diese Schritte nicht helfen, schreib an {MAIL} mit dem Betreff „Daten löschen“. Wir antworten innerhalb von 7 Tagen. Da der Entwickler keine Einträge speichert, erklären wir dir die Schritte zum Löschen.')]),
        ],
    ),
)

# ───────────────────────────── Français
L['fr'] = dict(
    langName='Français', name='Dear Crayon',
    nav=dict(home='Accueil', privacy='Confidentialité', terms='Conditions d’utilisation', delete='Suppression des données'),
    langLabel='Langue', effective='En vigueur le 19 octobre 2026', contact='Contact',
    footer='Dear Crayon · Éditeur : développeur de Dear Crayon',
    index=dict(
        title='Dear Crayon · Petits dessins, petits mots',
        desc='Une application Android pour garder les dessins et la voix de votre enfant, et faire de chaque année un livre. Tout reste sur votre téléphone.',
        meta='Application Android · pour les parents',
        tagline='Petits dessins, petits mots.',
        lead=[
            'Avec Dear Crayon, les parents photographient les dessins de leur enfant et enregistrent, avec sa propre voix, ce qu’il raconte sur chacun. Les réponses aux mêmes questions mensuelles se comparent d’une année à l’autre, et à chaque anniversaire les souvenirs de l’année deviennent un livre.',
            'Ce site est la page d’information officielle de l’application Dear Crayon : politique de confidentialité, conditions d’utilisation et marche à suivre pour supprimer vos données.',
        ],
        sections=[
            ('Ce que permet l’application', [('ul', [
                '<strong>Ajouter une œuvre :</strong> photographiez un dessin, l’application trouve les bords de la feuille et la redresse, puis gardez son histoire avec la voix de l’enfant ou vos propres mots.',
                '<strong>Histoires du mois :</strong> des questions à poser chaque mois et la citation du mois, quatre dessins et six questions à chaque anniversaire.',
                '<strong>Grandir :</strong> les réponses du mois dernier, de l’an dernier et du dernier anniversaire à la même question, côte à côte.',
                '<strong>Carte du mois et livre :</strong> un mois en une carte, une année en un livre, à partager en famille.',
            ])]),
            ('Tout reste sur votre téléphone', [('p', 'Pas d’inscription ni de connexion, et le développeur ne reçoit jamais vos données. Le prénom, les dessins, la voix et les mots de votre enfant sont conservés uniquement sur ce téléphone. La seule chose qui quitte le téléphone est la transcription de la voix, si un parent l’autorise, et le serveur relais ne conserve ni enregistrement ni texte. Ni publicité, ni mesure d’audience, ni localisation. Détails dans la <a href="privacy.html">politique de confidentialité</a>.')]),
            ('Tarifs', [('p', 'L’installation, les enregistrements, les cartes du mois ainsi que la consultation et le partage du livre (marqué « Aperçu ») sont gratuits. Le téléchargement du PDF du livre en haute résolution, prêt à imprimer, est payant et passe par la facturation Google Play. Le développeur ne reçoit jamais vos données bancaires.')]),
        ],
        operator=[('Éditeur', 'Développeur de Dear Crayon · République de Corée · développeur indépendant'), ('Service', 'Dear Crayon · Android'), ('Contact', MAIL)],
        operatorTitle='Éditeur et contact',
        linksTitle='Documents',
        links=dict(privacy='Ce qui est collecté, où cela va, comment le supprimer', terms='Conditions d’utilisation, paiement et remboursement', delete='Guide pas à pas pour supprimer vos données'),
    ),
    privacy=dict(
        title='Politique de confidentialité',
        intro='Dear Crayon est une application destinée aux parents pour garder les dessins et la voix de leur enfant. Elle n’est pas conçue pour être utilisée seule par un enfant ; un parent (représentant légal) saisit et gère les informations de l’enfant.',
        mdEffective='En vigueur le : 19 octobre 2026',
        summaryTitle='En bref',
        summary=[
            'Toutes les données sont conservées uniquement sur ce téléphone. Ni compte, ni base de données du développeur, ni publicité, mesure d’audience ou localisation.',
            'Seule la transcription de la voix quitte le téléphone, si un parent l’autorise. Le serveur relais ne conserve ni enregistrement ni texte.',
            'Le PDF payant du livre s’achète via la facturation Google Play. Le développeur ne reçoit jamais vos données bancaires.',
        ],
        sections=[
            ('1. Ce que nous traitons et où c’est conservé', [('ul', [
                'Prénom, date de naissance, nom d’artiste et photo de profil de l’enfant ; photos des œuvres ; enregistrements de la voix de l’enfant ; ce que l’enfant a dit et répondu ; citations ; notes des parents ; réglages de l’application.',
                '<strong>Tout est conservé uniquement dans le stockage de l’application sur ce téléphone.</strong> Dear Crayon n’a ni inscription, ni connexion, ni base de données propre, et le développeur ne reçoit jamais ces données.',
                'Nous n’utilisons ni publicité, ni mesure d’audience, ni localisation.',
                'La sauvegarde automatique d’Android (Google Drive) est désactivée. Les sauvegardes de l’application sont des fichiers (zip) créés par un parent.',
            ])]),
            ('2. Quand quelque chose quitte le téléphone', [('ul', [
                '<strong>Voix en texte (facultatif) :</strong> uniquement si un parent l’autorise lors du premier enregistrement, l’enregistrement à transcrire et le réglage de langue sont envoyés au serveur relais de Dear Crayon (Cloudflare Workers). Le serveur relais fait produire le texte par Cloudflare Workers AI (reconnaissance vocale Whisper, Cloudflare, Inc., États-Unis), le renvoie, et ne conserve ni l’enregistrement ni le texte. Aucune autre donnée, comme le prénom de l’enfant, n’est envoyée. Vous pouvez désactiver cette fonction à tout moment dans Réglages › Confidentialité ; rien n’est alors envoyé.',
                '<strong>Achat du PDF du livre :</strong> le PDF du livre en haute résolution, prêt à imprimer, s’achète via la facturation Google Play. Google traite le moyen de paiement et les données de facturation ; le développeur ne reçoit jamais vos données bancaires. L’application reçoit seulement la confirmation de l’achat et l’enregistre sur ce téléphone. Le développeur n’utilise les informations de transaction de la Google Play Console, comme le numéro de commande, que pour traiter les remboursements et les demandes d’aide.',
                '<strong>Fichiers partagés par un parent :</strong> les cartes du mois, PDF des livres, fichiers de livre et sauvegardes ne quittent le téléphone que lorsqu’un parent les envoie via l’application de son choix (messagerie, e-mail, etc.). Le destinataire dispose alors de ce fichier.',
            ])]),
            ('3. Autorisations du téléphone', [('ul', [
                'Appareil photo : pour photographier les œuvres.',
                'Micro : pour enregistrer la voix de l’enfant.',
                'Notifications : rappels des histoires du mois et des anniversaires. Tout le reste fonctionne si vous refusez.',
            ])]),
            ('4. Durée de conservation et suppression', [('ul', [
                'Les données restent sur ce téléphone jusqu’à ce qu’un parent les supprime.',
                'Les œuvres, réponses et citations peuvent être supprimées une par une dans l’application ; supprimer un enfant efface toutes ses données et tous ses fichiers.',
                'Supprimer l’application efface toutes les données de ce téléphone. Supprimez vous-même les sauvegardes et fichiers partagés là où vous les avez enregistrés.',
                'Comme rien n’est conservé sur un serveur, il n’y a aucune donnée dont il faudrait demander séparément la suppression.',
            ])]),
            ('5. Protection des données des enfants', [('ul', [
                'Conformément au RGPD (enfants), au COPPA (États-Unis) et à la loi coréenne sur la protection des données personnelles, nous demandons le consentement d’un parent avant d’envoyer la voix de l’enfant à un serveur.',
                'Les parents peuvent à tout moment consulter, corriger ou supprimer les informations de l’enfant et retirer leur consentement, directement dans l’application.',
            ])]),
            ('6. Contact', [('ul', [
                'Éditeur : développeur de Dear Crayon (développeur indépendant)',
                f'E-mail : {MAIL}',
                f'Web : <a href="{BASE}fr/privacy.html">{BASE}fr/privacy.html</a>',
            ])]),
        ],
        closing='Si cette politique change, nous mettrons à jour la date d’entrée en vigueur dans l’application et sur cette page.',
    ),
    terms=dict(
        title='Conditions d’utilisation',
        sections=[
            ('1. Champ d’application', [('p', 'Ces conditions précisent ce qu’il faut savoir pour utiliser Dear Crayon (l’« application »). En installant et en utilisant l’application, vous les acceptez. Les conditions d’utilisation de Google Play s’appliquent aussi au téléchargement et aux paiements.')]),
            ('2. Le service', [('p', 'L’application permet aux parents de garder les photos des dessins, la voix et les mots de leur enfant, et de créer, consulter et partager des cartes du mois et des livres (une année de souvenirs). Les données sont conservées uniquement sur le téléphone de l’utilisateur.')]),
            ('3. Qui peut l’utiliser', [('ul', [
                'L’application est destinée aux parents et représentants légaux (adultes). Elle n’est pas conçue pour être utilisée seule par un enfant.',
                'Les parents enregistrent les informations des enfants dont ils ont la charge. Demandez l’autorisation de toute autre personne (ou de son représentant légal) avant d’ajouter sa photo ou sa voix.',
            ])]),
            ('4. Tarifs et paiement', [('ul', [
                'L’installation, les enregistrements, les cartes du mois ainsi que la consultation et le partage du livre (marqué « Aperçu ») sont gratuits.',
                'Le téléchargement du PDF du livre en haute résolution, prêt à imprimer, est payant. Le prix s’affiche sur l’écran de paiement Google Play avant l’achat.',
                'Les paiements sont traités par la facturation Google Play. Google gère les moyens de paiement et la facturation ; le développeur ne reçoit jamais vos données bancaires.',
            ])]),
            ('5. Remboursements', [('ul', [
                'Les remboursements suivent la <a href="https://support.google.com/googleplay/answer/2479637?hl=fr" rel="noopener">politique de remboursement de Google Play</a>. Dans les 48 heures suivant l’achat, vous pouvez demander un remboursement directement sur Google Play ; ensuite, écrivez-nous à l’adresse ci-dessous.',
                'Ces conditions ne limitent pas les droits que vous accorde la loi en tant que consommateur.',
            ])]),
            ('6. Vos données', [('p', 'Les droits sur les dessins, voix et mots que vous ajoutez vous appartiennent (au parent et à l’enfant). Le développeur ne reçoit ni n’utilise ces données. Si la transcription de la voix est activée, les enregistrements servent uniquement à produire le texte et ne sont pas conservés.')]),
            ('7. La sauvegarde vous revient', [('p', 'Les données sont uniquement sur votre téléphone et la sauvegarde automatique d’Android est désactivée : en cas de perte ou de panne du téléphone, ou si vous supprimez l’application, elles ne peuvent pas être récupérées. Créez un fichier de sauvegarde dans Mes enfants › Sauvegarde et export et gardez-le en lieu sûr.')]),
            ('8. Limites des résultats', [('ul', [
                'La transcription de la voix peut comporter des erreurs. Vous pouvez modifier le texte à tout moment.',
                'À l’impression du PDF du livre, les couleurs et le format peuvent varier selon l’imprimante ou l’imprimeur.',
            ])]),
            ('9. Partage', [('p', 'Les cartes, livres et sauvegardes envoyés par un parent appartiennent au destinataire une fois envoyés et ne peuvent pas être rappelés depuis l’application. Le parent choisit à qui les envoyer.')]),
            ('10. Ce qui est interdit', [('ul', [
                'Utiliser l’application à des fins illégales ou pour porter atteinte aux droits d’autrui.',
                'Modifier l’application ou contourner le paiement.',
            ])]),
            ('11. Limitation de responsabilité', [('p', 'L’application est fournie en l’état. Dans les limites permises par la loi, le développeur n’est pas responsable des dommages tels que la perte de données liée à l’utilisation de l’application, sauf faute intentionnelle ou lourde.')]),
            ('12. Modifications et arrêt', [('p', 'Les fonctions peuvent changer ou s’arrêter. Les changements importants seront annoncés par les mises à jour de l’application et sur cette page. Même si le service s’arrête, les données sur votre téléphone et les PDF déjà téléchargés restent utilisables.')]),
            ('13. Droit applicable', [('p', 'Ces conditions sont régies par le droit de la République de Corée. Les consommateurs résidant dans d’autres pays conservent la protection des dispositions impératives de leur pays.')]),
            ('14. Contact', [('p', f'Questions sur ces conditions : {MAIL}')]),
        ],
    ),
    delete=dict(
        title='Suppression des données',
        sections=[
            ('À propos de cette page', [('p', 'Cette page explique comment supprimer les données de l’application Android « Dear Crayon ». Dear Crayon n’a ni compte ni stockage sur serveur : le prénom, les dessins, la voix et les mots de votre enfant ne se trouvent que sur votre téléphone. Vous pouvez les supprimer vous-même, immédiatement, et le développeur n’a aucune donnée à supprimer à votre place.')]),
            ('Méthode 1. Supprimer des éléments un par un', [('ol', [
                '<strong>Œuvre :</strong> ouvrez l’œuvre, touchez ⋯ en haut à droite › <strong>Supprimer l’œuvre</strong> › Supprimer. La photo, la voix et l’histoire sont supprimées ensemble.',
                '<strong>Réponse :</strong> sur l’écran de l’histoire, ouvrez le menu de la réponse (⋯) › <strong>Supprimer la réponse</strong>.',
                '<strong>Citation :</strong> touchez la citation › <strong>Supprimer</strong>.',
            ])]),
            ('Méthode 2. Supprimer toutes les données d’un enfant', [('ol', [
                'Ouvrez l’onglet <strong>Mes enfants</strong> en bas.',
                'Touchez <strong>Modifier les infos</strong>.',
                'Tout en bas, touchez <strong>Supprimer l’enfant</strong> et confirmez.',
            ]), ('p', 'Toutes les photos d’œuvres, enregistrements, réponses, citations et la photo de profil de cet enfant sont supprimés définitivement. Pour en garder une copie, créez d’abord un fichier dans Mes enfants › Sauvegarde et export.')]),
            ('Méthode 3. Tout supprimer dans l’application', [('ol', [
                'Ouvrez <strong>Paramètres</strong> › <strong>Applications</strong> › <strong>Dear Crayon</strong> sur votre téléphone.',
                'Touchez <strong>Désinstaller</strong>, ou pour garder l’application, <strong>Stockage</strong> › <strong>Effacer les données</strong>.',
            ]), ('p', 'Toutes les données et tous les réglages du téléphone sont supprimés immédiatement. La sauvegarde automatique étant désactivée, rien ne reste non plus dans Google Drive.')]),
            ('Désactiver la transcription de la voix', [('p', 'Mes enfants › ⚙ <strong>Réglages</strong> en haut à droite › <strong>Confidentialité</strong> › désactivez <strong>Transformer la voix en texte</strong>. Les enregistrements ne quittent alors plus le téléphone. Le serveur relais ne conserve de toute façon ni enregistrement ni texte : il n’y a rien à y supprimer.')]),
            ('Fichiers hors du téléphone', [('ul', [
                '<strong>Sauvegardes et fichiers partagés :</strong> supprimez vous-même les sauvegardes que vous avez créées et les fichiers de carte ou de livre envoyés à la famille, là où vous les avez enregistrés (Fichiers, cloud, messagerie, etc.). Les fichiers sur le téléphone d’un destinataire doivent être supprimés par celui-ci.',
                '<strong>Historique d’achat :</strong> les achats du PDF du livre restent dans l’historique d’achats Google Play de votre compte Google, visible dans Compte Google › Paiements et abonnements.',
            ])]),
            ('Ce qui est supprimé et durée de conservation', [('dl', [
                ('Infos de l’enfant, photos d’œuvres, voix, réponses, citations, notes des parents, réglages', 'Conservés dans le stockage de l’application sur le téléphone de l’utilisateur. Supprimés immédiatement avec les méthodes ci-dessus.'),
                ('Demandes de transcription', 'Non conservées sur le serveur relais. Rien ne reste une fois le texte renvoyé.'),
                ('Données conservées sur un serveur du développeur', 'Aucune. Ni compte, ni base de données du développeur, ni outil de publicité ou de mesure d’audience.'),
            ])]),
            ('Besoin d’aide ?', [('p', f'Si ces étapes ne suffisent pas, écrivez à {MAIL} avec l’objet « Suppression des données ». Nous répondons sous 7 jours. Le développeur ne détenant aucune donnée, nous vous guiderons dans les étapes de suppression.')]),
        ],
    ),
)

# ───────────────────────────── Español
L['es'] = dict(
    langName='Español', name='Dear Crayon',
    nav=dict(home='Inicio', privacy='Privacidad', terms='Condiciones de uso', delete='Borrar datos'),
    langLabel='Idioma', effective='Vigente desde el 19 de octubre de 2026', contact='Contacto',
    footer='Dear Crayon · Responsable: desarrollador de Dear Crayon',
    index=dict(
        title='Dear Crayon · Pequeños dibujos y palabras',
        desc='Una app de Android para guardar los dibujos y la voz de tu peque y convertir cada año en un libro. Todo se queda en tu móvil.',
        meta='App de Android · para madres y padres',
        tagline='Pequeños dibujos y palabras.',
        lead=[
            'Con Dear Crayon, madres y padres fotografían los dibujos de sus hijos y graban, con la propia voz del niño, lo que cuenta de cada uno. Las respuestas a las mismas preguntas de cada mes se pueden comparar año tras año, y en cada cumpleaños los recuerdos del año se reúnen en un libro.',
            'Esta es la página informativa oficial de la app Dear Crayon: política de privacidad, condiciones de uso y cómo borrar tus datos.',
        ],
        sections=[
            ('Qué puedes hacer', [('ul', [
                '<strong>Añadir obras:</strong> fotografía un dibujo, la app encuentra los bordes del papel y lo endereza, y guarda su historia con la voz del niño o con tus palabras.',
                '<strong>Historias del mes:</strong> preguntas para cada mes y la frase del mes; en cada cumpleaños, cuatro dibujos y seis preguntas.',
                '<strong>Crecimiento:</strong> las respuestas del mes pasado, del año pasado y del último cumpleaños a la misma pregunta, una al lado de otra.',
                '<strong>Tarjeta del mes y libro:</strong> un mes en una tarjeta y un año en un libro para compartir en familia.',
            ])]),
            ('Todo se queda en tu móvil', [('p', 'No hay registro ni inicio de sesión, y el desarrollador nunca recibe tus registros. El nombre, los dibujos, la voz y las palabras de tu peque se guardan solo en este móvil. Lo único que sale del móvil es la conversión de voz a texto, si un adulto la permite, y el servidor intermediario no guarda grabaciones ni textos. Sin publicidad, análisis de uso ni ubicación. Más detalles en la <a href="privacy.html">política de privacidad</a>.')]),
            ('Precios', [('p', 'Instalar la app, grabar, las tarjetas del mes y ver y compartir el libro (marcado como «Vista previa») son gratis. Descargar el PDF del libro en alta resolución, listo para imprimir, es de pago y se gestiona con la facturación de Google Play. El desarrollador nunca recibe los datos de tu tarjeta.')]),
        ],
        operator=[('Responsable', 'Desarrollador de Dear Crayon · República de Corea · desarrollador individual'), ('Servicio', 'Dear Crayon · Android'), ('Contacto', MAIL)],
        operatorTitle='Responsable y contacto',
        linksTitle='Documentos',
        links=dict(privacy='Qué se recoge, adónde va y cómo borrarlo', terms='Condiciones de uso, pagos y reembolsos', delete='Guía paso a paso para borrar tus datos'),
    ),
    privacy=dict(
        title='Política de privacidad',
        intro='Dear Crayon es una app para que madres y padres guarden los dibujos y la voz de sus hijos. No está pensada para que los niños la usen solos; un adulto (representante legal) introduce y gestiona la información del niño.',
        mdEffective='Vigente desde: 19 de octubre de 2026',
        summaryTitle='En resumen',
        summary=[
            'Todos los registros se guardan solo en este móvil. Sin cuenta, sin base de datos del desarrollador, sin publicidad, análisis ni ubicación.',
            'Lo único que sale del móvil es la conversión de voz a texto, si un adulto la permite. El servidor intermediario no guarda grabaciones ni textos.',
            'El PDF de pago del libro se compra con la facturación de Google Play. El desarrollador nunca recibe los datos de tu tarjeta.',
        ],
        sections=[
            ('1. Qué tratamos y dónde se guarda', [('ul', [
                'Nombre, fecha de nacimiento, nombre de artista y foto de perfil del niño; fotos de las obras; grabaciones de su voz; lo que dijo y respondió; frases; notas de los padres; ajustes de la app.',
                '<strong>Todo se guarda solo en el almacenamiento de la app en este móvil.</strong> Dear Crayon no tiene registro, ni inicio de sesión, ni base de datos propia, y el desarrollador nunca recibe estos registros.',
                'No usamos publicidad, análisis de uso ni ubicación.',
                'La copia de seguridad automática de Android (Google Drive) está desactivada. Las copias de seguridad de la app son archivos (zip) que crea un adulto.',
            ])]),
            ('2. Cuándo sale algo del móvil', [('ul', [
                '<strong>Voz a texto (opcional):</strong> solo si un adulto lo permite en la primera grabación, la grabación que se va a transcribir y el ajuste de idioma se envían al servidor intermediario de Dear Crayon (Cloudflare Workers). El servidor intermediario obtiene el texto de Cloudflare Workers AI (reconocimiento de voz Whisper, Cloudflare, Inc., Estados Unidos), lo devuelve y no guarda ni la grabación ni el texto. No se envía ningún otro dato, como el nombre del niño. Puedes desactivarlo cuando quieras en Ajustes › Privacidad; entonces no se envía nada.',
                '<strong>Compra del PDF del libro:</strong> el PDF del libro en alta resolución, listo para imprimir, se compra con la facturación de Google Play. Google gestiona el método de pago y los datos de facturación; el desarrollador nunca recibe los datos de tu tarjeta. La app solo recibe la confirmación de la compra y la registra en este móvil. El desarrollador usa los datos de la transacción de Google Play Console, como el número de pedido, solo para gestionar reembolsos y consultas.',
                '<strong>Archivos que comparten los padres:</strong> las tarjetas del mes, los PDF de los libros, los archivos de libro y las copias de seguridad solo salen del móvil cuando un adulto los envía con la app que elija (mensajería, correo, etc.). Quien los recibe tendrá ese archivo.',
            ])]),
            ('3. Permisos del móvil', [('ul', [
                'Cámara: para fotografiar las obras.',
                'Micrófono: para grabar la voz del niño.',
                'Notificaciones: recordatorios de las historias del mes y de los cumpleaños. Si los rechazas, todo lo demás sigue funcionando.',
            ])]),
            ('4. Conservación y borrado', [('ul', [
                'Los registros permanecen en este móvil hasta que un adulto los borra.',
                'Las obras, respuestas y frases se pueden borrar una a una en la app; al borrar a un niño se borran todos sus registros y archivos.',
                'Al borrar la app se borran todos los registros de este móvil. Borra tú las copias de seguridad y los archivos compartidos allí donde los guardaste.',
                'Como no se guarda nada en ningún servidor, no hay datos cuyo borrado tengas que solicitar aparte.',
            ])]),
            ('5. Privacidad de los niños', [('ul', [
                'De acuerdo con el RGPD (menores), la COPPA (EE. UU.) y la ley coreana de protección de datos personales, pedimos el consentimiento de un adulto antes de enviar la voz del niño a un servidor.',
                'Los padres pueden ver, corregir o borrar la información del niño y retirar su consentimiento en cualquier momento, directamente en la app.',
            ])]),
            ('6. Contacto', [('ul', [
                'Responsable: desarrollador de Dear Crayon (desarrollador individual)',
                f'Correo: {MAIL}',
                f'Web: <a href="{BASE}es/privacy.html">{BASE}es/privacy.html</a>',
            ])]),
        ],
        closing='Si esta política cambia, actualizaremos la fecha de vigencia en la app y en esta página.',
    ),
    terms=dict(
        title='Condiciones de uso',
        sections=[
            ('1. Ámbito', [('p', 'Estas condiciones recogen lo necesario para usar Dear Crayon (la «app»). Al instalar y usar la app, las aceptas. A la descarga y a los pagos se aplican también las Condiciones de Servicio de Google Play.')]),
            ('2. El servicio', [('p', 'La app es una herramienta para que madres y padres guarden las fotos de los dibujos, la voz y las palabras de sus hijos, y para crear, ver y compartir tarjetas del mes y libros (un año de recuerdos). Los registros se guardan solo en el móvil de quien usa la app.')]),
            ('3. Quién puede usarla', [('ul', [
                'La app es para madres, padres y tutores (adultos). No está pensada para que los niños la usen solos.',
                'Los padres registran información de los niños a su cargo. Pide permiso a cualquier otra persona (o a su tutor) antes de añadir su foto o su voz.',
            ])]),
            ('4. Precios y pago', [('ul', [
                'Instalar la app, grabar, las tarjetas del mes y ver y compartir el libro (marcado como «Vista previa») son gratis.',
                'Descargar el PDF del libro en alta resolución, listo para imprimir, es de pago. El precio se muestra en la pantalla de pago de Google Play antes de pagar.',
                'Los pagos se procesan con la facturación de Google Play. Google gestiona los métodos de pago y la facturación; el desarrollador nunca recibe los datos de tu tarjeta.',
            ])]),
            ('5. Reembolsos', [('ul', [
                'Los reembolsos siguen la <a href="https://support.google.com/googleplay/answer/2479637?hl=es" rel="noopener">política de reembolsos de Google Play</a>. En las 48 horas siguientes a la compra puedes pedir el reembolso directamente en Google Play; después, escríbenos al correo de abajo.',
                'Estas condiciones no limitan los derechos que te reconoce la ley como consumidor.',
            ])]),
            ('6. Tus registros', [('p', 'Los derechos sobre los dibujos, la voz y las palabras que añades son tuyos (de los padres y del niño). El desarrollador no recibe ni usa estos registros. Si la voz a texto está activada, las grabaciones solo se usan para obtener el texto y no se guardan.')]),
            ('7. La copia de seguridad es cosa tuya', [('p', 'Los registros están solo en tu móvil y la copia de seguridad automática de Android está desactivada; si pierdes o se estropea el móvil, o borras la app, no se podrán recuperar. Crea un archivo de copia en Mis peques › Copia y exportación y guárdalo en un lugar seguro.')]),
            ('8. Límites de los resultados', [('ul', [
                'La voz a texto puede equivocarse. Puedes editar el texto cuando quieras.',
                'Al imprimir el PDF del libro, los colores y el tamaño pueden variar según la impresora o la imprenta.',
            ])]),
            ('9. Compartir', [('p', 'Las tarjetas, libros y copias de seguridad que envía un adulto pasan a ser de quien los recibe y no se pueden recuperar desde la app. Los padres deciden a quién enviarlos.')]),
            ('10. Lo que no se permite', [('ul', [
                'Usar la app para fines ilegales o para vulnerar los derechos de otras personas.',
                'Modificar la app o eludir el pago.',
            ])]),
            ('11. Limitación de responsabilidad', [('p', 'La app se ofrece tal cual. En la medida en que lo permita la ley, el desarrollador no responde de daños como la pérdida de registros derivada del uso de la app, salvo dolo o culpa grave.')]),
            ('12. Cambios e interrupción', [('p', 'Las funciones pueden cambiar o dejar de estar disponibles. Los cambios importantes se anunciarán en las actualizaciones de la app y en esta página. Aunque el servicio se interrumpa, los registros de tu móvil y los PDF ya descargados seguirán siendo utilizables.')]),
            ('13. Ley aplicable', [('p', 'Estas condiciones se rigen por las leyes de la República de Corea. Los consumidores que residen en otros países conservan la protección de las normas imperativas de su país.')]),
            ('14. Contacto', [('p', f'Consultas sobre estas condiciones: {MAIL}')]),
        ],
    ),
    delete=dict(
        title='Borrar datos',
        sections=[
            ('Sobre esta página', [('p', 'Esta página explica cómo borrar los datos de la app de Android «Dear Crayon». Dear Crayon no tiene cuenta ni almacenamiento en servidores: el nombre, los dibujos, la voz y las palabras de tu peque solo están en tu móvil. Puedes borrarlos tú mismo al momento, y el desarrollador no tiene ningún dato que borrar por ti.')]),
            ('Opción 1. Borrar registros uno a uno', [('ol', [
                '<strong>Obra:</strong> abre la obra, toca ⋯ arriba a la derecha › <strong>Eliminar obra</strong> › Eliminar. Se borran juntas la foto, la voz y la historia.',
                '<strong>Respuesta:</strong> en la pantalla de la historia, abre el menú de la respuesta (⋯) › <strong>Eliminar respuesta</strong>.',
                '<strong>Frase:</strong> toca la frase › <strong>Eliminar</strong>.',
            ])]),
            ('Opción 2. Borrar todos los registros de un niño', [('ol', [
                'Abre la pestaña <strong>Mis peques</strong> abajo.',
                'Toca <strong>Editar datos del peque</strong>.',
                'Abajo del todo, toca <strong>Eliminar peque</strong> y confirma.',
            ]), ('p', 'Se borran para siempre todas las fotos de obras, grabaciones, respuestas, frases y la foto de perfil de ese niño. Si quieres conservar una copia, crea antes un archivo en Mis peques › Copia y exportación.')]),
            ('Opción 3. Borrar todo en la app', [('ol', [
                'Abre <strong>Ajustes</strong> › <strong>Aplicaciones</strong> › <strong>Dear Crayon</strong> en tu móvil.',
                'Toca <strong>Desinstalar</strong>, o para conservar la app, <strong>Almacenamiento</strong> › <strong>Borrar datos</strong>.',
            ]), ('p', 'Se borran al instante todos los registros y ajustes del móvil. Como la copia de seguridad automática está desactivada, tampoco queda nada en Google Drive.')]),
            ('Desactivar la voz a texto', [('p', 'Mis peques › ⚙ <strong>Ajustes</strong> arriba a la derecha › <strong>Privacidad</strong> › desactiva <strong>Convertir la voz en texto</strong>. Así las grabaciones dejan de salir del móvil. El servidor intermediario nunca guarda grabaciones ni textos, así que allí no hay nada que borrar.')]),
            ('Archivos fuera del móvil', [('ul', [
                '<strong>Copias y archivos compartidos:</strong> borra tú las copias de seguridad que creaste y los archivos de tarjetas o libros que enviaste a la familia allí donde los guardaste (Archivos, nube, mensajería, etc.). Los archivos del móvil de quien los recibió debe borrarlos esa persona.',
                '<strong>Historial de compras:</strong> las compras del PDF del libro quedan en el historial de compras de Google Play de tu cuenta de Google, en Cuenta de Google › Pagos y suscripciones.',
            ])]),
            ('Qué se borra y cuánto tiempo se guarda', [('dl', [
                ('Datos del niño, fotos de obras, voz, respuestas, frases, notas de los padres, ajustes', 'Guardados en el almacenamiento de la app en el móvil de quien la usa. Se borran al momento con las opciones de arriba.'),
                ('Solicitudes de voz a texto', 'No se guardan en el servidor intermediario. No queda nada una vez devuelto el texto.'),
                ('Registros guardados en un servidor del desarrollador', 'Ninguno. No hay cuenta, ni base de datos del desarrollador, ni herramientas de publicidad o análisis.'),
            ])]),
            ('¿Necesitas ayuda?', [('p', f'Si estos pasos no lo resuelven, escribe a {MAIL} con el asunto «Borrar datos». Respondemos en un plazo de 7 días. Como el desarrollador no guarda ningún registro, te guiaremos por los pasos para borrarlos.')]),
        ],
    ),
)

# ───────────────────────────── index = 가족이 공유 링크로 들어오는 "앱 받기" 페이지(2026-10-19 추가 요청)
PLAY = 'https://play.google.com/store/apps/details?id=com.dearcrayon.app'
_F = '<strong>…dearcrayon.zip</strong>'
INDEX = {
    'ko': dict(
        title='디어 크레용 · 아이의 그림과 말을 모으는 곳',
        ogTitle='디어 크레용 · 가족이 보낸 아이의 이야기',
        desc='아이의 그림과 말을 모으는 곳, 디어 크레용. 앱을 받으면 가족이 보낸 이달의 카드와 도록을 바로 볼 수 있어요.',
        hero='아이의 그림과 말을 모으는 곳, 디어 크레용',
        play='Google Play 에서 받기', playNote='안드로이드 무료 · 아이폰은 준비 중이에요',
        receiveTitle='가족에게 도록을 받았다면',
        receive=[
            '위 버튼으로 <strong>디어 크레용</strong> 앱을 설치해요.',
            f'카카오톡에서 받은 {_F} 파일을 눌러 <strong>‘디어 크레용’</strong>으로 열어요.',
            '바로 그 책이 열려요. 앱 첫 화면의 <strong>가족이 보낸 도록 보기</strong>에서도 다시 볼 수 있어요.',
        ],
        aboutTitle='디어 크레용은',
        about='부모가 아이의 그림을 사진으로 담고, 그 그림에 대해 아이가 한 말을 목소리로 남기는 앱이에요. 매달 같은 질문에 답하며 쌓인 기록은 이달의 카드가 되고, 생일마다 한 권의 도록으로 엮여요. 모든 기록은 휴대폰 안에만 저장되고, 회원 가입도 광고도 없어요.',
        docsTitle='안내',
    ),
    'en': dict(
        title='Dear Crayon · Little drawings, little words',
        ogTitle='Dear Crayon · A story from your family',
        desc='Little drawings, little words. Get the Dear Crayon app to open the monthly cards and books your family sends you.',
        hero='Little drawings, little words. Dear Crayon.',
        play='Get it on Google Play', playNote='Free on Android · iPhone coming soon',
        receiveTitle='Got a book from family?',
        receive=[
            'Install the <strong>Dear Crayon</strong> app with the button above.',
            f'Tap the file ending in {_F} you received (in a messaging app or email) and open it with <strong>Dear Crayon</strong>.',
            'The book opens right away. You can also find it later under <strong>View a book from family</strong> on the app’s first screen.',
        ],
        aboutTitle='About Dear Crayon',
        about='Dear Crayon lets parents photograph their child’s drawings and keep, in the child’s own voice, what each drawing is about. Answers to the same monthly questions become a monthly card, and each birthday they are gathered into a book. Everything stays on the phone — no sign-up, no ads.',
        docsTitle='Documents',
    ),
    'de': dict(
        title='Dear Crayon · Kleine Bilder, kleine Worte',
        ogTitle='Dear Crayon · Eine Geschichte von deiner Familie',
        desc='Kleine Bilder, kleine Worte. Mit der App Dear Crayon öffnest du die Monatskarten und Bücher, die deine Familie dir schickt.',
        hero='Kleine Bilder, kleine Worte. Dear Crayon.',
        play='Bei Google Play laden', playNote='Kostenlos für Android · iPhone folgt bald',
        receiveTitle='Ein Buch von der Familie bekommen?',
        receive=[
            'Installiere mit dem Button oben die App <strong>Dear Crayon</strong>.',
            f'Tippe auf die erhaltene Datei, die auf {_F} endet (im Messenger oder in der E-Mail), und öffne sie mit <strong>Dear Crayon</strong>.',
            'Das Buch öffnet sich sofort. Später findest du es auch unter <strong>Buch von der Familie ansehen</strong> auf dem ersten Bildschirm der App.',
        ],
        aboutTitle='Über Dear Crayon',
        about='Mit Dear Crayon fotografieren Eltern die Bilder ihres Kindes und halten mit der Stimme des Kindes fest, was es dazu erzählt. Antworten auf dieselben Monatsfragen werden zur Monatskarte und zu jedem Geburtstag zu einem Buch. Alles bleibt auf dem Handy – ohne Registrierung, ohne Werbung.',
        docsTitle='Dokumente',
    ),
    'fr': dict(
        title='Dear Crayon · Petits dessins, petits mots',
        ogTitle='Dear Crayon · Une histoire de votre famille',
        desc='Petits dessins, petits mots. Installez Dear Crayon pour ouvrir les cartes du mois et les livres que votre famille vous envoie.',
        hero='Petits dessins, petits mots. Dear Crayon.',
        play='Disponible sur Google Play', playNote='Gratuit sur Android · iPhone bientôt disponible',
        receiveTitle='Vous avez reçu un livre de la famille ?',
        receive=[
            'Installez l’application <strong>Dear Crayon</strong> avec le bouton ci-dessus.',
            f'Touchez le fichier reçu se terminant par {_F} (dans une messagerie ou un e-mail) et ouvrez-le avec <strong>Dear Crayon</strong>.',
            'Le livre s’ouvre aussitôt. Vous le retrouverez aussi dans <strong>Voir un livre de la famille</strong> sur le premier écran de l’application.',
        ],
        aboutTitle='Dear Crayon, c’est',
        about='Une application pour photographier les dessins de votre enfant et garder, avec sa propre voix, ce qu’il raconte sur chacun. Les réponses aux mêmes questions du mois deviennent une carte du mois et, à chaque anniversaire, un livre. Tout reste sur le téléphone — sans inscription ni publicité.',
        docsTitle='Documents',
    ),
    'es': dict(
        title='Dear Crayon · Pequeños dibujos y palabras',
        ogTitle='Dear Crayon · Una historia de tu familia',
        desc='Pequeños dibujos y palabras. Descarga Dear Crayon para abrir las tarjetas del mes y los libros que te envía tu familia.',
        hero='Pequeños dibujos y palabras. Dear Crayon.',
        play='Disponible en Google Play', playNote='Gratis en Android · iPhone, próximamente',
        receiveTitle='¿Te ha llegado un libro de la familia?',
        receive=[
            'Instala la app <strong>Dear Crayon</strong> con el botón de arriba.',
            f'Toca el archivo recibido que termina en {_F} (en la app de mensajería o en el correo) y ábrelo con <strong>Dear Crayon</strong>.',
            'El libro se abre al momento. También lo encontrarás después en <strong>Ver un libro de la familia</strong>, en la primera pantalla de la app.',
        ],
        aboutTitle='Qué es Dear Crayon',
        about='Una app para fotografiar los dibujos de tu peque y guardar, con su propia voz, lo que cuenta de cada uno. Las respuestas a las mismas preguntas de cada mes se convierten en una tarjeta del mes y, en cada cumpleaños, en un libro. Todo se queda en el móvil, sin registro ni anuncios.',
        docsTitle='Documentos',
    ),
}
for _l, _v in INDEX.items():
    L[_l]['index'].update(_v)
