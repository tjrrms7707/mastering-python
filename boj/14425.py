#문제 내용
'''
 N+M개의 문자열이 주어질때 N개의 문자열은 S의 집합에 속한다.
 그렇다면 나머지 M개의 문자열 중에서 S의 속하는 문자열은 몇개인가?
 
'''


#문제 풀이
'''
N개와 M개의 문자열을 리스트에 저장하고 in 을 통해서 확인하는 방법으로 해보자
리스트로 처리하려 했으니 리스트는 순서가 있기 때문에 비교를 하는 방법에서는 적합하지 않은것 같다.
시간초과로 이어졌고 리스트 대신 세트를 사용하고 한줄씩 입력 받아 입력받은 값이 세트에 포함되어 있는지 확인해보았다.

'''

#코드
import sys

read = sys.stdin.readline()
N , M = map(int , read.split())
s = set([read().strip() for _ in range(N)])
cnt = 0

for _ in range(M):
    t = read()
    if t in s :
       cnt += 1
       
print(cnt) 