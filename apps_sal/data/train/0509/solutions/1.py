
from collections import deque

n, m = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = list(map(int, input().split()))
    edges[u - 1].append((v - 1, c))
    edges[v - 1].append((u - 1, c))

ret = [-1] * n
q = deque([0])
ret[0] = 1
while q:
    now = q.popleft()
    for nxt, c in edges[now]:
        if ret[nxt] != -1:
            continue
        if ret[now] != c:
            ret[nxt] = c
        else:
            ret[nxt] = 2 if c == 1 else 1
        q.append(nxt)
print(('\n'.join(map(str, ret))))
