from math import sqrt
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

xs, ys, xt, yt = list(map(int, input().split()))
n = int(input())
xyr = [list(map(int, input().split())) for _ in range(n)]

xyr.append([xs, ys, 0])
xyr.append([xt, yt, 0])

row = []
col = []
cost = []

for i, (xi, yi, ri) in enumerate(xyr):
    for j, (xj, yj, rj) in enumerate(xyr[i+1:], i+1):
        row.append(i)
        col.append(j)
        dist = max(0, sqrt((xi - xj) ** 2 + (yi - yj) ** 2) - ri - rj)
        cost.append(dist)

g = csr_matrix((cost, (row, col)), shape=(n + 2, n + 2))
d = dijkstra(g, directed=False, indices=n)
ans = d[n+1]
print(ans)

