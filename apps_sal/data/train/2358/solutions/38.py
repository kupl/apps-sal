import heapq
from math import sqrt


def dijkstra(s, n, g):
    INF = 10 ** 18
    d = [INF] * n
    d[s] = 0
    que = []
    heapq.heappush(que, (0, s))
    while que:
        (dist, v) = heapq.heappop(que)
        if d[v] < dist:
            continue
        for (next_v, cost) in g[v]:
            if d[next_v] > d[v] + cost:
                d[next_v] = d[v] + cost
                heapq.heappush(que, (d[next_v], next_v))
    return d


(xs, ys, xg, yg) = map(int, input().split())
xyrl = []
xyrl.append((xs, ys, 0))
xyrl.append((xg, yg, 0))
n = int(input())
for _ in range(n):
    (x, y, r) = map(int, input().split())
    xyrl.append((x, y, r))
g = [[] for _ in range(n + 2)]
for i in range(n + 2):
    for j in range(n + 2):
        if i == j:
            continue
        (x1, y1, r1) = xyrl[i]
        (x2, y2, r2) = xyrl[j]
        d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) - r1 - r2
        if d < 0:
            d = 0
        g[i].append((j, d))
dists = dijkstra(0, n + 2, g)
print(dists[1])
