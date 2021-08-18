import sys
import heapq
from collections import defaultdict


def input():
    return sys.stdin.readline()[:-1]


class DijkstraList():
    def __init__(self, adj, start):
        self.list = adj
        self.start = start
        self.size = len(adj)

    def solve(self):
        self.dist = defaultdict(lambda: 10**30)
        self.dist[self.start] = 0
        self.q = []
        self.cnt = 0

        heapq.heappush(self.q, (0, self.start))

        while self.q and self.cnt < self.size:
            u_dist, u = heapq.heappop(self.q)
            if self.dist[u] < u_dist:
                continue
            for v, w in self.list[u]:
                if self.dist[v] > u_dist + w:
                    self.dist[v] = u_dist + w
                    heapq.heappush(self.q, (self.dist[v], v))
            self.cnt += 1
        return

    def distance(self, goal):
        return self.dist[goal]


n, m = map(int, input().split())
cost = [10**30 for _ in range(n)]
edges = defaultdict(list)
for _ in range(m):
    p, q, t = map(int, input().split())
    edges[p - 1 + t * n].append((q - 1 + t * n, 0))
    edges[q - 1 + t * n].append((p - 1 + t * n, 0))
    if len(edges[p - 1 + t * n]) == 1:
        edges[p - 1 + t * n].append((p - 1 + 0 * n, 0))
        edges[p - 1 + 0 * n].append((p - 1 + t * n, 1))
    if len(edges[q - 1 + t * n]) == 1:
        edges[q - 1 + t * n].append((q - 1 + 0 * n, 0))
        edges[q - 1 + 0 * n].append((q - 1 + t * n, 1))

d = DijkstraList(edges, 0)
d.solve()
res = d.distance(n - 1)
if res > 10**20:
    print(-1)
else:
    print(res)
