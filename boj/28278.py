# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	1024 MB	42073	15324	12737	36.836%
# 문제
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.


# 입력
# 첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000) 

# 둘째 줄부터 N# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000) append
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다. pop() , -1
# 3: 스택에 들어있는 정수의 개수를 출력한다. len
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다. len 
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다. 개 줄에 명령이 하나씩 주어진다.

# 출력을 요구하는 명령은 하나 이상 주어진다.

# 출력
# 출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

from sys import stdin

def input():
    return stdin.readline().rstrip()

n = int(input())
list = []
def stack_order():
    x = input()
   # 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000) append
    if len(x)>1 :
        a , b = map(int , x.split())
        list.append(b)
    else:
        x = int(x)
        if x == 2: # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
            if len(list) == 0 :
                print(-1)
            else:
                print(list.pop())
        elif x == 3: # 3: 스택에 들어있는 정수의 개수를 출력한다.
            print(len(list))
        elif x == 4: # 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
            if not list :
                print(1)
            else:
                print(0)
        else:# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다. 
            if list : 
                print(list[-1])
            else:
                print(-1)

for i in range(n):
    stack_order()