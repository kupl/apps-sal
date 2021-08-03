from bisect import bisect_left
from collections import defaultdict as dd
N = int(input())
As = list(map(int, input().split()))
Es = dd(dict)
for _ in range(N - 1):
    f, t = list(map(int, input().split()))
    Es[f - 1][t - 1] = Es[t - 1][f - 1] = 1

INF = float('inf')
RET = 0
PROC = 1

stack = []
lismin = [INF] * N
anss = [INF] * N
visited = [False] * N

stack.append((RET, 0, INF))
stack.append((PROC, 0, 0))
while stack:
    cmd, *v = stack.pop()
    if cmd == RET:
        i, backup = v
        lismin[i] = backup
    else:
        node, i = v
        lismin[i] = As[node]
        anss[node] = bisect_left(lismin, INF)
        visited[node] = True
        for to in list(Es[node].keys()):
            if not visited[to]:
                x = bisect_left(lismin, As[to])
                stack.append((RET, x, lismin[x]))
                stack.append((PROC, to, x))
for ans in anss:
    print(ans)
