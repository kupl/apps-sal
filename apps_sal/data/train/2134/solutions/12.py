from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([0])
    a[0] = s[0]
    visited = [False] * n
    visited[0] = True
    while q:
        v = q.popleft()
        for nv in G[v]:
            if visited[nv]:
                continue
            visited[nv] = True
            if s[nv] == -1:
                l = []
                for nnv in G[nv]:
                    if v == nnv:
                        continue
                    l.append(s[nnv])
                if len(l) == 0:
                    s[nv] = s[v]
                else:
                    s[nv] = min(l)
                a[nv] = s[nv] - s[v]
                q.append(nv)
            else:
                a[nv] = s[nv] - s[v]
                q.append(nv)


n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
G = [[] for _ in range(n)]
for i in range(n - 1):
    G[i + 1].append(p[i] - 1)
    G[p[i] - 1].append(i + 1)
a = [0] * n
bfs()
if min(a) >= 0:
    print(sum(a))
else:
    print(-1)
