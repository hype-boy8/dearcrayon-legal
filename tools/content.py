# Dear Crayon 정적 안내 페이지 내용(6개 언어). build.py 가 읽는다.
# 블록: ('p', html) · ('ul', [html]) · ('ol', [html]) · ('dl', [(dt, dd)]) · ('box', 제목, [html])
EMAIL = 'zxcvzxcv4423@gmail.com'
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
BASE = 'https://hype-boy8.github.io/dearcrayon-legal/'

LANGS = ['ko', 'en', 'de', 'fr', 'es', 'ja']

L = {}

# ───────────────────────────── 한국어
L['ko'] = dict(
    langName='한국어', name='Dear Crayon',
    nav=dict(home='홈', privacy='개인정보 처리방침', terms='이용약관', delete='데이터 삭제'),
    langLabel='언어', effective='시행일 2026년 10월 19일', contact='문의',
    footer='Dear Crayon · 운영: Dear Crayon 개발자',
    index=dict(
        title='Dear Crayon · 아이의 그림과 말을 모으는 곳',
        desc='부모가 아이의 그림 사진과 목소리를 기록하고, 한 해의 기록을 도록으로 엮는 안드로이드 앱. 기록은 휴대폰에 저장되고, 원하면 내 구글 드라이브에도 자동 백업돼요.',
        meta='안드로이드 앱 · 부모용',
        tagline='아이의 그림과 말을 모으는 곳',
        lead=[
            'Dear Crayon은 부모가 아이의 그림을 사진으로 담고, 그 그림에 대해 아이가 한 말을 목소리로 남기는 앱이에요. 매달 같은 질문에 답하며 쌓인 기록은 해마다 비교해 볼 수 있고, 생일마다 한 권의 도록(아이의 한 해 기록 책)으로 엮여요.',
            '이 사이트는 Dear Crayon 앱의 공식 안내 페이지예요. 개인정보 처리방침, 이용약관, 데이터 삭제 방법을 확인할 수 있어요.',
        ],
        sections=[
            ('앱에서 할 수 있는 것', [('ul', [
                '<strong>작품 담기:</strong> 아이 그림을 찍으면 종이 모서리를 찾아 반듯하게 펴 주고, 그림 이야기를 아이 목소리나 부모의 글로 남겨요.',
                '<strong>매달 이야기:</strong> 매달 아이에게 물어볼 질문과 이달의 한마디, 생일마다 그림 4장과 질문 6개.',
                '<strong>성장:</strong> 같은 질문에 대한 지난달 · 작년 · 지난 생일의 답을 나란히 봐요.',
                '<strong>이달의 카드 · 도록:</strong> 그달 기록을 카드 한 장으로, 한 해 기록을 책 한 권으로 만들어 가족과 나눠요.',
            ])]),
            ('기록은 휴대폰과 내 드라이브에만', [('p', '회원 가입이 없고, 개발자는 기록을 받지 않아요. 아이 이름 · 그림 · 목소리 · 글은 이 휴대폰에 저장돼요. 부모가 구글 드라이브 자동 백업을 켜면 <strong>부모 본인의 구글 드라이브</strong> 안 앱 전용 공간에도 저장돼요. 개발자 서버를 거치지 않아서 개발자는 볼 수 없어요. 그 밖에 휴대폰 밖으로 나가는 것은 부모가 허락한 경우의 음성 → 글 변환뿐이고, 중계 서버는 녹음과 글을 저장하지 않아요. 광고 · 사용 분석 · 위치 정보를 쓰지 않아요. 자세한 내용은 <a href="privacy.html">개인정보 처리방침</a>에 있어요.')]),
            ('요금', [('p', '앱 설치와 기록, 이달의 카드, 도록 보기 · 공유(‘미리보기’ 표시)는 무료예요. 인쇄용 고화질 도록 PDF 내려받기는 유료이며 구글 플레이 결제로 처리돼요. 개발자는 카드 정보를 받지 않아요.')]),
        ],
        operator=[('운영자', 'Dear Crayon 개발자 · 대한민국 · 개인 개발자'), ('서비스 이름', 'Dear Crayon (Dear Crayon) · 안드로이드'), ('문의', MAIL)],
        operatorTitle='운영자와 문의',
        linksTitle='안내 문서',
        links=dict(privacy='모은 정보 · 쓰는 곳 · 지우는 법', terms='이용 조건 · 결제와 환불', delete='기록을 지우는 방법 · 단계별 안내'),
    ),
    privacy=dict(
        title='개인정보 처리방침',
        intro='Dear Crayon은 부모가 아이의 그림과 목소리를 기록하는 앱이에요. 아이가 혼자 쓰도록 만든 앱이 아니며, 아이의 정보는 부모(법정대리인)가 직접 입력하고 관리해요.',
        mdEffective='시행일: 2026년 10월 19일',
        summaryTitle='한눈에 보기',
        summary=[
            '기록은 이 휴대폰에 저장돼요. 개발자 서버에는 저장하지 않고, 개발자는 기록을 볼 수 없어요. 회원 계정 · 자체 데이터베이스 · 광고 · 분석 · 위치 정보가 없어요.',
            '구글 드라이브 자동 백업(선택)을 켜면 기록이 <strong>부모 본인의 구글 드라이브</strong> 안 앱 전용 공간에도 저장돼요. 처음엔 꺼져 있어요.',
            '그 밖에 휴대폰 밖으로 나가는 것은 부모가 허락한 음성 → 글 변환뿐이에요. 중계 서버는 녹음과 글을 저장하지 않아요.',
            '유료 도록 PDF는 구글 플레이 결제로 사요. 개발자는 카드 정보를 받지 않아요.',
        ],
        sections=[
            ('1. 다루는 정보와 저장하는 곳', [('ul', [
                '아이 이름 · 생년월일 · 작가 이름 · 프로필 사진, 작품 사진, 아이 목소리 녹음, 아이가 한 말과 답, 이달의 한마디, 부모 메모, 앱 설정.',
                '이 정보는 <strong>이 휴대폰 안의 앱 저장소</strong>에 저장돼요. 부모가 구글 드라이브 자동 백업을 켠 경우에만 같은 내용이 <strong>부모 본인의 구글 드라이브</strong> 안 앱 전용 공간에도 저장돼요(아래 2번). Dear Crayon은 회원 가입 · 자체 데이터베이스 · 자체 서버 저장소가 없고, 개발자는 이 기록을 받거나 볼 수 없어요. 구글 로그인은 드라이브 자동 백업을 켤 때만 써요.',
                '광고, 사용 분석, 위치 정보를 쓰지 않아요.',
                '안드로이드 시스템 자동 백업은 꺼져 있어요. 앱 안의 백업은 부모가 직접 만드는 파일(zip)과, 부모가 켜는 선택 기능인 구글 드라이브 자동 백업(처음엔 꺼져 있어요) 두 가지예요.',
            ])]),
            ('2. 휴대폰 밖으로 나가는 경우', [('ul', [
                '<strong>목소리를 글로 바꾸기(선택):</strong> 처음 녹음할 때 부모가 허락한 경우에만, 글로 바꿀 녹음 파일과 언어 설정을 Dear Crayon 중계 서버(Cloudflare Workers)로 보내요. 중계 서버는 Cloudflare Workers AI(Whisper 음성 인식, Cloudflare, Inc., 미국)로 글을 만들어 돌려주고, 녹음과 글을 저장하지 않아요. 아이 이름 같은 다른 기록은 보내지 않아요. 언제든 설정 › 개인정보에서 끌 수 있고, 끄면 아무것도 보내지 않아요.',
                '<strong>구글 드라이브 자동 백업(선택):</strong> 처음엔 꺼져 있어요. 부모가 구글로 로그인해 켜면(첫 화면 ‘Google로 시작하기’ 또는 우리 아이 › 백업 · 내보내기), 백업 파일과 같은 내용 — 아이 정보, 원본 화질 작품 사진, 목소리 녹음, 답과 아이가 한 말, 한마디, 부모 메모, 가족에게 받은 도록 — 을 <strong>부모 본인의 구글 드라이브</strong> 안 앱 전용 숨김 공간에 올려요(구글 권한 drive.appdata). 이 공간은 드라이브 화면에 보이지 않고 저장 용량만 써요. 앱은 드라이브의 다른 파일을 볼 수 없어요. 기록은 휴대폰과 구글 드라이브(Google LLC) 사이를 바로 오가고 개발자 서버를 거치거나 저장되지 않아서, 개발자는 볼 수 없어요. 기본은 와이파이에서만, 앱이 열려 있을 때만 올리고(스위치로 모바일 데이터 허용), 앱에서 지운 것은 다음에 올릴 때 드라이브 백업에서도 지워요. 어느 계정을 쓰는지 보여 주려고 로그인한 계정의 이메일 주소를 이 휴대폰에만 저장해요.',
                '<strong>도록 PDF 구매:</strong> 인쇄용 고화질 도록 PDF 내려받기는 구글 플레이 결제로 사요. 결제 수단과 청구 정보는 구글이 처리하고, 개발자는 카드 정보를 받지 않아요. 앱은 구매가 됐다는 확인만 받아 이 휴대폰에 기록해요. 개발자는 구글 플레이 콘솔의 주문 번호 같은 거래 정보를 환불 · 문의 처리에만 써요.',
                '<strong>부모가 직접 보내는 파일:</strong> 이달의 카드, 도록 PDF, 도록 파일, 백업 파일은 부모가 고른 앱(메신저 · 메일 등)으로 직접 보낼 때만 나가요. 받은 사람이 그 파일을 갖게 돼요.',
            ])]),
            ('3. 휴대폰 권한', [('ul', [
                '카메라: 작품 사진을 찍을 때.',
                '마이크: 아이 목소리를 녹음할 때.',
                '알림: 매달 이야기 · 생일 알림. 거절해도 나머지 기능은 그대로 쓸 수 있어요.',
            ])]),
            ('4. 보관 기간과 지우는 법', [('ul', [
                '기록은 부모가 지우기 전까지 이 휴대폰에 남아요. 구글 드라이브 자동 백업을 켰다면 드라이브 백업도 부모가 지우기 전까지 부모의 구글 계정에 남아요.',
                '작품 · 답 · 한마디는 앱 안에서 하나씩 지울 수 있고, 아이를 지우면 그 아이의 모든 기록과 파일이 지워져요.',
                '앱을 지우면 이 휴대폰 안의 모든 기록이 지워져요. 드라이브 백업은 앱을 지워도 남으니 아래 방법으로 지워 주세요. 백업 파일과 보낸 파일은 부모가 보관한 곳에서 직접 지워 주세요.',
                '<strong>드라이브 백업 지우기:</strong> ‘자동 백업 끄기’는 올리기만 멈추고 드라이브의 백업은 남겨 둬요. 앱의 <strong>드라이브의 백업 지우기</strong>로 드라이브 백업 전체를 지울 수 있어요. 앱 없이도 구글 드라이브 › 설정 › 앱 관리 › Dear Crayon › 숨겨진 앱 데이터 삭제로 지울 수 있고, 구글 계정 › 보안 › 서드 파티 앱에서 접근 권한을 거둘 수 있어요.',
                '개발자 서버에 남는 기록이 없어서 개발자에게 따로 삭제를 요청할 데이터는 없어요. 드라이브 백업은 부모 본인의 구글 계정에 있고, 부모가 직접 지울 수 있어요.',
            ])]),
            ('5. 아이 개인정보 보호', [('ul', [
                '미국 아동 온라인 개인정보 보호법(COPPA), 유럽 개인정보 보호법(GDPR)의 아동 규정, 한국 개인정보 보호법에 따라, 아이 목소리를 서버로 보내기 전에 부모의 동의를 받아요. 구글 드라이브 자동 백업도 부모가 직접 로그인해 켤 때만 동작해요.',
                '부모는 언제든 아이 정보를 보고 · 고치고 · 지우고, 동의를 거둘 수 있어요(모두 앱 안에서 바로).',
            ])]),
            ('6. 문의', [('ul', [
                '운영자: Dear Crayon 개발자(개인 개발자)',
                f'연락처: {MAIL}',
                f'웹: <a href="{BASE}privacy.html">{BASE}privacy.html</a>',
            ])]),
        ],
        closing='이 방침이 바뀌면 앱과 이 페이지의 시행일을 바꿔 알려 드려요.',
    ),
    terms=dict(
        title='이용약관',
        sections=[
            ('1. 약관의 적용', [('p', '이 약관은 Dear Crayon(이하 “앱”)을 쓰는 데 필요한 사항을 정해요. 앱을 설치해 쓰면 이 약관에 동의한 것으로 봐요. 앱 내려받기와 결제에는 구글 플레이 서비스 약관도 함께 적용돼요.')]),
            ('2. 서비스 내용', [('p', '앱은 부모가 아이의 그림 사진 · 목소리 · 말을 기록하고, 이달의 카드와 도록(아이의 한 해 기록 책)을 만들어 보고 나누는 도구예요. 기록은 이용자의 휴대폰에 저장되고, 이용자가 구글 드라이브 자동 백업(선택)을 켜면 이용자 본인의 구글 드라이브 안 앱 전용 공간에도 저장돼요. 개발자 서버에는 저장하지 않아요.')]),
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
            ('6. 이용자의 기록', [('p', '앱에 담은 그림 · 목소리 · 글의 권리는 이용자(부모와 아이)에게 있어요. 개발자는 이 기록을 받거나 쓰지 않아요. 음성 → 글 변환을 켠 경우에도 녹음은 글로 바꾸는 데만 쓰이고 저장되지 않아요. 구글 드라이브 자동 백업도 이용자 본인의 드라이브에 바로 저장되고, 개발자는 볼 수 없어요.')]),
            ('7. 백업은 이용자가', [('p', '안드로이드 시스템 자동 백업은 꺼져 있어요. 백업이 없으면 휴대폰을 잃어버리거나 고장 나거나 앱을 지웠을 때 기록을 되살릴 수 없어요. 우리 아이 › 백업 · 내보내기에서 구글 드라이브 자동 백업을 켜거나(선택 — 새 휴대폰에서 구글로 로그인하면 되살릴 수 있어요), 백업 파일을 만들어 안전한 곳에 보관해 주세요. 드라이브 자동 백업은 앱이 열려 있을 때(기본은 와이파이에서) 올라가서, 가장 최근 기록은 아직 올라가지 않았을 수 있어요.')]),
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
            ('이 페이지는', [('p', '안드로이드 앱 “Dear Crayon”의 데이터 삭제 안내예요. Dear Crayon은 회원 계정과 개발자 서버 저장이 없어요. 아이 이름 · 그림 · 목소리 · 글은 이용자의 휴대폰에 있고, 구글 드라이브 자동 백업을 켰다면 이용자 본인의 구글 드라이브(앱 전용 공간)에도 있어요. 그래서 이용자가 직접, 바로 지울 수 있고, 개발자가 대신 지워 드릴 데이터는 없어요.')]),
            ('방법 1. 기록을 하나씩 지우기', [('ol', [
                '<strong>작품:</strong> 작품을 열고 오른쪽 위 ⋯ › <strong>작품 삭제</strong> › 삭제. 사진 · 목소리 · 이야기가 함께 지워져요.',
                '<strong>답:</strong> 이야기 화면에서 답의 메뉴(⋯) › <strong>답 삭제</strong>.',
                '<strong>한마디:</strong> 한마디를 눌러 › <strong>삭제</strong>.',
            ])]),
            ('방법 2. 아이의 모든 기록 지우기', [('ol', [
                '아래 <strong>우리 아이</strong> 탭을 열어요.',
                '<strong>아이 정보 고치기</strong>를 눌러요.',
                '맨 아래 <strong>아이 삭제</strong>를 누르고 확인해요.',
            ]), ('p', '그 아이의 작품 사진 · 목소리 · 답 · 한마디 · 프로필 사진이 모두 지워지고 되돌릴 수 없어요. 남겨 두고 싶으면 먼저 우리 아이 › 백업 · 내보내기로 파일을 만들어 두세요.')]),
            ('방법 3. 앱의 모든 기록 지우기', [('ol', [
                '휴대폰 <strong>설정</strong> › <strong>애플리케이션</strong> › <strong>Dear Crayon</strong>을 열어요.',
                '<strong>삭제</strong>(앱 지우기)를 누르거나, 앱을 남기려면 <strong>저장공간</strong> › <strong>데이터 삭제</strong>를 눌러요.',
            ]), ('p', '휴대폰 안의 모든 기록과 설정이 바로 지워져요. 안드로이드 시스템 자동 백업은 꺼져 있어요. 다만 앱의 구글 드라이브 자동 백업을 켰다면 드라이브의 백업은 그대로 남아요. 아래 ‘구글 드라이브 백업 지우기’로 지워 주세요.')]),
            ('구글 드라이브 백업 지우기', [('ol', [
                '<strong>앱에서:</strong> 우리 아이 › <strong>백업 · 내보내기</strong> › <strong>드라이브의 백업 지우기</strong>를 누르고 확인해요. 드라이브 백업 전체가 지워져요.',
                '<strong>앱 없이:</strong> 구글 드라이브 › <strong>설정</strong> › <strong>앱 관리</strong> › <strong>Dear Crayon</strong> › <strong>숨겨진 앱 데이터 삭제</strong>.',
                '<strong>접근 권한 거두기:</strong> 구글 계정 › <strong>보안</strong> › <strong>서드 파티 앱</strong>에서 Dear Crayon의 접근을 삭제해요.',
            ]), ('p', '<strong>자동 백업 끄기</strong>는 올리기만 멈추고 드라이브의 백업은 남겨 둬요. 켜 둔 동안 앱에서 지운 기록은 다음에 올릴 때 드라이브 백업에서도 지워져요.')]),
            ('음성 변환 끄기', [('p', '우리 아이 › 오른쪽 위 ⚙ <strong>설정</strong> › <strong>개인정보</strong> › <strong>아이 목소리를 글로 바꾸기</strong>를 꺼요. 끄면 녹음을 휴대폰 밖으로 보내지 않아요. 중계 서버는 처음부터 녹음과 글을 저장하지 않아서 따로 지울 것이 없어요.')]),
            ('휴대폰 밖에 있는 파일', [('ul', [
                '<strong>백업 · 보낸 파일:</strong> 부모가 만든 백업 파일, 가족에게 보낸 카드 · 도록 파일은 저장한 곳(내 파일, 클라우드, 메신저 등)에서 직접 지워 주세요. 받은 사람의 휴대폰에 있는 파일은 받은 사람이 지워야 해요.',
                '<strong>구글 드라이브 백업:</strong> 자동 백업을 켰다면 이용자 본인의 구글 드라이브 안 앱 전용 공간에 있어요. 위 ‘구글 드라이브 백업 지우기’로 지워 주세요.',
                '<strong>구매 기록:</strong> 도록 PDF 구매 내역은 구글 계정의 구글 플레이 구매 기록에 남아요. 구글 계정 › 결제 및 구독에서 확인할 수 있어요.',
            ])]),
            ('지워지는 데이터와 보관 기간', [('dl', [
                ('아이 정보 · 작품 사진 · 목소리 · 답 · 한마디 · 부모 메모 · 설정', '저장 위치: 이용자의 휴대폰 안 앱 저장소. 삭제 시점: 위 방법으로 지우는 즉시.'),
                ('음성 → 글 변환 요청', '중계 서버에 저장하지 않아요. 변환이 끝나면 남는 것이 없어요.'),
                ('구글 드라이브 자동 백업(켠 경우)', '저장 위치: 이용자 본인의 구글 드라이브 안 앱 전용 숨김 공간(개발자는 볼 수 없어요). 삭제 시점: 앱의 ‘드라이브의 백업 지우기’나 구글 드라이브의 ‘숨겨진 앱 데이터 삭제’ 즉시. 앱에서 지운 것은 다음에 올릴 때 함께 지워져요.'),
                ('개발자 서버에 보관되는 기록', '없어요. 회원 계정 · 자체 데이터베이스 · 광고 · 분석 도구가 없어요.'),
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
        desc='An Android app for parents to keep their child’s drawings and voice, and turn each year into a book. Records stay on your phone — and, if you turn it on, in your own Google Drive.',
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
            ('Your records stay with you', [('p', 'There is no sign-up, and the developer never receives your records. Your child’s name, drawings, voice and words are stored on this phone. If a parent turns on Google Drive auto backup, they are also stored in an app-only space in <strong>the parent’s own Google Drive</strong>. Nothing passes through the developer’s servers, so the developer cannot see them. The only other thing that leaves the phone is voice-to-text, if a parent allows it, and the relay server does not store recordings or text. No advertising, usage analytics or location. Details are in the <a href="privacy.html">Privacy Policy</a>.')]),
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
            'Records are stored on this phone. Nothing is stored on the developer’s servers, and the developer cannot see your records. No Dear Crayon account, no developer database, no advertising, analytics or location.',
            'If you turn on Google Drive auto backup (optional), records are also stored in an app-only space in <strong>the parent’s own Google Drive</strong>. It is off by default.',
            'The only other thing that leaves the phone is voice-to-text, if a parent allows it. The relay server does not store recordings or text.',
            'The paid book PDF is bought through Google Play Billing. The developer never receives your card details.',
        ],
        sections=[
            ('1. What we handle and where it is stored', [('ul', [
                'Child’s name, date of birth, artist name and profile photo; photos of artworks; recordings of the child’s voice; what the child said and answered; quotes; parent notes; app settings.',
                'It is stored in <strong>the app’s storage on this phone</strong>. Only if a parent turns on Google Drive auto backup is the same content also stored in an app-only space in <strong>the parent’s own Google Drive</strong> (see section 2). Dear Crayon has no sign-up, no database and no server storage of its own, and the developer never receives or sees these records. Google sign-in is used only to turn on Drive auto backup.',
                'We do not use advertising, usage analytics or location.',
                'Android’s system Auto Backup is turned off. The app offers two kinds of backup: files (zip) that a parent creates, and the optional Google Drive auto backup that a parent turns on (off by default).',
            ])]),
            ('2. When something leaves the phone', [('ul', [
                '<strong>Voice-to-text (optional):</strong> only if a parent allows it at the first recording, the recording to be transcribed and the language setting are sent to the Dear Crayon relay server (Cloudflare Workers). The relay server has the text produced by Cloudflare Workers AI (Whisper speech recognition, Cloudflare, Inc., United States), returns it, and stores neither the recording nor the text. No other records, such as the child’s name, are sent. You can turn this off anytime in Settings › Privacy; when off, nothing is sent.',
                '<strong>Google Drive auto backup (optional):</strong> off by default. If a parent signs in with Google and turns it on (“Continue with Google” on the first screen, or My Kids › Backup &amp; export), the same contents as a backup file — child info, artwork photos in original quality, voice recordings, answers and the child’s words, quotes, parent notes and books received from family — are uploaded to a hidden, app-only folder in <strong>the parent’s own Google Drive</strong> (Google permission drive.appdata). This folder does not appear in the Drive interface; it only uses storage. The app cannot see any other files in your Drive. Data goes directly between the phone and Google Drive (Google LLC); it does not pass through or get stored on any developer server, so the developer cannot see it. By default it uploads only on Wi‑Fi and only while the app is open (a switch allows mobile data). Items deleted in the app are also deleted from the Drive backup at the next upload. The email address of the signed-in account is kept on this phone only, to show which account is used.',
                '<strong>Buying the book PDF:</strong> the high-resolution, print-ready book PDF is bought through Google Play Billing. Google handles the payment method and billing details; the developer never receives your card details. The app only receives confirmation that the purchase went through and records it on this phone. The developer uses transaction details in the Google Play Console, such as the order number, only to handle refunds and support requests.',
                '<strong>Files a parent shares:</strong> monthly cards, book PDFs, book files and backup files leave the phone only when a parent sends them through an app they choose (messaging, email, etc.). The recipient then has that file.',
            ])]),
            ('3. Phone permissions', [('ul', [
                'Camera: to photograph artworks.',
                'Microphone: to record the child’s voice.',
                'Notifications: monthly story and birthday reminders. Everything else still works if you decline.',
            ])]),
            ('4. Retention and deletion', [('ul', [
                'Records stay on this phone until a parent deletes them. If Google Drive auto backup is on, the Drive backup also stays in the parent’s Google account until the parent deletes it.',
                'Artworks, answers and quotes can be deleted one by one in the app; deleting a child deletes all of that child’s records and files.',
                'Deleting the app deletes every record on this phone. The Drive backup remains even if you delete the app, so delete it as described below. Please delete backup files and shared files yourself wherever you saved them.',
                '<strong>Deleting the Drive backup:</strong> “Turn off auto backup” only stops uploads and leaves the backup in Drive. <strong>Delete backup from Drive</strong> in the app deletes the whole Drive backup. Without the app, you can delete it in Google Drive › Settings › Manage apps › Dear Crayon › Delete hidden app data, and revoke access in Google Account › Security › Third-party apps.',
                'Because nothing is kept on a developer server, there is no data to ask the developer to delete. The Drive backup is in the parent’s own Google account, and the parent can delete it at any time.',
            ])]),
            ('5. Children’s privacy', [('ul', [
                'In line with COPPA (US), the GDPR rules for children (EU/UK) and the Korean Personal Information Protection Act, we ask for a parent’s consent before any of the child’s voice is sent to a server. Google Drive auto backup also works only after a parent signs in and turns it on.',
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
            ('2. The service', [('p', 'The app is a tool for parents to record their child’s drawing photos, voice and words, and to make, view and share monthly cards and books (a year of the child’s records). Records are stored on the user’s phone and, if the user turns on Google Drive auto backup (optional), also in an app-only space in the user’s own Google Drive. They are not stored on the developer’s servers.')]),
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
            ('6. Your records', [('p', 'The rights to the drawings, voice and words you add belong to you (the parent and child). The developer does not receive or use these records. If voice-to-text is on, recordings are used only to produce the text and are not stored. Google Drive auto backup is saved directly to your own Drive, and the developer cannot see it.')]),
            ('7. Backups are up to you', [('p', 'Android’s system Auto Backup is off. Without a backup, records cannot be recovered if your phone is lost or broken or you delete the app. In My Kids › Backup &amp; export, turn on Google Drive auto backup (optional — on a new phone, sign in with Google to restore) or create a backup file and keep it somewhere safe. Drive auto backup uploads while the app is open (on Wi‑Fi by default), so the most recent records may not have been uploaded yet.')]),
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
            ('About this page', [('p', 'This page explains how to delete data in the Android app “Dear Crayon”. Dear Crayon has no Dear Crayon account and no developer server storage. Your child’s name, drawings, voice and words are on your phone and, if you turned on Google Drive auto backup, also in an app-only space in your own Google Drive. You can delete them yourself, immediately, and there is no data the developer could delete on your behalf.')]),
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
            ]), ('p', 'All records and settings on the phone are deleted immediately. Android’s system Auto Backup is off. However, if you turned on the app’s Google Drive auto backup, the backup in Drive remains — delete it as described in “Delete the Google Drive backup” below.')]),
            ('Delete the Google Drive backup', [('ol', [
                '<strong>In the app:</strong> My Kids › <strong>Backup &amp; export</strong> › tap <strong>Delete backup from Drive</strong> and confirm. The whole Drive backup is deleted.',
                '<strong>Without the app:</strong> Google Drive › <strong>Settings</strong> › <strong>Manage apps</strong> › <strong>Dear Crayon</strong> › <strong>Delete hidden app data</strong>.',
                '<strong>Revoke access:</strong> Google Account › <strong>Security</strong> › <strong>Third-party apps</strong>, then remove Dear Crayon’s access.',
            ]), ('p', '<strong>Turn off auto backup</strong> only stops uploads and leaves the backup in Drive. While it is on, records you delete in the app are also deleted from the Drive backup at the next upload.')]),
            ('Turn off voice-to-text', [('p', 'Go to My Kids › ⚙ <strong>Settings</strong> at the top right › <strong>Privacy</strong> and turn off <strong>Turn voice into text</strong>. Recordings will no longer leave the phone. The relay server never stores recordings or text, so there is nothing there to delete.')]),
            ('Files outside the phone', [('ul', [
                '<strong>Backups and shared files:</strong> please delete backup files you created and card or book files you sent to family from wherever you saved them (Files, cloud storage, messaging apps, etc.). Files on a recipient’s phone must be deleted by the recipient.',
                '<strong>Google Drive backup:</strong> if you turned on auto backup, it is in an app-only space in your own Google Drive. Delete it as described in “Delete the Google Drive backup” above.',
                '<strong>Purchase history:</strong> book PDF purchases remain in your Google account’s Google Play purchase history, which you can see under Google Account › Payments &amp; subscriptions.',
            ])]),
            ('What is deleted and how long it is kept', [('dl', [
                ('Child info, artwork photos, voice, answers, quotes, parent notes, settings', 'Stored in the app’s storage on the user’s phone. Deleted immediately when you use the options above.'),
                ('Voice-to-text requests', 'Not stored on the relay server. Nothing remains once the text is returned.'),
                ('Google Drive auto backup (if turned on)', 'Stored in a hidden, app-only space in the user’s own Google Drive (the developer cannot see it). Deleted immediately with “Delete backup from Drive” in the app or “Delete hidden app data” in Google Drive. Items deleted in the app are removed at the next upload.'),
                ('Records kept on a developer server', 'None. There is no Dear Crayon account, no developer database, no advertising or analytics tools.'),
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
        desc='Eine Android-App für Eltern, um die Bilder und die Stimme ihres Kindes festzuhalten und jedes Jahr zu einem Buch zu machen. Die Einträge bleiben auf deinem Handy – und, wenn du es einschaltest, in deinem eigenen Google Drive.',
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
            ('Deine Einträge bleiben bei dir', [('p', 'Es gibt keine Registrierung, und der Entwickler erhält deine Einträge nie. Name, Bilder, Stimme und Worte deines Kindes werden auf diesem Handy gespeichert. Schaltet ein Elternteil die automatische Google-Drive-Sicherung ein, werden sie zusätzlich in einem App-eigenen Bereich im <strong>eigenen Google Drive der Eltern</strong> gespeichert. Nichts läuft über Server des Entwicklers, der Entwickler kann sie also nicht sehen. Sonst verlässt nur die Sprache-zu-Text-Umwandlung das Handy, wenn ein Elternteil sie erlaubt – und der Relay-Server speichert weder Aufnahmen noch Text. Keine Werbung, keine Nutzungsanalyse, kein Standort. Einzelheiten in der <a href="privacy.html">Datenschutzerklärung</a>.')]),
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
            'Die Einträge werden auf diesem Handy gespeichert. Auf Servern des Entwicklers wird nichts gespeichert, und der Entwickler kann deine Einträge nicht sehen. Kein Dear-Crayon-Konto, keine Datenbank des Entwicklers, keine Werbung, Analyse oder Standortdaten.',
            'Schaltest du die automatische Google-Drive-Sicherung ein (freiwillig), werden die Einträge zusätzlich in einem App-eigenen Bereich im <strong>eigenen Google Drive der Eltern</strong> gespeichert. Sie ist anfangs ausgeschaltet.',
            'Sonst verlässt nur die Sprache-zu-Text-Umwandlung das Handy, wenn ein Elternteil sie erlaubt. Der Relay-Server speichert weder Aufnahmen noch Text.',
            'Das kostenpflichtige Buch-PDF wird über Google Play Billing gekauft. Der Entwickler erhält keine Kartendaten.',
        ],
        sections=[
            ('1. Welche Daten wir verarbeiten und wo sie gespeichert werden', [('ul', [
                'Name, Geburtsdatum, Künstlername und Profilfoto des Kindes; Fotos der Kunstwerke; Aufnahmen der Stimme des Kindes; was das Kind gesagt und geantwortet hat; Zitate; Notizen der Eltern; App-Einstellungen.',
                'Alles wird im <strong>App-Speicher auf diesem Handy</strong> gespeichert. Nur wenn ein Elternteil die automatische Google-Drive-Sicherung einschaltet, werden dieselben Inhalte zusätzlich in einem App-eigenen Bereich im <strong>eigenen Google Drive der Eltern</strong> gespeichert (siehe Abschnitt 2). Dear Crayon hat keine Registrierung, keine eigene Datenbank und keinen eigenen Serverspeicher, und der Entwickler erhält oder sieht diese Einträge nie. Die Google-Anmeldung dient nur dazu, die Drive-Sicherung einzuschalten.',
                'Wir verwenden keine Werbung, keine Nutzungsanalyse und keinen Standort.',
                'Die automatische Systemsicherung von Android ist ausgeschaltet. Die App bietet zwei Arten der Sicherung: Dateien (zip), die ein Elternteil selbst erstellt, und die freiwillige automatische Google-Drive-Sicherung, die ein Elternteil einschaltet (anfangs aus).',
            ])]),
            ('2. Wann etwas das Handy verlässt', [('ul', [
                '<strong>Sprache-zu-Text (freiwillig):</strong> Nur wenn ein Elternteil es bei der ersten Aufnahme erlaubt, werden die zu verschriftende Aufnahme und die Spracheinstellung an den Dear-Crayon-Relay-Server (Cloudflare Workers) gesendet. Der Relay-Server lässt den Text von Cloudflare Workers AI (Whisper-Spracherkennung, Cloudflare, Inc., USA) erstellen, gibt ihn zurück und speichert weder Aufnahme noch Text. Andere Einträge, etwa der Name des Kindes, werden nicht gesendet. Du kannst das jederzeit unter Einstellungen › Datenschutz ausschalten; dann wird nichts gesendet.',
                '<strong>Automatische Google-Drive-Sicherung (freiwillig):</strong> anfangs ausgeschaltet. Meldet sich ein Elternteil mit Google an und schaltet sie ein („Mit Google fortfahren“ auf dem ersten Bildschirm oder Meine Kinder › Sichern &amp; exportieren), werden dieselben Inhalte wie in einer Sicherungsdatei – Angaben zum Kind, Kunstwerkfotos in Originalqualität, Sprachaufnahmen, Antworten und Worte des Kindes, Zitate, Notizen der Eltern und von der Familie erhaltene Bücher – in einen versteckten, App-eigenen Ordner im <strong>eigenen Google Drive der Eltern</strong> hochgeladen (Google-Berechtigung drive.appdata). Dieser Ordner ist in der Drive-Oberfläche nicht sichtbar und belegt nur Speicherplatz. Die App kann keine anderen Dateien in deinem Drive sehen. Die Daten gehen direkt zwischen Handy und Google Drive (Google LLC); sie laufen nicht über Server des Entwicklers und werden dort nicht gespeichert, der Entwickler kann sie also nicht sehen. Standardmäßig wird nur im WLAN und nur bei geöffneter App hochgeladen (ein Schalter erlaubt mobile Daten). In der App gelöschte Einträge werden beim nächsten Hochladen auch aus der Drive-Sicherung gelöscht. Die E-Mail-Adresse des angemeldeten Kontos wird nur auf diesem Handy gespeichert, um anzuzeigen, welches Konto verwendet wird.',
                '<strong>Kauf des Buch-PDFs:</strong> Das hochauflösende, druckfertige Buch-PDF wird über Google Play Billing gekauft. Zahlungsmittel und Abrechnungsdaten verarbeitet Google; der Entwickler erhält keine Kartendaten. Die App erhält nur die Bestätigung, dass der Kauf erfolgt ist, und speichert sie auf diesem Handy. Transaktionsdaten in der Google Play Console, etwa die Bestellnummer, nutzt der Entwickler nur für Erstattungen und Anfragen.',
                '<strong>Dateien, die Eltern teilen:</strong> Monatskarten, Buch-PDFs, Buchdateien und Sicherungsdateien verlassen das Handy nur, wenn ein Elternteil sie über eine selbst gewählte App (Messenger, E-Mail usw.) sendet. Die Empfänger haben dann diese Datei.',
            ])]),
            ('3. Berechtigungen', [('ul', [
                'Kamera: zum Fotografieren der Kunstwerke.',
                'Mikrofon: zum Aufnehmen der Stimme des Kindes.',
                'Benachrichtigungen: Erinnerungen an Monatsgeschichten und Geburtstage. Lehnst du ab, funktioniert alles andere weiter.',
            ])]),
            ('4. Speicherdauer und Löschen', [('ul', [
                'Einträge bleiben auf diesem Handy, bis ein Elternteil sie löscht. Ist die automatische Google-Drive-Sicherung eingeschaltet, bleibt auch die Drive-Sicherung im Google-Konto der Eltern, bis sie gelöscht wird.',
                'Kunstwerke, Antworten und Zitate lassen sich in der App einzeln löschen; wird ein Kind gelöscht, werden alle seine Einträge und Dateien gelöscht.',
                'Wird die App gelöscht, sind alle Einträge auf diesem Handy gelöscht. Die Drive-Sicherung bleibt auch nach dem Löschen der App bestehen; lösche sie wie unten beschrieben. Sicherungen und geteilte Dateien löschst du bitte selbst dort, wo du sie gespeichert hast.',
                '<strong>Drive-Sicherung löschen:</strong> „Automatische Sicherung ausschalten“ stoppt nur das Hochladen und lässt die Sicherung in Drive bestehen. Mit <strong>Sicherung aus Drive löschen</strong> in der App wird die gesamte Drive-Sicherung gelöscht. Ohne App geht es unter Google Drive › Einstellungen › Apps verwalten › Dear Crayon › Versteckte App-Daten löschen; den Zugriff entziehst du unter Google-Konto › Sicherheit › Drittanbieter-Apps.',
                'Da nichts auf einem Server des Entwicklers gespeichert wird, gibt es keine Daten, deren Löschung beim Entwickler beantragt werden müsste. Die Drive-Sicherung liegt im eigenen Google-Konto der Eltern und kann jederzeit von ihnen gelöscht werden.',
            ])]),
            ('5. Datenschutz für Kinder', [('ul', [
                'Gemäß DSGVO (Kinder), COPPA (USA) und dem koreanischen Datenschutzgesetz bitten wir um die Einwilligung eines Elternteils, bevor die Stimme des Kindes an einen Server gesendet wird. Auch die automatische Google-Drive-Sicherung läuft nur, wenn ein Elternteil sich anmeldet und sie einschaltet.',
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
            ('2. Leistung', [('p', 'Die App ist ein Werkzeug für Eltern, um Bildfotos, Stimme und Worte ihres Kindes festzuhalten und Monatskarten und Bücher (ein Jahr an Einträgen) zu erstellen, anzusehen und zu teilen. Die Einträge werden auf dem Handy der Nutzer gespeichert und, wenn die automatische Google-Drive-Sicherung (freiwillig) eingeschaltet ist, zusätzlich in einem App-eigenen Bereich im eigenen Google Drive der Nutzer. Auf Servern des Entwicklers werden sie nicht gespeichert.')]),
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
            ('6. Deine Einträge', [('p', 'Die Rechte an den Bildern, Aufnahmen und Worten, die du hinzufügst, liegen bei dir (Eltern und Kind). Der Entwickler erhält und nutzt diese Einträge nicht. Ist Sprache-zu-Text eingeschaltet, werden Aufnahmen nur zur Umwandlung in Text verwendet und nicht gespeichert. Die automatische Google-Drive-Sicherung wird direkt in deinem eigenen Drive gespeichert; der Entwickler kann sie nicht sehen.')]),
            ('7. Sicherung ist deine Sache', [('p', 'Die automatische Systemsicherung von Android ist aus. Ohne Sicherung lassen sich die Einträge nicht wiederherstellen, wenn das Handy verloren geht oder kaputtgeht oder die App gelöscht wird. Schalte unter Meine Kinder › Sichern &amp; exportieren die automatische Google-Drive-Sicherung ein (freiwillig – auf einem neuen Handy meldest du dich mit Google an und stellst sie wieder her) oder erstelle eine Sicherungsdatei und bewahre sie sicher auf. Die Drive-Sicherung lädt bei geöffneter App hoch (standardmäßig im WLAN), daher sind die neuesten Einträge möglicherweise noch nicht hochgeladen.')]),
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
            ('Über diese Seite', [('p', 'Diese Seite erklärt, wie du Daten in der Android-App „Dear Crayon“ löschst. Dear Crayon hat kein Dear-Crayon-Konto und keinen Serverspeicher des Entwicklers. Name, Bilder, Stimme und Worte deines Kindes liegen auf deinem Handy und, wenn du die automatische Google-Drive-Sicherung eingeschaltet hast, auch in einem App-eigenen Bereich in deinem eigenen Google Drive. Du kannst sie selbst sofort löschen, und es gibt keine Daten, die der Entwickler für dich löschen könnte.')]),
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
            ]), ('p', 'Alle Einträge und Einstellungen auf dem Handy werden sofort gelöscht. Die automatische Systemsicherung von Android ist aus. Hast du jedoch die Google-Drive-Sicherung der App eingeschaltet, bleibt die Sicherung in Drive bestehen – lösche sie wie unter „Google-Drive-Sicherung löschen“ beschrieben.')]),
            ('Google-Drive-Sicherung löschen', [('ol', [
                '<strong>In der App:</strong> Meine Kinder › <strong>Sichern &amp; exportieren</strong> › auf <strong>Sicherung aus Drive löschen</strong> tippen und bestätigen. Die gesamte Drive-Sicherung wird gelöscht.',
                '<strong>Ohne App:</strong> Google Drive › <strong>Einstellungen</strong> › <strong>Apps verwalten</strong> › <strong>Dear Crayon</strong> › <strong>Versteckte App-Daten löschen</strong>.',
                '<strong>Zugriff entziehen:</strong> Google-Konto › <strong>Sicherheit</strong> › <strong>Drittanbieter-Apps</strong> und den Zugriff von Dear Crayon entfernen.',
            ]), ('p', '<strong>Automatische Sicherung ausschalten</strong> stoppt nur das Hochladen und lässt die Sicherung in Drive bestehen. Solange sie eingeschaltet ist, werden in der App gelöschte Einträge beim nächsten Hochladen auch aus der Drive-Sicherung gelöscht.')]),
            ('Sprache-zu-Text ausschalten', [('p', 'Meine Kinder › oben rechts ⚙ <strong>Einstellungen</strong> › <strong>Datenschutz</strong> › <strong>Stimme in Text umwandeln</strong> ausschalten. Dann verlassen Aufnahmen das Handy nicht mehr. Der Relay-Server speichert ohnehin weder Aufnahmen noch Text, dort gibt es also nichts zu löschen.')]),
            ('Dateien außerhalb des Handys', [('ul', [
                '<strong>Sicherungen und geteilte Dateien:</strong> Selbst erstellte Sicherungen und an die Familie gesendete Karten- oder Buchdateien löschst du bitte dort, wo du sie gespeichert hast (Dateien, Cloud, Messenger usw.). Dateien auf dem Handy der Empfänger müssen diese selbst löschen.',
                '<strong>Google-Drive-Sicherung:</strong> Hast du die automatische Sicherung eingeschaltet, liegt sie in einem App-eigenen Bereich in deinem eigenen Google Drive. Lösche sie wie unter „Google-Drive-Sicherung löschen“ beschrieben.',
                '<strong>Kaufverlauf:</strong> Käufe des Buch-PDFs bleiben im Google-Play-Kaufverlauf deines Google-Kontos, einsehbar unter Google-Konto › Zahlungen und Abos.',
            ])]),
            ('Was gelöscht wird und wie lange es bleibt', [('dl', [
                ('Angaben zum Kind, Kunstwerkfotos, Stimme, Antworten, Zitate, Notizen der Eltern, Einstellungen', 'Gespeichert im App-Speicher auf dem Handy der Nutzer. Sofort gelöscht, wenn du einen der Wege oben nutzt.'),
                ('Sprache-zu-Text-Anfragen', 'Werden auf dem Relay-Server nicht gespeichert. Nach der Rückgabe des Textes bleibt nichts zurück.'),
                ('Automatische Google-Drive-Sicherung (wenn eingeschaltet)', 'Gespeichert in einem versteckten, App-eigenen Bereich im eigenen Google Drive der Nutzer (der Entwickler kann ihn nicht sehen). Sofort gelöscht mit „Sicherung aus Drive löschen“ in der App oder „Versteckte App-Daten löschen“ in Google Drive. In der App gelöschte Einträge werden beim nächsten Hochladen entfernt.'),
                ('Einträge auf einem Server des Entwicklers', 'Keine. Es gibt kein Dear-Crayon-Konto, keine Datenbank des Entwicklers, keine Werbe- oder Analysetools.'),
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
        desc='Une application Android pour garder les dessins et la voix de votre enfant, et faire de chaque année un livre. Les données restent sur votre téléphone — et, si vous l’activez, dans votre propre Google Drive.',
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
            ('Vos données restent chez vous', [('p', 'Pas d’inscription, et le développeur ne reçoit jamais vos données. Le prénom, les dessins, la voix et les mots de votre enfant sont conservés sur ce téléphone. Si un parent active la sauvegarde automatique Google Drive, ils sont aussi conservés dans un espace réservé à l’application dans <strong>le propre Google Drive du parent</strong>. Rien ne passe par les serveurs du développeur, qui ne peut donc pas les voir. Sinon, seule la transcription de la voix quitte le téléphone, si un parent l’autorise, et le serveur relais ne conserve ni enregistrement ni texte. Ni publicité, ni mesure d’audience, ni localisation. Détails dans la <a href="privacy.html">politique de confidentialité</a>.')]),
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
            'Les données sont conservées sur ce téléphone. Rien n’est conservé sur les serveurs du développeur, qui ne peut pas voir vos données. Ni compte Dear Crayon, ni base de données du développeur, ni publicité, mesure d’audience ou localisation.',
            'Si vous activez la sauvegarde automatique Google Drive (facultative), les données sont aussi conservées dans un espace réservé à l’application dans <strong>le propre Google Drive du parent</strong>. Elle est désactivée par défaut.',
            'Sinon, seule la transcription de la voix quitte le téléphone, si un parent l’autorise. Le serveur relais ne conserve ni enregistrement ni texte.',
            'Le PDF payant du livre s’achète via la facturation Google Play. Le développeur ne reçoit jamais vos données bancaires.',
        ],
        sections=[
            ('1. Ce que nous traitons et où c’est conservé', [('ul', [
                'Prénom, date de naissance, nom d’artiste et photo de profil de l’enfant ; photos des œuvres ; enregistrements de la voix de l’enfant ; ce que l’enfant a dit et répondu ; citations ; notes des parents ; réglages de l’application.',
                'Tout est conservé dans <strong>le stockage de l’application sur ce téléphone</strong>. Uniquement si un parent active la sauvegarde automatique Google Drive, le même contenu est aussi conservé dans un espace réservé à l’application dans <strong>le propre Google Drive du parent</strong> (voir section 2). Dear Crayon n’a ni inscription, ni base de données, ni stockage serveur propres, et le développeur ne reçoit ni ne voit jamais ces données. La connexion Google sert uniquement à activer la sauvegarde Drive.',
                'Nous n’utilisons ni publicité, ni mesure d’audience, ni localisation.',
                'La sauvegarde automatique du système Android est désactivée. L’application propose deux sauvegardes : des fichiers (zip) créés par un parent, et la sauvegarde automatique Google Drive, facultative, qu’un parent active (désactivée par défaut).',
            ])]),
            ('2. Quand quelque chose quitte le téléphone', [('ul', [
                '<strong>Voix en texte (facultatif) :</strong> uniquement si un parent l’autorise lors du premier enregistrement, l’enregistrement à transcrire et le réglage de langue sont envoyés au serveur relais de Dear Crayon (Cloudflare Workers). Le serveur relais fait produire le texte par Cloudflare Workers AI (reconnaissance vocale Whisper, Cloudflare, Inc., États-Unis), le renvoie, et ne conserve ni l’enregistrement ni le texte. Aucune autre donnée, comme le prénom de l’enfant, n’est envoyée. Vous pouvez désactiver cette fonction à tout moment dans Réglages › Confidentialité ; rien n’est alors envoyé.',
                '<strong>Sauvegarde automatique Google Drive (facultative) :</strong> désactivée par défaut. Si un parent se connecte avec Google et l’active (« Continuer avec Google » sur le premier écran, ou Mes enfants › Sauvegarde et export), le même contenu qu’un fichier de sauvegarde — infos de l’enfant, photos des œuvres en qualité d’origine, enregistrements de voix, réponses et mots de l’enfant, citations, notes des parents et livres reçus de la famille — est envoyé dans un dossier caché, réservé à l’application, dans <strong>le propre Google Drive du parent</strong> (autorisation Google drive.appdata). Ce dossier n’apparaît pas dans l’interface de Drive ; il utilise seulement de l’espace de stockage. L’application ne peut voir aucun autre fichier de votre Drive. Les données vont directement du téléphone à Google Drive (Google LLC) ; elles ne passent par aucun serveur du développeur et n’y sont pas conservées, le développeur ne peut donc pas les voir. Par défaut, l’envoi se fait uniquement en Wi‑Fi et seulement quand l’application est ouverte (un bouton permet les données mobiles). Les éléments supprimés dans l’application sont aussi supprimés de la sauvegarde Drive au prochain envoi. L’adresse e-mail du compte connecté est conservée uniquement sur ce téléphone, pour indiquer quel compte est utilisé.',
                '<strong>Achat du PDF du livre :</strong> le PDF du livre en haute résolution, prêt à imprimer, s’achète via la facturation Google Play. Google traite le moyen de paiement et les données de facturation ; le développeur ne reçoit jamais vos données bancaires. L’application reçoit seulement la confirmation de l’achat et l’enregistre sur ce téléphone. Le développeur n’utilise les informations de transaction de la Google Play Console, comme le numéro de commande, que pour traiter les remboursements et les demandes d’aide.',
                '<strong>Fichiers partagés par un parent :</strong> les cartes du mois, PDF des livres, fichiers de livre et sauvegardes ne quittent le téléphone que lorsqu’un parent les envoie via l’application de son choix (messagerie, e-mail, etc.). Le destinataire dispose alors de ce fichier.',
            ])]),
            ('3. Autorisations du téléphone', [('ul', [
                'Appareil photo : pour photographier les œuvres.',
                'Micro : pour enregistrer la voix de l’enfant.',
                'Notifications : rappels des histoires du mois et des anniversaires. Tout le reste fonctionne si vous refusez.',
            ])]),
            ('4. Durée de conservation et suppression', [('ul', [
                'Les données restent sur ce téléphone jusqu’à ce qu’un parent les supprime. Si la sauvegarde automatique Google Drive est activée, la sauvegarde Drive reste aussi dans le compte Google du parent jusqu’à ce qu’il la supprime.',
                'Les œuvres, réponses et citations peuvent être supprimées une par une dans l’application ; supprimer un enfant efface toutes ses données et tous ses fichiers.',
                'Supprimer l’application efface toutes les données de ce téléphone. La sauvegarde Drive reste même après la suppression de l’application : supprimez-la comme indiqué ci-dessous. Supprimez vous-même les sauvegardes et fichiers partagés là où vous les avez enregistrés.',
                '<strong>Supprimer la sauvegarde Drive :</strong> « Désactiver la sauvegarde automatique » arrête seulement les envois et laisse la sauvegarde dans Drive. <strong>Supprimer la sauvegarde de Drive</strong> dans l’application efface toute la sauvegarde Drive. Sans l’application, vous pouvez la supprimer dans Google Drive › Paramètres › Gérer les applications › Dear Crayon › Supprimer les données d’application masquées, et retirer l’accès dans Compte Google › Sécurité › Applications tierces.',
                'Comme rien n’est conservé sur un serveur du développeur, il n’y a aucune donnée dont il faudrait demander la suppression au développeur. La sauvegarde Drive se trouve dans le propre compte Google du parent, qui peut la supprimer à tout moment.',
            ])]),
            ('5. Protection des données des enfants', [('ul', [
                'Conformément au RGPD (enfants), au COPPA (États-Unis) et à la loi coréenne sur la protection des données personnelles, nous demandons le consentement d’un parent avant d’envoyer la voix de l’enfant à un serveur. La sauvegarde automatique Google Drive ne fonctionne elle aussi que si un parent se connecte et l’active.',
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
            ('2. Le service', [('p', 'L’application permet aux parents de garder les photos des dessins, la voix et les mots de leur enfant, et de créer, consulter et partager des cartes du mois et des livres (une année de souvenirs). Les données sont conservées sur le téléphone de l’utilisateur et, s’il active la sauvegarde automatique Google Drive (facultative), aussi dans un espace réservé à l’application dans son propre Google Drive. Elles ne sont pas conservées sur les serveurs du développeur.')]),
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
            ('6. Vos données', [('p', 'Les droits sur les dessins, voix et mots que vous ajoutez vous appartiennent (au parent et à l’enfant). Le développeur ne reçoit ni n’utilise ces données. Si la transcription de la voix est activée, les enregistrements servent uniquement à produire le texte et ne sont pas conservés. La sauvegarde automatique Google Drive est enregistrée directement dans votre propre Drive, et le développeur ne peut pas la voir.')]),
            ('7. La sauvegarde vous revient', [('p', 'La sauvegarde automatique du système Android est désactivée. Sans sauvegarde, les données ne peuvent pas être récupérées en cas de perte ou de panne du téléphone, ou si vous supprimez l’application. Dans Mes enfants › Sauvegarde et export, activez la sauvegarde automatique Google Drive (facultative — sur un nouveau téléphone, connectez-vous avec Google pour restaurer) ou créez un fichier de sauvegarde et gardez-le en lieu sûr. La sauvegarde Drive s’envoie quand l’application est ouverte (en Wi‑Fi par défaut) : les données les plus récentes peuvent ne pas encore y figurer.')]),
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
            ('À propos de cette page', [('p', 'Cette page explique comment supprimer les données de l’application Android « Dear Crayon ». Dear Crayon n’a ni compte Dear Crayon ni stockage sur les serveurs du développeur. Le prénom, les dessins, la voix et les mots de votre enfant se trouvent sur votre téléphone et, si vous avez activé la sauvegarde automatique Google Drive, aussi dans un espace réservé à l’application dans votre propre Google Drive. Vous pouvez les supprimer vous-même, immédiatement, et le développeur n’a aucune donnée à supprimer à votre place.')]),
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
            ]), ('p', 'Toutes les données et tous les réglages du téléphone sont supprimés immédiatement. La sauvegarde automatique du système Android est désactivée. Mais si vous avez activé la sauvegarde automatique Google Drive de l’application, la sauvegarde reste dans Drive — supprimez-la comme indiqué dans « Supprimer la sauvegarde Google Drive ».')]),
            ('Supprimer la sauvegarde Google Drive', [('ol', [
                '<strong>Dans l’application :</strong> Mes enfants › <strong>Sauvegarde et export</strong> › touchez <strong>Supprimer la sauvegarde de Drive</strong> et confirmez. Toute la sauvegarde Drive est supprimée.',
                '<strong>Sans l’application :</strong> Google Drive › <strong>Paramètres</strong> › <strong>Gérer les applications</strong> › <strong>Dear Crayon</strong> › <strong>Supprimer les données d’application masquées</strong>.',
                '<strong>Retirer l’accès :</strong> Compte Google › <strong>Sécurité</strong> › <strong>Applications tierces</strong>, puis supprimez l’accès de Dear Crayon.',
            ]), ('p', '<strong>Désactiver la sauvegarde automatique</strong> arrête seulement les envois et laisse la sauvegarde dans Drive. Tant qu’elle est activée, les éléments supprimés dans l’application sont aussi supprimés de la sauvegarde Drive au prochain envoi.')]),
            ('Désactiver la transcription de la voix', [('p', 'Mes enfants › ⚙ <strong>Réglages</strong> en haut à droite › <strong>Confidentialité</strong> › désactivez <strong>Transformer la voix en texte</strong>. Les enregistrements ne quittent alors plus le téléphone. Le serveur relais ne conserve de toute façon ni enregistrement ni texte : il n’y a rien à y supprimer.')]),
            ('Fichiers hors du téléphone', [('ul', [
                '<strong>Sauvegardes et fichiers partagés :</strong> supprimez vous-même les sauvegardes que vous avez créées et les fichiers de carte ou de livre envoyés à la famille, là où vous les avez enregistrés (Fichiers, cloud, messagerie, etc.). Les fichiers sur le téléphone d’un destinataire doivent être supprimés par celui-ci.',
                '<strong>Sauvegarde Google Drive :</strong> si vous avez activé la sauvegarde automatique, elle se trouve dans un espace réservé à l’application dans votre propre Google Drive. Supprimez-la comme indiqué dans « Supprimer la sauvegarde Google Drive ».',
                '<strong>Historique d’achat :</strong> les achats du PDF du livre restent dans l’historique d’achats Google Play de votre compte Google, visible dans Compte Google › Paiements et abonnements.',
            ])]),
            ('Ce qui est supprimé et durée de conservation', [('dl', [
                ('Infos de l’enfant, photos d’œuvres, voix, réponses, citations, notes des parents, réglages', 'Conservés dans le stockage de l’application sur le téléphone de l’utilisateur. Supprimés immédiatement avec les méthodes ci-dessus.'),
                ('Demandes de transcription', 'Non conservées sur le serveur relais. Rien ne reste une fois le texte renvoyé.'),
                ('Sauvegarde automatique Google Drive (si activée)', 'Conservée dans un espace caché, réservé à l’application, dans le propre Google Drive de l’utilisateur (le développeur ne peut pas la voir). Supprimée immédiatement avec « Supprimer la sauvegarde de Drive » dans l’application ou « Supprimer les données d’application masquées » dans Google Drive. Les éléments supprimés dans l’application sont retirés au prochain envoi.'),
                ('Données conservées sur un serveur du développeur', 'Aucune. Ni compte Dear Crayon, ni base de données du développeur, ni outil de publicité ou de mesure d’audience.'),
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
        desc='Una app de Android para guardar los dibujos y la voz de tu peque y convertir cada año en un libro. Los registros se quedan en tu móvil y, si lo activas, en tu propio Google Drive.',
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
            ('Tus registros se quedan contigo', [('p', 'No hay registro de usuario, y el desarrollador nunca recibe tus registros. El nombre, los dibujos, la voz y las palabras de tu peque se guardan en este móvil. Si un adulto activa la copia de seguridad automática en Google Drive, también se guardan en un espacio exclusivo de la app en <strong>el propio Google Drive de ese adulto</strong>. Nada pasa por los servidores del desarrollador, así que el desarrollador no puede verlos. Aparte de eso, solo sale del móvil la conversión de voz a texto, si un adulto la permite, y el servidor intermediario no guarda grabaciones ni textos. Sin publicidad, análisis de uso ni ubicación. Más detalles en la <a href="privacy.html">política de privacidad</a>.')]),
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
            'Los registros se guardan en este móvil. No se guarda nada en los servidores del desarrollador, y el desarrollador no puede ver tus registros. Sin cuenta de Dear Crayon, sin base de datos del desarrollador, sin publicidad, análisis ni ubicación.',
            'Si activas la copia de seguridad automática en Google Drive (opcional), los registros también se guardan en un espacio exclusivo de la app en <strong>el propio Google Drive del adulto</strong>. Viene desactivada.',
            'Aparte de eso, solo sale del móvil la conversión de voz a texto, si un adulto la permite. El servidor intermediario no guarda grabaciones ni textos.',
            'El PDF de pago del libro se compra con la facturación de Google Play. El desarrollador nunca recibe los datos de tu tarjeta.',
        ],
        sections=[
            ('1. Qué tratamos y dónde se guarda', [('ul', [
                'Nombre, fecha de nacimiento, nombre de artista y foto de perfil del niño; fotos de las obras; grabaciones de su voz; lo que dijo y respondió; frases; notas de los padres; ajustes de la app.',
                'Todo se guarda en <strong>el almacenamiento de la app en este móvil</strong>. Solo si un adulto activa la copia de seguridad automática en Google Drive, el mismo contenido se guarda también en un espacio exclusivo de la app en <strong>el propio Google Drive del adulto</strong> (ver el apartado 2). Dear Crayon no tiene registro de usuarios, ni base de datos, ni almacenamiento en servidores propios, y el desarrollador nunca recibe ni ve estos registros. El inicio de sesión con Google solo se usa para activar la copia en Drive.',
                'No usamos publicidad, análisis de uso ni ubicación.',
                'La copia de seguridad automática del sistema Android está desactivada. La app ofrece dos tipos de copia: archivos (zip) que crea un adulto y la copia de seguridad automática en Google Drive, opcional, que activa un adulto (viene desactivada).',
            ])]),
            ('2. Cuándo sale algo del móvil', [('ul', [
                '<strong>Voz a texto (opcional):</strong> solo si un adulto lo permite en la primera grabación, la grabación que se va a transcribir y el ajuste de idioma se envían al servidor intermediario de Dear Crayon (Cloudflare Workers). El servidor intermediario obtiene el texto de Cloudflare Workers AI (reconocimiento de voz Whisper, Cloudflare, Inc., Estados Unidos), lo devuelve y no guarda ni la grabación ni el texto. No se envía ningún otro dato, como el nombre del niño. Puedes desactivarlo cuando quieras en Ajustes › Privacidad; entonces no se envía nada.',
                '<strong>Copia de seguridad automática en Google Drive (opcional):</strong> viene desactivada. Si un adulto inicia sesión con Google y la activa («Continuar con Google» en la primera pantalla, o Mis peques › Copia y exportación), el mismo contenido que un archivo de copia —datos del niño, fotos de las obras en calidad original, grabaciones de voz, respuestas y palabras del niño, frases, notas de los padres y libros recibidos de la familia— se sube a una carpeta oculta y exclusiva de la app en <strong>el propio Google Drive del adulto</strong> (permiso de Google drive.appdata). Esta carpeta no aparece en la interfaz de Drive; solo ocupa espacio de almacenamiento. La app no puede ver ningún otro archivo de tu Drive. Los datos van directamente entre el móvil y Google Drive (Google LLC); no pasan por ningún servidor del desarrollador ni se guardan en él, así que el desarrollador no puede verlos. Por defecto solo se sube con Wi‑Fi y solo con la app abierta (un interruptor permite usar datos móviles). Lo que se borra en la app también se borra de la copia en Drive en la siguiente subida. El correo de la cuenta con la que se inició sesión se guarda solo en este móvil, para mostrar qué cuenta se usa.',
                '<strong>Compra del PDF del libro:</strong> el PDF del libro en alta resolución, listo para imprimir, se compra con la facturación de Google Play. Google gestiona el método de pago y los datos de facturación; el desarrollador nunca recibe los datos de tu tarjeta. La app solo recibe la confirmación de la compra y la registra en este móvil. El desarrollador usa los datos de la transacción de Google Play Console, como el número de pedido, solo para gestionar reembolsos y consultas.',
                '<strong>Archivos que comparten los padres:</strong> las tarjetas del mes, los PDF de los libros, los archivos de libro y las copias de seguridad solo salen del móvil cuando un adulto los envía con la app que elija (mensajería, correo, etc.). Quien los recibe tendrá ese archivo.',
            ])]),
            ('3. Permisos del móvil', [('ul', [
                'Cámara: para fotografiar las obras.',
                'Micrófono: para grabar la voz del niño.',
                'Notificaciones: recordatorios de las historias del mes y de los cumpleaños. Si los rechazas, todo lo demás sigue funcionando.',
            ])]),
            ('4. Conservación y borrado', [('ul', [
                'Los registros permanecen en este móvil hasta que un adulto los borra. Si la copia de seguridad automática en Google Drive está activada, la copia en Drive también permanece en la cuenta de Google del adulto hasta que la borre.',
                'Las obras, respuestas y frases se pueden borrar una a una en la app; al borrar a un niño se borran todos sus registros y archivos.',
                'Al borrar la app se borran todos los registros de este móvil. La copia en Drive se mantiene aunque borres la app, así que bórrala como se explica abajo. Borra tú las copias de seguridad y los archivos compartidos allí donde los guardaste.',
                '<strong>Borrar la copia en Drive:</strong> «Desactivar la copia automática» solo detiene las subidas y deja la copia en Drive. <strong>Borrar la copia de Drive</strong> en la app borra toda la copia en Drive. Sin la app, puedes borrarla en Google Drive › Configuración › Gestionar aplicaciones › Dear Crayon › Eliminar datos ocultos de la aplicación, y retirar el acceso en Cuenta de Google › Seguridad › Aplicaciones de terceros.',
                'Como no se guarda nada en ningún servidor del desarrollador, no hay datos cuyo borrado tengas que pedir al desarrollador. La copia en Drive está en la propia cuenta de Google del adulto, que puede borrarla cuando quiera.',
            ])]),
            ('5. Privacidad de los niños', [('ul', [
                'De acuerdo con el RGPD (menores), la COPPA (EE. UU.) y la ley coreana de protección de datos personales, pedimos el consentimiento de un adulto antes de enviar la voz del niño a un servidor. La copia de seguridad automática en Google Drive también funciona solo si un adulto inicia sesión y la activa.',
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
            ('2. El servicio', [('p', 'La app es una herramienta para que madres y padres guarden las fotos de los dibujos, la voz y las palabras de sus hijos, y para crear, ver y compartir tarjetas del mes y libros (un año de recuerdos). Los registros se guardan en el móvil de quien usa la app y, si activa la copia de seguridad automática en Google Drive (opcional), también en un espacio exclusivo de la app en su propio Google Drive. No se guardan en los servidores del desarrollador.')]),
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
            ('6. Tus registros', [('p', 'Los derechos sobre los dibujos, la voz y las palabras que añades son tuyos (de los padres y del niño). El desarrollador no recibe ni usa estos registros. Si la voz a texto está activada, las grabaciones solo se usan para obtener el texto y no se guardan. La copia de seguridad automática en Google Drive se guarda directamente en tu propio Drive, y el desarrollador no puede verla.')]),
            ('7. La copia de seguridad es cosa tuya', [('p', 'La copia de seguridad automática del sistema Android está desactivada. Sin copia, si pierdes o se estropea el móvil, o borras la app, los registros no se podrán recuperar. En Mis peques › Copia y exportación, activa la copia de seguridad automática en Google Drive (opcional; en un móvil nuevo, inicia sesión con Google para restaurarla) o crea un archivo de copia y guárdalo en un lugar seguro. La copia en Drive se sube con la app abierta (con Wi‑Fi por defecto), así que puede que los registros más recientes aún no se hayan subido.')]),
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
            ('Sobre esta página', [('p', 'Esta página explica cómo borrar los datos de la app de Android «Dear Crayon». Dear Crayon no tiene cuenta de Dear Crayon ni almacenamiento en servidores del desarrollador. El nombre, los dibujos, la voz y las palabras de tu peque están en tu móvil y, si activaste la copia de seguridad automática en Google Drive, también en un espacio exclusivo de la app en tu propio Google Drive. Puedes borrarlos tú mismo al momento, y el desarrollador no tiene ningún dato que borrar por ti.')]),
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
            ]), ('p', 'Se borran al instante todos los registros y ajustes del móvil. La copia de seguridad automática del sistema Android está desactivada. Pero si activaste la copia automática en Google Drive de la app, la copia en Drive se mantiene: bórrala como se explica en «Borrar la copia en Google Drive».')]),
            ('Borrar la copia en Google Drive', [('ol', [
                '<strong>En la app:</strong> Mis peques › <strong>Copia y exportación</strong> › toca <strong>Borrar la copia de Drive</strong> y confirma. Se borra toda la copia en Drive.',
                '<strong>Sin la app:</strong> Google Drive › <strong>Configuración</strong> › <strong>Gestionar aplicaciones</strong> › <strong>Dear Crayon</strong> › <strong>Eliminar datos ocultos de la aplicación</strong>.',
                '<strong>Retirar el acceso:</strong> Cuenta de Google › <strong>Seguridad</strong> › <strong>Aplicaciones de terceros</strong> y elimina el acceso de Dear Crayon.',
            ]), ('p', '<strong>Desactivar la copia automática</strong> solo detiene las subidas y deja la copia en Drive. Mientras está activada, lo que borras en la app también se borra de la copia en Drive en la siguiente subida.')]),
            ('Desactivar la voz a texto', [('p', 'Mis peques › ⚙ <strong>Ajustes</strong> arriba a la derecha › <strong>Privacidad</strong> › desactiva <strong>Convertir la voz en texto</strong>. Así las grabaciones dejan de salir del móvil. El servidor intermediario nunca guarda grabaciones ni textos, así que allí no hay nada que borrar.')]),
            ('Archivos fuera del móvil', [('ul', [
                '<strong>Copias y archivos compartidos:</strong> borra tú las copias de seguridad que creaste y los archivos de tarjetas o libros que enviaste a la familia allí donde los guardaste (Archivos, nube, mensajería, etc.). Los archivos del móvil de quien los recibió debe borrarlos esa persona.',
                '<strong>Copia en Google Drive:</strong> si activaste la copia automática, está en un espacio exclusivo de la app en tu propio Google Drive. Bórrala como se explica en «Borrar la copia en Google Drive».',
                '<strong>Historial de compras:</strong> las compras del PDF del libro quedan en el historial de compras de Google Play de tu cuenta de Google, en Cuenta de Google › Pagos y suscripciones.',
            ])]),
            ('Qué se borra y cuánto tiempo se guarda', [('dl', [
                ('Datos del niño, fotos de obras, voz, respuestas, frases, notas de los padres, ajustes', 'Guardados en el almacenamiento de la app en el móvil de quien la usa. Se borran al momento con las opciones de arriba.'),
                ('Solicitudes de voz a texto', 'No se guardan en el servidor intermediario. No queda nada una vez devuelto el texto.'),
                ('Copia de seguridad automática en Google Drive (si está activada)', 'Guardada en un espacio oculto y exclusivo de la app en el propio Google Drive de quien la usa (el desarrollador no puede verla). Se borra al momento con «Borrar la copia de Drive» en la app o «Eliminar datos ocultos de la aplicación» en Google Drive. Lo que se borra en la app se elimina en la siguiente subida.'),
                ('Registros guardados en un servidor del desarrollador', 'Ninguno. No hay cuenta de Dear Crayon, ni base de datos del desarrollador, ni herramientas de publicidad o análisis.'),
            ])]),
            ('¿Necesitas ayuda?', [('p', f'Si estos pasos no lo resuelven, escribe a {MAIL} con el asunto «Borrar datos». Respondemos en un plazo de 7 días. Como el desarrollador no guarda ningún registro, te guiaremos por los pasos para borrarlos.')]),
        ],
    ),
)

# ───────────────────────────── 日本語
L['ja'] = dict(
    langName='日本語', name='Dear Crayon',
    nav=dict(home='ホーム', privacy='プライバシーポリシー', terms='利用規約', delete='データの削除'),
    langLabel='言語', effective='施行日 2026年10月19日', contact='お問い合わせ',
    footer='Dear Crayon · 運営: Dear Crayon 開発者(個人)',
    index=dict(
        links=dict(privacy='集める情報・使い道・消し方', terms='利用の条件・お支払いと返金', delete='記録を消す方法・手順のご案内'),
    ),
    privacy=dict(
        title='プライバシーポリシー',
        intro='Dear Crayon は、親が子どもの絵と声を記録するアプリです。子どもがひとりで使うためのアプリではなく、子どもの情報は親(法定代理人)が入力し、管理します。',
        mdEffective='施行日: 2026年10月19日',
        summaryTitle='ひと目でわかる要点',
        summary=[
            '記録はこのスマートフォンに保存されます。開発者のサーバーには保存せず、開発者が記録を見ることはできません。Dear Crayon の会員アカウント・独自のデータベース・広告・利用分析・位置情報はありません。',
            'Google ドライブ自動バックアップ(任意)をオンにすると、記録は<strong>親自身の Google ドライブ</strong>のアプリ専用領域にも保存されます。最初はオフです。',
            'そのほかにスマートフォンの外に出るのは、親が許可した「声を文字にする」機能だけです。中継サーバーは録音も文字も保存しません。',
            '有料の作品集PDFは Google Play の決済で購入します。開発者がカード情報を受け取ることはありません。',
        ],
        sections=[
            ('1. 扱う情報と保存場所', [('ul', [
                '子どもの名前・生年月日・作家名・プロフィール写真、作品の写真、子どもの声の録音、子どもが話したことと答え、今月のひとこと、親のメモ、アプリの設定。',
                'これらの情報は<strong>このスマートフォンの中のアプリ用ストレージ</strong>に保存されます。親が Google ドライブ自動バックアップをオンにした場合にかぎり、同じ内容が<strong>親自身の Google ドライブ</strong>のアプリ専用領域にも保存されます(下の2を参照)。Dear Crayon には会員登録・独自のデータベース・独自のサーバー保存がなく、開発者がこの記録を受け取ったり見たりすることはありません。Google ログインは、ドライブ自動バックアップをオンにするときだけ使います。',
                '広告、利用分析、位置情報は使いません。',
                'Android システムの自動バックアップはオフにしています。アプリ内のバックアップは、親が自分で作るファイル(zip)と、親がオンにする任意の Google ドライブ自動バックアップ(最初はオフ)の2つです。',
            ])]),
            ('2. スマートフォンの外に出る場合', [('ul', [
                '<strong>声を文字にする(任意):</strong> はじめて録音するときに親が許可した場合にかぎり、文字にする録音ファイルと言語設定を Dear Crayon の中継サーバー(Cloudflare Workers)へ送ります。中継サーバーは Cloudflare Workers AI(Whisper 音声認識、Cloudflare, Inc.、アメリカ)で文字を作って返し、録音も文字も保存しません。子どもの名前など、ほかの記録は送りません。設定 › プライバシーからいつでもオフにでき、オフにすると何も送りません。',
                '<strong>Google ドライブ自動バックアップ(任意):</strong> 最初はオフです。親が Google でログインしてオンにすると(最初の画面の「Google で始める」、または うちの子 › バックアップ)、バックアップファイルと同じ内容 — 子どもの情報、元の画質の作品の写真、声の録音、答えと子どもが話したこと、ひとこと、親のメモ、家族から届いた作品集 — を<strong>親自身の Google ドライブ</strong>の、アプリ専用の非表示フォルダにアップロードします(Google の権限 drive.appdata)。このフォルダはドライブの画面には表示されず、保存容量だけを使います。アプリがドライブのほかのファイルを見ることはできません。記録はスマートフォンと Google ドライブ(Google LLC)のあいだを直接やりとりし、開発者のサーバーを通ったり保存されたりしないため、開発者は見ることができません。初期設定では Wi‑Fi のときだけ、アプリを開いているあいだだけアップロードします(スイッチでモバイルデータも許可できます)。アプリで消したものは、次のアップロードのときにドライブのバックアップからも消えます。どのアカウントを使っているかを表示するため、ログインしたアカウントのメールアドレスをこのスマートフォンにだけ保存します。',
                '<strong>作品集PDFの購入:</strong> 印刷用の高画質な作品集PDFのダウンロードは、Google Play の決済で購入します。支払い方法と請求情報は Google が扱い、開発者がカード情報を受け取ることはありません。アプリは購入が完了したという確認だけを受け取り、このスマートフォンに記録します。開発者は Google Play Console の注文番号などの取引情報を、返金とお問い合わせへの対応にだけ使います。',
                '<strong>親が自分で送るファイル:</strong> 今月のカード、作品集PDF、作品集ファイル、バックアップファイルは、親が選んだアプリ(メッセージアプリ・メールなど)で自分で送るときだけ外に出ます。受け取った人がそのファイルを持つことになります。',
            ])]),
            ('3. スマートフォンの権限', [('ul', [
                'カメラ: 作品の写真を撮るとき。',
                'マイク: 子どもの声を録音するとき。',
                '通知: 毎月のおはなし・誕生日のお知らせ。許可しなくても、ほかの機能はそのまま使えます。',
            ])]),
            ('4. 保存期間と消し方', [('ul', [
                '記録は、親が消すまでこのスマートフォンに残ります。Google ドライブ自動バックアップをオンにした場合、ドライブのバックアップも親が消すまで親の Google アカウントに残ります。',
                '作品・答え・ひとことはアプリの中でひとつずつ消せます。子どもを削除すると、その子のすべての記録とファイルが消えます。',
                'アプリを削除すると、このスマートフォンの中のすべての記録が消えます。ドライブのバックアップはアプリを削除しても残るため、下の方法で消してください。バックアップファイルや送ったファイルは、保存した場所でご自身で消してください。',
                '<strong>ドライブのバックアップを消す:</strong>「自動バックアップをオフにする」はアップロードを止めるだけで、ドライブのバックアップは残ります。アプリの<strong>ドライブのバックアップを削除</strong>で、ドライブのバックアップ全体を消せます。アプリがなくても、Google ドライブ › 設定 › アプリの管理 › Dear Crayon › 非表示のアプリデータを削除 で消せます。Google アカウント › セキュリティ › サードパーティ製アプリ から、アクセス権を取り消せます。',
                '開発者のサーバーに残る記録がないため、開発者に削除を依頼していただくデータはありません。ドライブのバックアップは親自身の Google アカウントにあり、親がいつでも消せます。',
            ])]),
            ('5. 子どもの個人情報の保護', [('ul', [
                'アメリカの児童オンラインプライバシー保護法(COPPA)、ヨーロッパの一般データ保護規則(GDPR)の子どもに関する規定、韓国の個人情報保護法、日本の個人情報保護法にしたがい、子どもの声をサーバーへ送る前に親の同意をいただきます。Google ドライブ自動バックアップも、親が自分でログインしてオンにしたときだけ動きます。',
                '親はいつでも、子どもの情報を見る・なおす・消すこと、同意を取り消すことができます(すべてアプリの中ですぐに)。',
            ])]),
            ('6. お問い合わせ', [('ul', [
                '運営者: Dear Crayon 開発者(個人)',
                f'連絡先: {MAIL}',
                f'Web: <a href="{BASE}ja/privacy.html">{BASE}ja/privacy.html</a>',
            ])]),
        ],
        closing='このポリシーが変わるときは、アプリとこのページの施行日を更新してお知らせします。',
    ),
    terms=dict(
        title='利用規約',
        sections=[
            ('1. 規約の適用', [('p', 'この規約は、Dear Crayon(以下「アプリ」)を使うために必要なことを定めます。アプリをインストールして使うと、この規約に同意したものとみなします。アプリのダウンロードと決済には、Google Play の利用規約もあわせて適用されます。')]),
            ('2. サービスの内容', [('p', 'アプリは、親が子どもの絵の写真・声・ことばを記録し、今月のカードと作品集(子どもの1年の記録の本)を作って見たり、分けあったりするための道具です。記録は利用者のスマートフォンに保存され、利用者が Google ドライブ自動バックアップ(任意)をオンにすると、利用者自身の Google ドライブのアプリ専用領域にも保存されます。開発者のサーバーには保存しません。')]),
            ('3. ご利用いただける方', [('ul', [
                'アプリは保護者(大人)が使うアプリです。子どもがひとりで使うためには作っていません。',
                '親は、自分が保護する子どもの情報を記録します。ほかの人の写真や声を残すときは、その人(またはその保護者)の許可を得てください。',
            ])]),
            ('4. 料金とお支払い', [('ul', [
                'アプリのインストール、記録、今月のカード、作品集を見る・分けあう(「プレビュー」表示)は無料です。',
                '印刷用の高画質な作品集PDFのダウンロードは有料です。価格は、お支払いの前に Google Play の決済画面に表示されます。',
                'お支払いは Google Play の決済で処理されます。支払い方法と請求は Google が扱い、開発者がカード情報を受け取ることはありません。',
            ])]),
            ('5. 返金', [('ul', [
                '返金は <a href="https://support.google.com/googleplay/answer/2479637?hl=ja" rel="noopener">Google Play の返金ポリシー</a>にしたがいます。購入後48時間以内は Google Play から直接返金を申し込めます。それ以降は、下のメールアドレスへお問い合わせください。',
                '関係する法令が保障する消費者の権利は、この規約によって狭められることはありません。',
            ])]),
            ('6. 利用者の記録', [('p', 'アプリに残した絵・声・文章の権利は、利用者(親と子ども)にあります。開発者はこの記録を受け取ったり使ったりしません。「声を文字にする」をオンにした場合も、録音は文字にするためだけに使われ、保存されません。Google ドライブ自動バックアップも利用者自身のドライブに直接保存され、開発者は見ることができません。')]),
            ('7. バックアップは利用者が', [('p', 'Android システムの自動バックアップはオフです。バックアップがないと、スマートフォンをなくしたり、こわれたり、アプリを削除したりしたときに記録を復元できません。うちの子 › バックアップで Google ドライブ自動バックアップをオンにするか(任意 — 新しいスマートフォンで Google にログインすると復元できます)、バックアップファイルを作って安全な場所に保管してください。ドライブ自動バックアップはアプリを開いているあいだ(初期設定では Wi‑Fi のとき)にアップロードされるため、いちばん新しい記録はまだアップロードされていないことがあります。')]),
            ('8. 結果の限界', [('ul', [
                '「声を文字にする」はまちがえることがあります。文字はいつでもなおせます。',
                '作品集PDFを印刷すると、プリンターや印刷所によって色や大きさが変わることがあります。',
            ])]),
            ('9. 分けあうこと', [('p', '親が送ったカード・作品集・バックアップファイルは受け取った人のものになり、送ったあとにアプリから取り消すことはできません。だれに送るかは親が決めます。')]),
            ('10. してはいけないこと', [('ul', [
                '法律に反したり、ほかの人の権利を侵害したりするためにアプリを使うこと。',
                'アプリを改造したり、決済を回避したりすること。',
            ])]),
            ('11. 責任の制限', [('p', 'アプリは現状のまま提供されます。法令が認める範囲で、アプリの利用によって生じた記録の消失などの損害について責任を負いません。ただし、開発者に故意または重大な過失がある場合は除きます。')]),
            ('12. 変更と中止', [('p', '機能は変わったり、止まったりすることがあります。大切な変更は、アプリのアップデートとこのページでお知らせします。サービスを止めても、スマートフォンの中の記録とすでにダウンロードしたPDFはそのまま使えます。')]),
            ('13. 準拠法', [('p', 'この規約は大韓民国の法律にしたがいます。ほかの国に住む消費者は、その国の法律が保障する保護をそのまま受けられます。')]),
            ('14. お問い合わせ', [('p', f'規約に関するお問い合わせは {MAIL} へお送りください。')]),
        ],
    ),
    delete=dict(
        title='データの削除について',
        sections=[
            ('このページについて', [('p', 'Android アプリ「Dear Crayon」のデータ削除のご案内です。Dear Crayon には会員アカウントも開発者のサーバーへの保存もありません。子どもの名前・絵・声・文章は利用者のスマートフォンにあり、Google ドライブ自動バックアップをオンにした場合は、利用者自身の Google ドライブのアプリ専用領域にもあります。そのため利用者がご自身ですぐに消すことができ、開発者がかわりに消すデータはありません。')]),
            ('方法1. 記録をひとつずつ消す', [('ol', [
                '<strong>作品:</strong> 作品を開き、右上の ⋯ › <strong>作品を削除</strong> › 削除。写真・声・おはなしがいっしょに消えます。',
                '<strong>答え:</strong> おはなしの画面で答えのメニュー(⋯) › <strong>答えを削除</strong>。',
                '<strong>ひとこと:</strong> ひとことをタップ › <strong>削除</strong>。',
            ])]),
            ('方法2. 子どものすべての記録を消す', [('ol', [
                '下の<strong>うちの子</strong>タブを開きます。',
                '<strong>子どもの情報をなおす</strong>をタップします。',
                'いちばん下の<strong>子どもを削除</strong>をタップして確認します。',
            ]), ('p', 'その子の作品の写真・声・答え・ひとこと・プロフィール写真がすべて消え、元に戻せません。残しておきたいときは、先にうちの子 › バックアップでファイルを作っておいてください。')]),
            ('方法3. アプリのすべての記録を消す', [('ol', [
                'スマートフォンの<strong>設定</strong> › <strong>アプリ</strong> › <strong>Dear Crayon</strong> を開きます。',
                '<strong>アンインストール</strong>をタップします。アプリを残したいときは、<strong>ストレージ</strong> › <strong>データを消去</strong>をタップします。',
            ]), ('p', 'スマートフォンの中のすべての記録と設定がすぐに消えます。Android システムの自動バックアップはオフです。ただし、アプリの Google ドライブ自動バックアップをオンにしていた場合、ドライブのバックアップはそのまま残ります。下の「Google ドライブのバックアップを消す」で消してください。')]),
            ('Google ドライブのバックアップを消す', [('ol', [
                '<strong>アプリで:</strong> うちの子 › <strong>バックアップ</strong> › <strong>ドライブのバックアップを削除</strong>をタップして確認します。ドライブのバックアップ全体が消えます。',
                '<strong>アプリなしで:</strong> Google ドライブ › <strong>設定</strong> › <strong>アプリの管理</strong> › <strong>Dear Crayon</strong> › <strong>非表示のアプリデータを削除</strong>。',
                '<strong>アクセス権を取り消す:</strong> Google アカウント › <strong>セキュリティ</strong> › <strong>サードパーティ製アプリ</strong>で、Dear Crayon のアクセスを削除します。',
            ]), ('p', '<strong>自動バックアップをオフにする</strong>と、アップロードが止まるだけで、ドライブのバックアップは残ります。オンのあいだにアプリで消した記録は、次のアップロードのときにドライブのバックアップからも消えます。')]),
            ('「声を文字にする」をオフにする', [('p', 'うちの子 › 右上の ⚙ <strong>設定</strong> › <strong>プライバシー</strong> › <strong>子どもの声を文字にする</strong>をオフにします。オフにすると、録音をスマートフォンの外へ送りません。中継サーバーははじめから録音も文字も保存しないため、別に消すものはありません。')]),
            ('スマートフォンの外にあるファイル', [('ul', [
                '<strong>バックアップ・送ったファイル:</strong> 親が作ったバックアップファイル、家族に送ったカード・作品集のファイルは、保存した場所(ファイル、クラウド、メッセージアプリなど)でご自身で消してください。受け取った人のスマートフォンにあるファイルは、受け取った人が消す必要があります。',
                '<strong>Google ドライブのバックアップ:</strong> 自動バックアップをオンにした場合は、利用者自身の Google ドライブのアプリ専用領域にあります。上の「Google ドライブのバックアップを消す」で消してください。',
                '<strong>購入の記録:</strong> 作品集PDFの購入履歴は、Google アカウントの Google Play 購入履歴に残ります。Google アカウント › お支払いと定期購入で確認できます。',
            ])]),
            ('消えるデータと保存期間', [('dl', [
                ('子どもの情報・作品の写真・声・答え・ひとこと・親のメモ・設定', '保存場所: 利用者のスマートフォンの中のアプリ用ストレージ。削除の時点: 上の方法で消すとすぐに。'),
                ('「声を文字にする」のリクエスト', '中継サーバーには保存しません。文字にし終わると、何も残りません。'),
                ('Google ドライブ自動バックアップ(オンにした場合)', '保存場所: 利用者自身の Google ドライブのアプリ専用の非表示領域(開発者は見ることができません)。削除の時点: アプリの「ドライブのバックアップを削除」または Google ドライブの「非表示のアプリデータを削除」ですぐに。アプリで消したものは、次のアップロードのときにいっしょに消えます。'),
                ('開発者のサーバーに保管される記録', 'ありません。会員アカウント・独自のデータベース・広告・分析ツールがありません。'),
            ])]),
            ('お困りのときは', [('p', f'上の方法で解決しないときは、件名に「データ削除の問い合わせ」と書いて {MAIL} へお送りください。7日以内にお返事します。開発者が保管している記録はないため、削除の方法をご案内します。')]),
        ],
    ),
)

# ───────────────────────────── index = 가족이 공유 링크로 들어오는 "앱 받기" 페이지(2026-10-19 추가 요청)
PLAY = 'https://play.google.com/store/apps/details?id=com.dearcrayon.app'
_F = '<strong>…dearcrayon.zip</strong>'
INDEX = {
    'ko': dict(
        title='Dear Crayon · 아이의 그림과 말을 모으는 곳',
        ogTitle='Dear Crayon · 가족이 보낸 아이의 이야기',
        desc='아이의 그림과 말을 모으는 곳, Dear Crayon. 앱을 받으면 가족이 보낸 이달의 카드와 도록을 바로 볼 수 있어요.',
        hero='아이의 그림과 말을 모으는 곳, Dear Crayon',
        play='Google Play 에서 받기', playNote='안드로이드 무료 · 아이폰은 준비 중이에요',
        receiveTitle='가족에게 도록을 받았다면',
        receive=[
            '위 버튼으로 <strong>Dear Crayon</strong> 앱을 설치해요.',
            f'카카오톡에서 받은 {_F} 파일을 눌러 <strong>‘Dear Crayon’</strong>으로 열어요.',
            '바로 그 책이 열려요. 앱 첫 화면의 <strong>가족이 보낸 도록 보기</strong>에서도 다시 볼 수 있어요.',
        ],
        aboutTitle='Dear Crayon은',
        about='부모가 아이의 그림을 사진으로 담고, 그 그림에 대해 아이가 한 말을 목소리로 남기는 앱이에요. 매달 같은 질문에 답하며 쌓인 기록은 이달의 카드가 되고, 생일마다 한 권의 도록으로 엮여요. 기록은 휴대폰에, 원하면 내 구글 드라이브에도 저장돼요. 개발자 서버에는 저장하지 않고, 회원 가입도 광고도 없어요.',
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
        about='Dear Crayon lets parents photograph their child’s drawings and keep, in the child’s own voice, what each drawing is about. Answers to the same monthly questions become a monthly card, and each birthday they are gathered into a book. Records stay on the phone — and, if you choose, in your own Google Drive. Nothing is stored on the developer’s servers; no sign-up, no ads.',
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
        about='Mit Dear Crayon fotografieren Eltern die Bilder ihres Kindes und halten mit der Stimme des Kindes fest, was es dazu erzählt. Antworten auf dieselben Monatsfragen werden zur Monatskarte und zu jedem Geburtstag zu einem Buch. Die Einträge bleiben auf dem Handy – und, wenn du willst, in deinem eigenen Google Drive. Nichts wird auf Servern des Entwicklers gespeichert; ohne Registrierung, ohne Werbung.',
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
        about='Une application pour photographier les dessins de votre enfant et garder, avec sa propre voix, ce qu’il raconte sur chacun. Les réponses aux mêmes questions du mois deviennent une carte du mois et, à chaque anniversaire, un livre. Les données restent sur le téléphone — et, si vous le souhaitez, dans votre propre Google Drive. Rien n’est conservé sur les serveurs du développeur ; sans inscription ni publicité.',
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
        about='Una app para fotografiar los dibujos de tu peque y guardar, con su propia voz, lo que cuenta de cada uno. Las respuestas a las mismas preguntas de cada mes se convierten en una tarjeta del mes y, en cada cumpleaños, en un libro. Los registros se quedan en el móvil y, si quieres, en tu propio Google Drive. Nada se guarda en los servidores del desarrollador; sin registro ni anuncios.',
        docsTitle='Documentos',
    ),
    'ja': dict(
        title='Dear Crayon · 子どもの絵とことばを集める場所',
        ogTitle='Dear Crayon · 家族から届いた子どものおはなし',
        desc='子どもの絵とことばを集める場所、Dear Crayon。アプリを入れると、家族から届いた今月のカードや作品集をすぐに見られます。',
        hero='子どもの絵とことばを集める場所、Dear Crayon',
        play='Google Play で手に入れよう', playNote='Android は無料 · iPhone 版は準備中です',
        receiveTitle='家族から作品集が届いたら',
        receive=[
            '上のボタンから <strong>Dear Crayon</strong> アプリをインストールします。',
            f'LINE で受け取った {_F} のファイルをタップして、<strong>「Dear Crayon」</strong>で開きます。',
            'すぐにその本が開きます。アプリの最初の画面の<strong>家族から届いた作品集を見る</strong>からも、また見られます。',
        ],
        aboutTitle='Dear Crayon とは',
        about='親が子どもの絵を写真に残し、その絵について子どもが話したことを声で残すアプリです。毎月おなじ質問に答えてたまった記録は今月のカードになり、誕生日ごとに1冊の作品集にまとまります。記録はスマートフォンに、希望すれば自分の Google ドライブにも保存されます。開発者のサーバーには保存せず、会員登録も広告もありません。',
        docsTitle='ご案内',
    ),
}
for _l, _v in INDEX.items():
    L[_l]['index'].update(_v)
