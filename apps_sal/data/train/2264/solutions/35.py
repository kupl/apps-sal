import heapq
MOD = 10 ** 9 + 7

N, M = list(map(int, input().split()))
S, T = [int(x) - 1 for x in input().split()]

adjList = [[] for i in range(N)]
for i in range(M):
    U, V, D = list(map(int, input().split()))
    adjList[U - 1].append((V - 1, D))
    adjList[V - 1].append((U - 1, D))

numRouteS = [0 for i in range(N)]
numRouteS[S] = 1

cost = [float('inf')] * N
cost[S] = 0
prev = [None] * N

pq = []
heapq.heappush(pq, (0, S))

vs = []
while pq:
    c, vNow = heapq.heappop(pq)
    if c > cost[vNow]:
        continue
    if c > cost[T]:
        break
    vs += [vNow]

    for v2, wt in adjList[vNow]:
        c2 = cost[vNow] + wt
        if c2 <= cost[v2]:
            if c2 == cost[v2]:
                prev[v2] += [vNow]
                numRouteS[v2] = (numRouteS[v2] + numRouteS[vNow]) % MOD
            else:
                cost[v2] = c2
                prev[v2] = [vNow]
                numRouteS[v2] = numRouteS[vNow]
                heapq.heappush(pq, (c2, v2))

numRouteT = [0] * N
numRouteT[T] = 1
for v in reversed(vs[1:]):
    for v0 in prev[v]:
        numRouteT[v0] = (numRouteT[v0] + numRouteT[v]) % MOD

cST = cost[T]
ans = (numRouteS[T] ** 2) % MOD

for v, c in enumerate(cost):
    if c * 2 == cST:
        x = (numRouteS[v] ** 2) % MOD
        y = (numRouteT[v] ** 2) % MOD
        ans = (ans - x * y) % MOD

for v, c in enumerate(cost):
    if c * 2 < cST:
        for v2, wt in adjList[v]:
            if (cost[v2] * 2 > cST) and c + wt == cost[v2]:
                x = (numRouteS[v] ** 2) % MOD
                y = (numRouteT[v2] ** 2) % MOD
                ans = (ans - x * y) % MOD

print(ans)
