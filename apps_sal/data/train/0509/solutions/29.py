from collections import deque
(N, M) = list(map(int, input().split()))
G = [{} for i in range(N)]
for _ in range(M):
    (u, v, c) = list(map(int, input().split()))
    G[u - 1][v - 1] = c - 1
    G[v - 1][u - 1] = c - 1
ans = [-1 for i in range(N)]
ans[0] = 0
q = deque([0])
while q:
    r = q.pop()
    for p in G[r]:
        if ans[p] != -1:
            continue
        if ans[r] == G[p][r]:
            ans[p] = (ans[r] + 1) % N
        else:
            ans[p] = G[p][r]
        q.append(p)
for i in ans:
    print(i + 1)
