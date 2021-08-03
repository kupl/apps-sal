from heapq import heappush, heappop, heapify
N, M = map(int, input().split())

E = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    E[u].append((c, v))
    E[v].append((c, u))

used = [0] * N
que = [(c, next, 0) for c, next in E[0]]
used[0] = 1
heapify(que)

ans = [-1] * N
ans[0] = 1

while que:
    cv, v, pre = heappop(que)
    if used[v]:
        continue
    used[v] = 1
    if cv == ans[pre]:
        ans[v] = N - (-(cv + 1) % N)
    else:
        ans[v] = cv
    for cost, next in E[v]:
        if used[next]:
            continue
        heappush(que, (cost, next, v))

print("\n".join([str(i) for i in ans]))
