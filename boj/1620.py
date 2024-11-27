#문제 내용
'''
N과 M이 주어지고 N은 사전에 등록된 포켓몬 이름
M은 내가 맞추어야 하는 포켓몬의 이름또는 도감 순서이다.
'''
#문제 풀이
'''
사전을 2개 만든다. key가 번호인것과 이름인것으로
그리고 받은 값이 숫자인지 이름인지 구분하여 사전에서 꺼내어 출력한다.
'''


from sys import stdin

def input():
    return stdin.readline().rstrip()

N , M = map(int,input.split())

by_id = {}
by_name = {}

for i in range(1,N+1):
    pokemon = input()
    by_id[i] = pokemon
    by_name[pokemon] = i
    
for _ in range(M):
    x = input()
    if x.isdigit():
        print(by_id[int(x)])
    else:
        print(by_name[x])
        
        

