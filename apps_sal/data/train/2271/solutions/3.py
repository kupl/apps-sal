import sys
from collections import deque
readline = sys.stdin.readline
n, m = map(int, readline().split())
P = list(map(lambda x:int(x)-1, readline().split()))
G = [set() for _ in range(n)]
for i in range(m):
    x, y = map(lambda x:int(x)-1, readline().split())
    G[x].add(y)
    G[y].add(x)

D = {}
cnt = 0
V = [-1]*n
for i in range(n):
    if V[i]!=-1: continue
    V[i] = cnt
    que = deque([i])
    D[cnt] = set([P[i]])
    while que:
        nw = que.popleft()
        for nx in G[nw]:
            if V[nx] != -1: continue
            D[cnt].add(P[nx])
            V[nx] = cnt
            que.append(nx)
    cnt += 1
print(sum([int(i in D[V[i]]) for i in range(n)]))
