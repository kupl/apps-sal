R,C,N = list(map(int,input().split()))

point = []

def XtoZ(x,y):
    if x==0:
        if y==0:
            return 0
        else:
            return 2*R + 2*C - y
    elif x==R:
        return R + y
    elif y==0:
        return x
    elif y==C:
        return 2*R + C - x

for i in range(N):
    x1,y1,x2,y2 = list(map(int,input().split()))
    if ((x1==0 or x1==R) or (y1==0 or y1==C)) and ((x2==0 or x2==R) or (y2==0 or y2==C)):
        point.append([XtoZ(x1,y1),i])
        point.append([XtoZ(x2,y2),i])

point.sort(key = lambda x:x[0])

flag = [0]*N

from collections import deque

Q = deque()

flag = [True]*N
flag2=False
for p in point:
    if flag[p[1]]:
        Q.append(p[1])
        flag[p[1]] = False
    else:
        if Q.pop()!=p[1]:
            flag2=True
            break

if flag2:
    print("NO")
else:
    print("YES")
