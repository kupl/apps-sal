import sys

input = sys.stdin.readline
N, M = list(map(int, input().split()))
uvc = [list(map(int, input().split())) for _ in range(M)]

g = [[] for _ in range(N)]
for u, v, c in uvc:
    u -= 1
    v -= 1
    g[u].append((v, c))
    g[v].append((u, c))

children = [[] for _ in range(N)]
appeared = [False] * N
q = [0]
appeared[0] = True
while q:
    u = q.pop()
    for v, c in g[u]:
        if not appeared[v]:
            children[u].append((v, c))
            q.append(v)
            appeared[v] = True

colors = [None] * N
colors[0] = 1
q = [0]
while q:
    u = q.pop()
    c_u = colors[u]
    for v, c_edge in children[u]:
        colors[v] = c_edge + (c_edge == c_u)
        q.append(v)
print(('\n'.join(map(str, colors))))
