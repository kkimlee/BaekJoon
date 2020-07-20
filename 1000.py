'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

첫째 줄에 A+B를 출력한다.
'''

A, B = input().split() # 문자를 입력받아 공백으로 구분

# 입력받은 문자는 char형으로 저장되므로 덧셈을 위해 int형으로 변환하여 저장
A = int(A)  
B = int(B)

# 두 수의 합 출력
print(A + B)