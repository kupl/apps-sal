import sys
input = sys.stdin.readline
(N, M) = map(int, input().split())
P = list(map(int, input().split()))
edges = [[] for _ in range(N)]
for _ in range(M):
    (x, y) = map(int, input().split())
    edges[x - 1].append(y - 1)
    edges[y - 1].append(x - 1)
ans = 0
visited = set()
for i in range(N):
    q = [i]
    loop = set()
    values = set()
    while q:
        x = q.pop()
        if x in visited:
            continue
        visited.add(x)
        loop.add(x + 1)
        values.add(P[x])
        for nx in edges[x]:
            if nx not in visited:
                q.append(nx)
    ans += len(loop & values)
print(ans)
