from heapq import heappop, heappush, heapify
from collections import deque


class Graph():
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.edge = edge
        self.indexed = indexed
        self.graph = [[] for _ in range(n)]
        for e in edge:
            self.graph[e[0] - indexed].append((e[1] - indexed, e[2]))
            self.graph[e[1] - indexed].append((e[0] - indexed, e[2]))

    def dijkstra(self, s, INF=10**18, restore_to=None):
        dist = [INF for _ in range(self.n)]
        dist[s] = 0
        heap = [(0, s)]
        prev = [None for _ in range(self.n)]
        while heap:
            cost, node = heappop(heap)
            if dist[node] < cost:
                continue
            for adj, adjcost in self.graph[node]:
                if dist[node] + adjcost < dist[adj]:
                    dist[adj] = dist[node] + adjcost
                    prev[adj] = node
                    heappush(heap, (dist[adj], adj))
        if restore_to is not None:
            g = restore_to
            if dist[g] == INF:
                return dist, False
            path = [g]
            node = g
            while node != s:
                node = prev[node]
                path.append(node)
            return dist, path[::-1]
        return dist


def dist(p, q):
    px, py = p
    qx, qy = q
    return ((px - qx)**2 + (py - qy)**2)**0.5


xs, ys, xt, yt = map(int, input().split())
s = (xs, ys)
t = (xt, yt)

N = int(input())

barrier = [tuple(map(int, input().split())) for _ in range(N)]
edge = []

edge.append((0, N + 1, dist(s, t)))

for i in range(N):
    xi, yi, ri = barrier[i]
    pi = (xi, yi)
    d = max(dist(s, pi) - ri, 0)
    edge.append((0, i + 1, d))

for i in range(N):
    xi, yi, ri = barrier[i]
    pi = (xi, yi)
    d = max(dist(t, pi) - ri, 0)
    edge.append((N + 1, i + 1, d))

for i in range(N - 1):
    for j in range(i + 1, N):
        xi, yi, ri = barrier[i]
        xj, yj, rj = barrier[j]
        pi = (xi, yi)
        pj = (xj, yj)
        d = max(dist(pi, pj) - ri - rj, 0)
        edge.append((i + 1, j + 1, d))

g = Graph(N + 2, edge, 0)

print(g.dijkstra(0)[N + 1])
