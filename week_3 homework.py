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
    a_tag = song.select_one(' tr > td > a')
    if a_tag is not None:
        # a의 text를 찍어본다.

        rank = song.select_one('tr:nth-child(1) > td')['number']  # img 태그의 alt 속성값을 가져오기
        title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
          # td 태그 사이의 텍스트를 가져오기

        print(a_tag.text)






#############################