import sys
input = sys.stdin.readline
N, M = map(int, input().split())
UVC = [tuple(map(int, input().split())) for i in range(M)]

es = [[] for _ in range(N)]
for u, v, c in UVC:
    u, v = u - 1, v - 1
    es[u].append((v, c))
    es[v].append((u, c))

ans = [-1] * N
ans[0] = 1
stack = [0]
visited = [0] * N
visited[0] = 1
while stack:
    v = stack.pop()
    for to, c in es[v]:
        if visited[to]:
            continue
        visited[to] = 1
        if ans[v] == c:
            ans[to] = c + 1 if c + 1 <= N else 1
        else:
            ans[to] = c
        stack.append(to)

print(*ans, sep='\n')
