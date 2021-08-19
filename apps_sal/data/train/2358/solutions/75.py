import sys
input = sys.stdin.readline


def dijkstra(edges, size, src):
    from heapq import heappush, heappop
    INF = 10 ** 18
    dist = [INF] * size
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        (d, v) = heappop(pq)
        if d > dist[v]:
            continue
        for (u, weight) in edges[v]:
            nd = d + weight
            if dist[u] > nd:
                dist[u] = nd
                heappush(pq, (nd, u))
    return dist


(xs, ys, xt, yt) = map(int, input().split())
N = int(input())
xyr = [tuple(map(int, input().split())) for _ in range(N)]
xyr.append((xs, ys, 0))
xyr.append((xt, yt, 0))
edges = [[] for _ in range(N + 2)]
for i in range(N + 1):
    for j in range(i, N + 2):
        (xi, yi, ri) = xyr[i]
        (xj, yj, rj) = xyr[j]
        d = max(0, ((xj - xi) ** 2 + (yj - yi) ** 2) ** 0.5 - (ri + rj))
        edges[i].append((j, d))
        edges[j].append((i, d))
d = dijkstra(edges, N + 2, N)
print(d[N + 1])
