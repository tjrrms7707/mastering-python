# 문제
# 문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

# 부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

# 예를 들어, 
# ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 
# 서로 다른것의 개수는 12개이다.

# 입력
# 첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.

# 출력
# 첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.


#문제 풀이
#예를 들어 길이가 5인 문자열
# 갯수가 1개는 5(idx -> 0 1 2 3 4)
# 갯수가 2개는 4(idx -> 01 12 23 34)
# 갯수가 3개는 3(idx -> 012 123 234)
# 갯수가 4개는 2(idx -> 0123 1234)
# 갯수가 5개는 1(idx -> 01234)  
# 

from sys import stdin

def input():
    return stdin.readline().rstrip()


read = input()

s = list(read)

s_set =set()


#n번 순해
for i in range(1,len(s)+1):
    #i는 idx 범위가 된다.
    for x in range(len(s)+1-i):
        s_set.add(read[x:x+i])


print(len(s_set))