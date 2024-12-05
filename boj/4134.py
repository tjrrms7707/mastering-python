# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	40416	10737	8559	24.983%
# 문제
# 정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

# 출력
# 각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

from sys import stdin
import math

def input():
    return stdin.readline().rstrip()


def search_pn(N):
    if N==0 or N==1:
        return 2
    while(True):
        j = 0 
        for x in range(2,int(math.sqrt(N)+1)):
            if N%x == 0:
                j +=1
                break    
        if j == 1:
            N +=1
            continue
        else:
            break
    return N
            

n = int(input())
n_l = []
for i in range(n):
    n_l.append(int(input()))
    
for i in n_l:
    print(search_pn(i))