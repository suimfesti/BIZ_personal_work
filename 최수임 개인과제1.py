print("Q1: 해당 Selector를 문자열로 표시하고, split과 join 함수를 활용하여 다음 예시와 같은 selector를 출력하시오.")
print("예시  '#today_main_news  >  div.hdline_news  >  ul  >  li'")

selector = "#today_main_news > div.hdline_news > ul > li:nth-child(1)" #지정한 CSS Selector

selector = selector.split('>') # ">"로 구분하여 list 생성
del selector[3] # "li:nth-child(1)" 삭제

subselect = selector[-1].split(':') # selector 마지막칸에 있는 내용을 ":"로 구분하여 list 생성
del subselect[1:] # "nth-child(1)" 삭제

selector.extend(subselect) # subselect를 selector 맨뒤에 추가
print(">".join(selector)) #">"를 기준으로 list 문자열 조인


print("Q2: list comprehension을 사용하여 구구단을 연산하는 함수 gugu_com을 작성하고 구구단 7단을 출력하시오.")

def gugu_com(x=7):
    [print(x[0],'*',x[1],'=',x[2]) for x in [ [x, y, x * y] for x in range(7,8,1) for y in range(1, 10, 1) ]]

gugu_com(x=7)


print("Q3: list comprehension을 사용하여, 힌트를 제외하고는 한줄의 코드로 해당 결과를 가지는 이차원 리스트를 만드시오.")

from pprint import pprint #pprint 임포트
pprint([[n*m for n in range(1,7)] for m in range(1,7)])


print("Q4: 이것을 6 x 6 크기의 2차원 리스트로 생성하고, 인덱싱을 통해 2 + 6의 값을 2가지 방법으로 나타내시오.")

from pprint import pprint #pprint 임포트
die_sum = [[i+j for i in range(1,7)] for j in range(1,7)]

pprint(die_sum)
print("2+6 : "+ str(die_sum[1][5])) #첫번째방법
print("2+6 : "+ str(die_sum[5][1])) #두번째방법
