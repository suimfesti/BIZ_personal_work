#일반문제
from bs4 import BeautifulSoup
from urllib import request

#Q.네이버 뉴스 헤드라인의 제목을 추출해보자. 다음의 코드에 css selector를 추가하여 최신 기사의 헤드라인을 스크레이핑하는 코드를 완성하시오.
#크롤링할 url 주소
url = "https://news.naver.com/"

#requests 패키지 함수를 사용해서 문서를 가져온다.
#bs4패키지의 함수로 html 문서를 파싱한다.
res = request.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

selector = "#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a"
headline = soup.select(selector)


for title in headline:
    print(title.get_text(strip=True))


#시민의 소리 게시판
#Q. 다음의 코드에 css selector를 추가하여 해당 페이지에서 게시글의 제목을 스크레이핑하는 코드를 완성하시오. 또한 과제 제출시 하단의 추가 내용을 참고하여 수집한 데이터를 csv 형태로 저장하여 해당 csv 파일도 함께 제출하시오.
url_head = "https://www.sisul.or.kr"
url_board = url_head + "/open_content/childrenpark/qna/qnaMsgList.do?pgno=1"

res = request.urlopen(url_board)
soup = BeautifulSoup(res, "html.parser")

# selector = "#detail_con > div.generalboard > table > tbody > tr > td.left.title > a"
selector = "#detail_con > div.generalboard > table > tbody > tr > td.left.title > a"
titles = []
links = []
for a in soup.select(selector):
    titles.append(a.text)
    links.append(url_head + a.attrs["href"])
    
print(titles, links)

import pandas as pd


board_df = pd.DataFrame({"title": titles, "link": links})
board_df.head()
board_df.to_csv("board.csv", index=False)
