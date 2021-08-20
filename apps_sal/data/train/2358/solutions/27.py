from scipy.sparse.csgraph import csgraph_from_dense, dijkstra
(xs, ys, xt, yt) = map(int, input().split())
N = int(input())
xyr = [tuple(map(int, input().split())) for _ in range(N)]
xyr.append((xs, ys, 0))
xyr.append((xt, yt, 0))
b = [[-1] * (N + 2) for _ in range(N + 2)]
for i in range(N + 2):
    (x1, y1, r1) = xyr[i]
    for j in range(i + 1, N + 2):
        (x2, y2, r2) = xyr[j]
        r = max(0, ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 - (r1 + r2))
        b[i][j] = r
        b[j][i] = r
Graph = csgraph_from_dense(b, null_value=-1)
start = N
end = N + 1
print(dijkstra(Graph, indices=start)[end])
