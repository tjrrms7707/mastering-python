# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	112710	44604	35577	38.953%
# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, 
# n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. 
# (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

# 입력의 마지막에는 0이 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

# 제한
# 1 ≤ n ≤ 123,456

from sys import stdin
import math

def input():
    return stdin.readline().rstrip()

# def pn(N):  ##소수 검증
#     for i in range(2,int(math.sqrt(N))+1):
#         if N%i == 0:
#             return False
#     return True

# def search_pn(N):
#     x = 0
#     for i in range(N+1,2*N+1):
#         if pn(i):
#             x +=1
#     return x

# while(True):
#     x = int(input())
#     if x ==0:
#         break
#     print(search_pn(x))

###PyPy3로 성공 


check = [0,0] + [1]*246912

for i in range(2,246913):
    if check[i]:
        for j in range(i*2,246913,i):
            check[j] = 0
            
while True:
    x = int(input())
    if x==0:
        break
    print(sum(check[x+1:x*2+1]))