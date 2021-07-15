
from sys import stdin
from collections import deque
tt = int(stdin.readline())

for loop in range(tt):

    Query = []
    ans = []

    n,m = list(map(int,stdin.readline().split()))
    lis = [ [] for i in range(n) ]
    inum = [0] * n
    ilis = inum
    index = [None] * n

    for i in range(m):

        st,x,y = list(map(int,stdin.readline().split()))
        x -= 1
        y -= 1
        if st == 1:
            ilis[y] += 1
            lis[x].append(y)
            ans.append((x,y))
        else:
            Query.append( (x,y) )

    endnum = 0
    q = deque([])
    for i in range(n):
        if ilis[i] == 0:
            q.append(i)
    while len(q) > 0:
        v = q.popleft()
        index[v] = endnum
        endnum += 1

        for nex in lis[v]:
            inum[nex] -= 1
            if inum[nex] == 0:
                q.append(nex)

    if endnum != n:
        print ("NO")
    else:
        print ("YES")
        for x,y in Query:
            if index[x] < index[y]:
                print(x+1,y+1)
            else:
                print(y+1,x+1)
        for x,y in ans:
            print(x+1,y+1)
        

