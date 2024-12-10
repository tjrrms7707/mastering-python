from sys import stdin

def input():
    return stdin.readline().rstrip()

n  = int(input())
stack_origin =list(map(int,input().split()))
stack_temp = []


for i in range(1,n+1):
    while True:
        if stack_origin: #원래줄에 사람 있음
            if stack_origin[0] ==i:
                stack_origin.pop(0)
                break
            elif stack_temp: 
                if stack_temp[-1]==i:
                    stack_temp.pop()
                    break
                else:
                    stack_temp.append(stack_origin.pop(0))
            else:
                stack_temp.append(stack_origin.pop(0))
        else:
            if stack_temp[-1] == i :
                stack_temp.pop()
                break
            else:
                break

if not stack_temp and not stack_origin:
    print('Nice')
else:
    print('Sad')