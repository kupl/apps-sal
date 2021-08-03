import heapq as hq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s, t = map(int, input().split())
abd = [list(map(int, input().split())) for i in range(m)]
mod = 10**9 + 7
graph = [[] for i in range(n + 1)]
# 隣接リスト
for a, b, d in abd:
    graph[a].append((b, d))
    graph[b].append((a, d))
dists = [[10**18, 0] for i in range(n + 1)]
distt = [[10**18, 0] for i in range(n + 1)]
# S,Tからdijkstra
# distX[i]: [Xからiへの最短経路長、そのパスの本数]
for start, dist in (s, dists), (t, distt):
    dist[start] = [0, 1]
    q = [(0, start)]
    hq.heapify(q)
    while q:
        dx, x = hq.heappop(q)
        k = dist[x][1]
        for y, d in graph[x]:
            if dist[y][0] > dx + d:
                dist[y][0] = dx + d
                dist[y][1] = k
                hq.heappush(q, (dist[y][0], y))
            elif dist[y][0] == dx + d:
                dist[y][1] = (dist[y][1] + k) % mod
dst = dists[t][0]
#dst: S-T間の距離
# anslsに「2人が出会いうる辺/頂点を通るパスの本数」を格納
ans = dists[t][1]**2 % mod
for v in range(1, n + 1):
    if dists[v][0] + distt[v][0] != dst:
        continue
    if dists[v][0] * 2 == distt[v][0] * 2 == dst:
        ans = (ans - (dists[v][1] * distt[v][1])**2) % mod
    else:
        for u, d in graph[v]:
            if dists[u][0] * 2 < dst and distt[v][0] * 2 < dst:
                if dists[u][0] + distt[v][0] + d == dst:
                    ans = (ans - (dists[u][1] * distt[v][1])**2) % mod
#答え: anslsの要素をaiとすると
# (Σai)^2-Σ(ai^2)になるはず…

print(ans % mod)
