# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초 (하단 참고)	512 MB	113648	37195	30084	32.831%
# 문제
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.


# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

from sys import stdin
from collections import deque


def input():
    return stdin.readline().rstrip()

def queue_fuc(list):
    x = input().split()
    if x[0] == 'push':
        list.append(x[1])
    elif x[0] =='pop' :
        if not list :
            print(-1)
        else:
            print(list.popleft())
    elif x[0] =='size':
        print(len(list))
    elif x[0] =='empty':
        if not list:
            print(1)
        else:
            print(0)
    elif x[0] =='front':
        if not list:
            print(-1)
        else:
            print(list[0])
    else:
        if not list:
            print(-1)
        else:
            print(list[-1])      
            
n = int(input())
list = deque()

for i in range(n):
    queue_fuc(list)