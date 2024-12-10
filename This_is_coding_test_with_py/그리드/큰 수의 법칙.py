from sys import stdin

def input():
    return stdin.readline().rstrip

n , m , k =map(int,input().split())

data = list(map(int,input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

