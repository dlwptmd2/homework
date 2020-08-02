import requests
from bs4 import BeautifulSoup

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
    a_tag = song.select_one('td.info > a')
    if a_tag is not None:
        # a의 text를 찍어본다.
        title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
        rank = song.select_one('td.number').text[0:2].strip()
        # 어떻게 오직 숫자만 출력할 수 있을까#아 저 [0:2}가 어디부터 어디까지 만 인쇄하라 그런 뜻인가 보네
        artist = song.select_one('td.info > a.artist.ellipsis').text
        #artist= song.select_one('a.artist ellipsis').text 이건 아니야 왤까 그나저나
        #뒤에 붙은 .text는 안에 있는 텍스트를 추출한다는 의미인가?
        #구글 크롬 콘솔 돌려보니 하단에 뜨는거 그대로 쓰면 되네 띄어쓰기 대신에 .요걸로 이어 놨어
        #그래도 모양이 안이뻐 어카지 strip얼른 써볼까



        print(rank, a_tag.text, artist)
          # td 태그 사이의 텍스트를 가져오기








#############################