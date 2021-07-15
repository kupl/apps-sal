import sys
from collections import deque
for case in range(int(input())):
    n, m = map(int, sys.stdin.readline().split()) #fast io
    g = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = map(int, sys.stdin.readline().split())
        g[x].append(y)
        g[y].append(x)
    col = [-1] * (n + 1)
    col[1] = 1
    Q = deque() #calling deque data structure from collections
    Q.append(1)
    ans = [[] for i in range(2)]
    ans[1].append(1)
    while Q:
        From = Q.popleft()
        for To in g[From]:
            if(col[To] == -1):
                if col[From] == 1:
                    col[To] = 2
                else:
                    col[To] = 1
                ans[col[To] % 2].append(To)
                Q.append(To)

    if len(ans[0]) < len(ans[1]):
        print(len(ans[0]))
        print(*ans[0])
    else:
        print(len(ans[1]))
        print(*ans[1])
