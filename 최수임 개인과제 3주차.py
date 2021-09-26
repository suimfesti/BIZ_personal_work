#1. urllib
#파이썬은 웹 사이트에 있는 데이터를 추출하기 위해 urllib 라이브러리 사용
#이를 이용해 HTTP 또는 FTP를 사용해 데이터 다운로드 가능
#urllib은 URL을 다루는 모듈을 모아 놓은 패키지
#urllib.request 모듈은 웹 사이트에 있는 데이터에 접근하는 기능 제공, 또한 인증, 리다렉트, 쿠키처럼 인터넷을 이용한 다양한 요청과 처리가 가능

from urllib import request



#1.x. urllib.request를 이용한 다운로드
#라이브러리 읽어들이기 
from urllib import request

url="http://uta.pw/shodou/img/28/214.png"
savename="test.png"

request.urlretrieve(url, savename)
print("저장되었습니다")

#1.2. urlopen으로 파일에 저장하는 방법
#request.urlopen()은 메모리에 데이터를 올린 후 파일에 저장하게 된다.

# URL과 저장경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test1.png"
#다운로드
mem = request.urlopen(url).read()
#파일로 저장하기, wb는 쓰기와 바이너리모드
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다..")

#1.3. API 사용하기
#데이터 읽어들이기
url="http://api.aoikujira.com/ip/ini"
res=request.urlopen(url)
data=res.read()

#바이너리를 문자열로 변환하기
text=data.decode("utf-8")
print(text)


#2. BeautifulSoup
#스크레이핑(Scraping or Crawling)이란 웹 사이트에서 데이터를 추출하고, 원하는 정보를 추출하는 것을 의미
#BeautifulSoup란 파이썬으로 스크레이핑할 때 사용되는 라이브러리로서 HTML/XML에서 정보를 추출할 수 있도록 도와줌. 그러나 다운로드 기능은 없음.
#파이썬 라이브러리는 pip 명령어를 이용해 설치 가능. Python Package Index(PyPI)에 있는 패키지 명령어를 한줄로 설치 가능
#URL (http://pypi.python.org/pypi)


from bs4 import BeautifulSoup
html = """
<html><body>
  <h1>스크레이핑이란?</h1>
  <p>웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

#2.1. 기본 사용
#다음은 Beautifulsoup를 이용하여 웹사이트로부터 HTML을 가져와 문자열로 만들어 이용하는 예제임
#h1 태그를 접근하기 위해 html-body-h1 구조를 사용하여 soup.html.body.h1 이런식으로 이용하게 됨.
#p 태그는 두개가 있어 soup.html.body.p 한 후 next_sibling을 두번 이용하여 다음 p를 추출. 한번만 하면 그 다음 공백이 추출됨.
#HTML 태그가 복잡한 경우 이런 방식으로 계속 진행하기는 적합하지 않음.


#2) HTML 분석하기
soup = BeautifulSoup(html, 'html.parser')

#3) 원하는 부분 추출하기
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

#4) 요소의 글자 출력하기
print(f"h1 = {h1.string}")
print(f"p  = {p1.string}")
print(f"p  = {p2.string}")

#2.2. 요소를 찾는 method
#단일 element 추출: find()
#BeautifulSoup는 루트부터 하나하나 요소를 찾는 방법 말고도 find()라는 메소드를 제공함
soup = BeautifulSoup(html, 'html.parser')
title = soup.find("h1")
body  = soup.find("p")
print(title)
print(f"#title = {title.string}" )
print(f"#body = {body.string}")
#복수 elements 추출: find_all()
html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
print(links, len(links))

for a in links:
    href = a.attrs['href'] # href의 속성에 있는 속성값을 추출
    text = a.string 
    print(text, ">", href)


#3. Css Selector
#앞서 간단하게 태그를 사용하여 데이터를 추출하는 방법에 대해서 살펴보았습니다.하지만 복잡하게 구조화된 웹 사이트에서 자신이 원하는 데이터를 가져오기 위해서는 Css Selector에 대한 이해가 필요합니다.
#BeautifulSoup에서 Css Selector 사용하기
#BeautifulSoup에서는 Css Selector로 값을 가져올 수 있도록 find와는 다른 다음과 같은 메서드를 제공합니다.
html = """
<html><body>
<div id="meigen">
  <h1>위키북스 도서</h1>
  <ul class="items">
    <li>유니티 게임 이펙트 입문</li>
    <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
    <li>모던 웹사이트 디자인의 정석</li>
  </ul>
</div>
</body></html>
"""

# HTML 분석하기 
soup = BeautifulSoup(html, 'html.parser')

# 타이틀 부분 추출하기 --- (※3)
h1 = soup.select_one("div#meigen > h1").string
print(f"h1 = {h1}")

# 목록 부분 추출하기 --- (※4)
li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
  print(f"li = {li.string}")

#4. 활용 예제
#URL을 이용하여 웹으로부터 html을 읽어들임 (urllib)
#html 분석 및 원하는 데이터를 추출 (BeautifulSoup)
from bs4 import BeautifulSoup
from urllib import request, parse

#네이버 금융 - 환율 정보
url = "https://finance.naver.com/marketindex/"
res = request.urlopen(url) #html 가져오기
soup = BeautifulSoup(res, "html.parser") #html 분석하기
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price) #원하는 데이터 추출하기

#기상청 RSS
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

#매개변수를 URL로 인코딩한다.
values = {
    'stnId':'109'
}

params=parse.urlencode(values)
url += "?"+params # URL에 매개변수 추가
print("url=", url)

res = request.urlopen(url) #html 가져오기
soup = BeautifulSoup(res, "html.parser") #분석하기

header = soup.find("header")

title = header.find("title").text
wf = header.find("wf").text

print(title)
print(wf) #원하는 데이터 추출

title = soup.select_one("header > title").text
wf = header.select_one("header wf").text

print(title)
print(wf)

#윤동주 작가의 작품 목록
# 뒤의 인코딩 부분은 "저자:윤동주"라는 의미입니다.
# 따로 입력하지 말고 위키 문헌 홈페이지에 들어간 뒤에 주소를 복사해서 사용하세요.

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = request.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

# #mw-content-text 바로 아래에 있는 
# ul 태그 바로 아래에 있는
# li 태그 아래에 있는
# a 태그를 모두 선택합니다.
a_list = soup.select("#mw-content-text   ul > li  a")
for a in a_list:
    name = a.string
    print(f"- {name}", )
