from scipy.sparse.csgraph import dijkstra, csgraph_from_dense
xs, ys, xg, yg = map(int, input().split())
N = int(input())
xyr = [(xs, ys, 0)]
xyr.extend([list(map(int, input().split())) for i in range(N)])
xyr.append((xg, yg, 0))
graph = [[0] * (N + 2) for _ in range(N + 2)]

max_val = 10**9

for i in range(N + 2):
    graph[i][i] = max_val

for i in range(N + 2):
    for j in range(i + 1, N + 2):
        x1, y1, r1 = xyr[i]
        x2, y2, r2 = xyr[j]
        d = max(0, ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5 - r1 - r2)
        graph[i][j] = graph[j][i] = d

g = csgraph_from_dense(graph, null_value=max_val)
print(dijkstra(g, indices=0)[-1])
