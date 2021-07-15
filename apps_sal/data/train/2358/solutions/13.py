from math import dist
from scipy.sparse.csgraph import dijkstra, csgraph_from_dense
from numpy import full, inf
from itertools import combinations

sx, sy, tx, ty, N, *XYR = map(int, open(0).read().split())

A = [(sx, sy, 0), (tx, ty, 0)] + list(zip(*[iter(XYR)] * 3))

D = full((N + 2, N + 2), inf)
for (i, (ax, ay, ad)), (j, (bx, by, bd)) in combinations(enumerate(A), 2):
    D[i][j] = max(
        0,
        dist((ax, ay), (bx, by)) - ad - bd
    )

print(dijkstra(csgraph_from_dense(D, null_value=inf), False, 0)[1])
