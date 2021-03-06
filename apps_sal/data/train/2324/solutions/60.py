from heapq import heappush, heappop
N = int(input())
(a, b) = list(zip(*(list(map(int, input().split())) for _ in range(N - 1)))) if N - 1 else ((), ())
G = [{} for _ in range(N + 1)]
for (x, y) in zip(a, b):
    G[x][y] = 1
    G[y][x] = 1
INF = 10 ** 10


def dijkstra(G, s):
    dp = [INF for _ in range(len(G))]
    q = []
    heappush(q, (0, s))
    while q:
        (c, i) = heappop(q)
        if dp[i] == INF:
            dp[i] = c
            for (j, w) in list(G[i].items()):
                heappush(q, (c + w, j))
    return dp


dp1 = dijkstra(G, 1)
dpN = dijkstra(G, N)
ans = 'Fennec' if sum((dp1[i] <= dpN[i] for i in range(1, N + 1))) > N // 2 else 'Snuke'
print(ans)
