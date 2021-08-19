from collections import defaultdict as dd
from heapq import heappop, heappush
import math
(xs, ys, xt, yt) = list(map(int, input().split()))
N = int(input())
Cs = [list(map(int, input().split())) for _ in range(N)]
Cs.append([xs, ys, 0])
Cs.append([xt, yt, 0])
Es = dd(dict)
for i in range(N + 2):
    (xi, yi, ri) = Cs[i]
    for j in range(i + 1, N + 2):
        (xj, yj, rj) = Cs[j]
        Es[i][j] = Es[j][i] = max(0, math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2) - ri - rj)
INF = float('inf')
dists = [INF] * (N + 2)
dists[N] = 0
q = []
close = set()
start = N
heappush(q, (0, start))
while q:
    (d, node) = heappop(q)
    if dists[node] < d:
        continue
    close.add(node)
    for (to, c) in list(Es[node].items()):
        if to in close or dists[to] <= d + c:
            continue
        dists[to] = d + c
        heappush(q, (dists[to], to))
print(dists[N + 1])
