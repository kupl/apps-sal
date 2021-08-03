from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

xs, ys, xt, yt = map(int, input().split())
N = int(input())
xyr = [list(map(int, input().split())) for i in range(N)]


def dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


row = [0]
col = [1]
data = [dist(xs, ys, xt, yt)]
for i, (xi, yi, ri) in enumerate(xyr, 2):
    d1 = max(0, dist(xi, yi, xs, ys) - ri)
    d2 = max(0, dist(xi, yi, xt, yt) - ri)
    row.extend([0, 1])
    col.extend([i, i])
    data.extend([d1, d2])
    for j in range(i - 1, N):
        xj, yj, rj = xyr[j]
        dij = max(0, dist(xi, yi, xj, yj) - ri - rj)
        row.append(i)
        col.append(j + 2)
        data.append(dij)

graph = csr_matrix((data, (row, col)), shape=(N + 2, N + 2))
dist = dijkstra(graph, directed=False, indices=0)
print(dist[1])
