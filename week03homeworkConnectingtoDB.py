import requests
from bs4 import BeautifulSoup
#########################################################
#프롬 아래에다 파이몽고 디비 기본세팅한다
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

#아 설마 파이몽고를 프로젝트 하나 할때마다 전부 하나씩 깔아주는 건가 새로 깔아야 하네

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.homeworkweek03  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# MongoDB에 insert 하기
#############################################################
# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이ㅜㄹ한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')


#############################
# (입맛에 맞게 코딩)
# select를 이용해서, tr들을 불러오기
songs = soup.select('#body-content > div > div > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for song in songs:
    # movie 안에 a 가 있으면,
    a_tag = song.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        # a의 text를 찍어본다.
        title = a_tag.text.strip()  # a 태그 사이의 텍스트를 가져오기
        rank = song.select_one('td.number').text[0:2].strip()
        # 어떻게 오직 숫자만 출력할 수 있을까#아 저 [0:2}가 어디부터 어디까지 만 인쇄하라 그런 뜻인가 보네
        artist = song.select_one('td.info > a.artist.ellipsis').text
        #artist= song.select_one('a.artist ellipsis').text 이건 아니야 왤까 그나저나
        #뒤에 붙은 .text는 안에 있는 텍스트를 추출한다는 의미인가?
        #구글 크롬 콘솔 돌려보니 하단에 뜨는거 그대로 쓰면 되네 띄어쓰기 대신에 .요걸로 이어 놨어
        #그래도 모양이 안이뻐 어카지 strip얼른 써볼까까 아이미적용된거네 그럼 a_tag요걸 건드리면 되는건가
        #아니지 그걸 건드리는게 아니라 하단부에 타이틀옆에 스트립을 붙여주고 프린트에 타이틀 자체를 넣어주는 거야 오예 성공

###################################################################################################3
#몽고디비에 넣을때 프린트를 굳이 꺼야 하나???
        #print(rank, title, artist)
        doc = {
            'title':title,
            'ranking':rank,
            'artist':artist,
        }
        #아 설마 타이틀, 랭크, 아트스트 사이에 콤마를 안붙여서 인가????
        # ''안에 있는 글자를 바꾸는건 문제가 없겠지? 몽고 디비에 저장되는 이름일테니?
        #맞네 !!!!!! 위랑 위 위에 대한 질문 다 정답은 이응이야 맞아 콤마 붙여야 했고 따옴펴안 글자는 디비 저장 카테고리 네임이야
        db.songs.insert_one(doc)











#############################





















####################################################################################
