
'''
문제) K번째 약수 찾기

어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 
나머지가 0이면 q는 p의 약수이다. 

6을 예로 들면

	6 ÷ 1 = 6 … 0
	6 ÷ 2 = 3 … 0
	6 ÷ 3 = 2 … 0
	6 ÷ 4 = 1 … 2
	6 ÷ 5 = 1 … 1
	6 ÷ 6 = 1 … 0

그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 
작성하시오.

▣ 입력설명
첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N 
이하이다.

▣ 출력설명
첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 
K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.

▣ 입력예제 1 
6 3

▣ 출력예제 1
3
'''

import sys

# 실행시 파일을 읽어옴
# sys.stdin = open("input.txt", "rt")

# 입력받은 값을 변수와 매핑함.
# 두 개의 숫자를 int형으로 받음
# 띄어씌기를 이용해 데이터가 분리되어 있기 때문에 split() 
n, k = map(int, input().split())

# k 번째 약수를 찾기 위한 변수
cnt = 0

# 1부터 n 까지 숫자를 i에 대입
for i in range(1, n+1):
	# n / i 의 나머지가 0인 경우 
	# i는 n의 약수이므로 cnt 증가
	if n%i == 0:
		cnt += 1
	# cnt 가 k인 경우 i는 n의 k번째 약수임
	# 따라서 i 출력
	# break를 통해 반복문 탈출
	if cnt == k:
		print(i)
		break
# for ~ else 구문
# for문이 정상적으로 종료된 경우 동작함
# break를 통해 도중에 탈출한 경우 동작하지 않음
else:
	print(-1)