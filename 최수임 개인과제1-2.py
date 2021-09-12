##1.람다함수 실습
#1.1기존함수
def f(x,y):
    return x + y
print(f(1,4))


#1.2 람다함수할당
f=lambda x,y: x + y
print(f(1,4))

#1.3 익명의 람다함수
print((lambda x, y:x+y)(1,4))

#2.맵리듀스
#2.1map함수
ex = [1,2,3,4,5]
f = lambda x:x**2
print(list(map(f, ex)))


ex=[1,2,3,4,5] #list 없는 람다,맵함수
f=lambda x:x**2
for value in map(f,ex):
    print(value)

ex = [1, 2, 3, 4, 5] #리스트 컴프리헨션 용법
[x**2 for x in ex]

ex=[1,2,3,4,5]
f=lambda x,y:x+y
list(map(f,ex,ex))

[x+y for x,y in zip(ex,ex)] #리스트 컴프리헨션 용법

#2.2reduce함수
from functools import reduce
print(reduce(lambda x,y:x+y, [1,2,3,4,5]))

x=0
for y in [1,2,3,4,5]:
    x += y
print(x)

#3.별표의활용
#3.1가변인수로 활용

def asterisk_test(a, *args):
    print(a,args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)

def asterisk_test(a,**kargs):
    print(a,kargs)
    print(type(kargs))
asterisk_test(1,b=2,c=3,d=4,e=5,f=6)

#3.2.별표의 언패킹 기능
def asterisk_test(a,args):
    print(a,*args)
    print(type(args))
asterisk_test(1,(2,3,4,5,6))

def asterisk_test(a,args):
    print(a,args)
    print(type(args))
asterisk_test(1,(2,3,4,5,6))

a,b,c=([1,2], [3,4], [5,6])
print(a,b,c)
data=([1,2], [3,4], [5,6])
print(*data)

for data in zip(*[[1,2],[3,4],[5,6]]):
    print(data)
    print(type(data))

def asterisk_test(a,b,c,d):
    print(a,b,c,d)
data={"b":1, "c":2, "d":3}
asterisk_test(10, **data)


#4.선형대수학
#4.1. 파이썬 스타일 코드로 표현한 벡터
vector_a=[1,2,10]  # 리스트로 표현한 경우
vector_b=(1,2,10)   # 튜플로 표현한 경우
vector_c={'x':1, 'y':2, 'z':10}  # 딕셔너리로 표현한 경우

u=[2,2]
v=[2,3]
z=[3,5]
result=[]
for i in range(len(u)):
    result.append(u[i]+v[i]+z[i])
print(result)

u=[2,2]
v=[2,3]
z=[3,5]
result=[sum(t) for t in zip(u,v,z)]
print(result)

def vector_addition(*args):
    return [sum(t) for t in zip(*args)]   # unpacking 통해 zip(u,v,z) 효과를 낼 수 있음.
vector_addition(u,v,z)

a = [1, 1]
b = [2, 2]
[x + y for x, y in zip(a, b)]


u=[1,2,3]
v=[4,4,4]
alpha=2
result=[alpha*sum(t) for t in zip(u,v)]
result



#4.2. 파이썬 스타일코드로 표현한 행렬
matrix_a=[[3,6], [4,5]] #리스트로 표현한 경우
matrix_b=[(3,6), (4,5)] #튜플로 표현한 경우
matrix_c={(0,0):3, (0,1):6, (1,0):4, (1,1):5}  #디셔너리로 표현한경우

matrix_a=[[3,6], [4,5]]
matrix_b=[[5,8], [6,7]]
result=[[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)



#주민등록번호로 성별 찾기 with map
#PR6에서 split을 활용하여 주민등록번호 뒷자리의 맨 첫 번째 숫자를 추출하여 성별을 알아내는 과정을 구현하였다.
#이번에는 여러개의 요소를 가지는 다음과 같은 리스트에서 성별을 찾는 과정을 맵리듀스를 이용해 간단하게 구현해보자.
pins = ["891120-1234567", "931120-2335567", "911120-1234234", "951120-1234567"]

#Q: lambda와 map을 사용하여 위의 리스트에서 출력결과 예시와 같이 성별을 나타내는 값을 추출하시오.
pins_lam= lambda x:x[7]
print(list(map(pins_lam,pins)))

















