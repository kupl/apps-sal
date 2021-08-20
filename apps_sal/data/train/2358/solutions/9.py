from math import sqrt
import numpy as np
from scipy.sparse.csgraph import csgraph_from_dense, shortest_path


def distance(x0, y0, x1, y1):
    return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)


(xs, ys, xt, yt, n, *XYR) = map(int, open(0).read().split())
P = [(xs, ys, 0), (xt, yt, 0)] + list(zip(XYR[::3], XYR[1::3], XYR[2::3]))
edges = np.zeros((n + 2, n + 2))
for i in range(n + 1):
    for j in range(i + 1, n + 2):
        dist = distance(P[i][0], P[i][1], P[j][0], P[j][1])
        dist = max(dist - P[i][2] - P[j][2], 0.0)
        edges[i, j] = edges[j, i] = dist
G = csgraph_from_dense(edges, null_value=-1)
print(shortest_path(G, indices=0)[1])
