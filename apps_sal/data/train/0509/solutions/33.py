import sys
from collections import deque


N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    u, v, c = map(int, sys.stdin.readline().split())
    u -= 1; v -= 1
    edge[u].append((v, c))
    edge[v].append((u, c))
path = [-1] * N
path[0] = edge[0][0][1]
q = deque()
for v, c in edge[0]:
    q.append((0, v, c))

while q:
    u, v, c = q.popleft()
    if path[v] == -1:
        if path[u] != c:
            vc = c
        else:
            if path[u] > 1:
                vc = path[u] - 1
            else:
                vc = path[u] + 1
        path[v] = vc
        for nv, nc in edge[v]:
            if path[nv] == -1:
                q.append((v, nv, nc))

print(*path, sep='\n')

