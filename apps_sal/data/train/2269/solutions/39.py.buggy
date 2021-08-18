import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [set() for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].add(B)
    G[B].add(A)

G_comp = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j and j not in G[i]:
            G_comp[i].append(j)

color = [-1] * N
A = []
dp = set([0])
for i in range(N):
    if color[i] != -1:
        continue
    cnt = [1, 0]
    color[i] = 0
    stack = [i]
    while stack:
        v = stack.pop()
        for u in G_comp[v]:
            if color[u] == -1:
                color[u] = 1 - color[v]
                stack.append(u)
                cnt[color[u]] += 1
            if color[u] == color[v]:
                print(-1)
                return
    ndp = set()
    for a in dp:
        ndp.add(a + cnt[0])
        ndp.add(a + cnt[1])
    dp = ndp
ans = float('inf')
for a in dp:
    ans = min(ans, a * (a - 1) // 2 + (N - a) * (N - a - 1) // 2)
print(ans)
