import sys
input = sys.stdin.readline
from collections import deque

n,q=list(map(int,input().split()))
A=deque(list(map(int,input().split())))
Q=[int(input()) for i in range(q)]

ANS=[0]

for l in range(10**5+1):
    x=A.popleft()
    y=A.popleft()

    ANS.append((x,y))

    if x>y:
        A.appendleft(x)
        A.append(y)
    else:
        A.appendleft(y)
        A.append(x)


ANS0=A[0]
B=list(A)[1:]

for q in Q:
    if q<=10**5+1:
        print(*ANS[q])
    else:
        print(ANS0,B[(q-10**5-2)%(n-1)])

