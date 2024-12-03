# 문제
# 서강대학교 컴퓨터공학과 실습실 R912호에는 현재 N개의 창문이 있고 또 N명의 사람이 있다. 
# 1번째 사람은 1의 배수 번째 창문을 열려 있으면 닫고 닫혀 있으면 연다.  
# 2번째 사람은 2의 배수 번째 창문을 열려 있으면 닫고 닫혀 있으면 연다. 
# 이러한 행동을 N번째 사람까지 진행한 후 열려 있는 창문의 개수를 구하라. 단, 처음에 모든 창문은 닫혀 있다.

# 예를 들어 현재 3개의 창문이 있고 3명의 사람이 있을 때,

# 1번째 사람은 1의 배수인 1,2,3번 창문을 연다. (1, 1, 1)
# 2번째 사람은 2의 배수인 2번 창문을 닫는다. (1, 0, 1)
# 3번째 사람은 3의 배수인 3번 창문을 닫는다. (1, 0, 0)
# 결과적으로 마지막에 열려 있는 창문의 개수는 1개 이다.

# 입력
# 첫 번째 줄에는 창문의 개수와 사람의 수 N(1 ≤ N ≤ 2,100,000,000)이 주어진다.

# 출력
# 마지막에 열려 있는 창문의 개수를 출력한다.
import math
from sys import stdin

input = int(stdin.readline().rstrip())

##### 1번 각 수의 약수의 갯수가 홀수인 수가 몇개인지 구하여 답을 제출함
# 시간초과가 발생하였다.
# open_window = 1

# for x in range(2,input+1):
#     num_divisor = 0 
#     sqrt_x = math.sqrt(x)
#     for j in range(1,math.ceil(sqrt_x)):
#         if x%j == 0 :
#             num_divisor +=1
#     num_divisor *= 2
#     if math.pow(math.floor(sqrt_x),2) == x:
#         num_divisor+=1 
#     if num_divisor%2==1:
#         open_window +=1
        
# print(open_window)

##### 2번 약수의 갯수가 홀수인 수들은 제곱수인것을 파악했다. ex) 1, 4, 9, 16, 25 
# 떄문에 주어진 수의 제곱근을 하고 나머지를 버리면 그것이 열려있는 창문의 갯수이다.

print(math.floor(math.sqrt(input)))