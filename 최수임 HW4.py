#Numpy
#Numpy는 Numerical Python의 줄임말로 고성능의 과학계산 컴퓨팅과 데이터 분석에 필요한 기본 패키지이다. 제공되는 기능은 다음과 같다.

#빠르고 메모리를 효율적으로 사용하며 벡터 산술연산과 관련된 브로드캐스팅 기능을 제공하는 다차원 배열인 ndarray
#반복문을 작성할 필요 없이 전체 데이터 배열에 대해 빠른 연산을 제공하는 표준 수학 함수
#배열 데이터를 디스크에 쓰거나 읽을 수 있는 도구와 메모리에 올려진 파일을 사용하는 도구
#선형대수, 난수 발생기, 푸리에 변환 기능
#Numpy를 사용하기 위해서는 먼저 numpy 패키지를 import한다.

import numpy as np
#다차원 배열(Arrays)
#Numpy가 제공하는 ndarray(n-dimensional array)은 같은 종류의 데이터를 담을 수 있는 다차원 배열이며, 모든 원소는 같은 자료형이어야 한다. 모든 배열은 각 차원의 크기를 알려주는 shape라는 튜플과 배열에 저장된 자료형을 알려주는 type이라는 객체를 가진다. ndarray의 차원(dimension)은 rank라고 부른다.

# ndarray를 사용해보기 전에 비교를 위해 먼저 리스트를 실펴본다.
a = [1, 2, 3, 4, 5, 6]
print(a)
b = [[1, 2, 3], [4, 5, 6]] # 리스트로 2차원 행렬을 표현했을때의 모양
print(b)
c = [1, 'a', 3.5] # 리스트는 서로 다른 type의 데이터 저장이 가능
print(c)
[1, 2, 3, 4, 5, 6]
[[1, 2, 3], [4, 5, 6]]
[1, 'a', 3.5]
#ndarray는 array 함수와 중첩된 리스트(list)를 이용하여 생성할 수 있으며, []를 이용하여 인덱싱(indexing)을 한다.

a = np.array([1, 2, 3])  # 1차원 배열 생성
print(type(a), a.shape, a[0], a[1], a[2])
a[0] = 5                 # 배열의 한 원소를 변경
print(a)
b = np.array([[1,2,3],[4,5,6]])   # 2차원 배열 생성
print(b) #2차원 배열의 모양을 확인
print(b.shape) #배열의 각 차원의 크기
print(b[0, 0], b[0, 1], b[1, 0]) #인덱싱 예제
(2, 3)
#Numpy는 array 함수 외에도 배열을 생성하기 위한 다양한 방법을 제공한다.

a = np.zeros((2, 3))  # 값이 모두 0인 배열 생성, 매개변수는 원하는 shape
print(a)
b = np.ones((3, 4))   # 값이 모두 1인 배열 생성
c = np.full((2, 4), 7) # 모든 원소가 원하는 값으로 초기화된 배열 생성
d = np.eye(4)        # 2x2의 단위행렬(identity matrix)을 생성
print(d)
e = np.random.random((2,4)) # 무작위값으로 이루어진 배열 생성
print(e)
#배열 인덱싱(Array indexing)
#슬라이싱(Slicing): 파이썬 리스트와 유사하게 배열도 슬라이싱이 가능하다. ndarray는 다차원 배열이므로 각 차원에 대해 슬라이싱을 할 수 있다.

import numpy as np

# shape가 (3, 4)이고 아래와 같은 값을 갖는 2차원 배열을 생성
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# 아래와 같은 일부를 뽑아내고 싶다면?
# [[2 3]
#  [6 7]]
#        0열 1열 2열 3열
# 0행 [[ 1   2   3   4]
# 1행  [ 5   6   7   8]
# 2행  [ 9  10  11  12]]

b = a[:2, 1:3]
print(b)
#주의할 점 : 배열의 슬라이스를 잘라서 만든 배열은 원래의 배열과 값을 공유하므로 수정할 경우 원래의 배열도 값이 변경된다.

print(a[0, 1])
b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
print(b)
print(a)
2
