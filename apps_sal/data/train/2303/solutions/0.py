#!/usr/bin/env python3
import sys
input = sys.stdin.readline
from collections import deque
INF = 10**9

n, m = map(int, input().split())
pqc = []

seen = set()
for i in range(n):
    seen.add((i, 0))
for _ in range(m):
    p, q, c = map(int, input().split())
    p -= 1; q -= 1
    pqc.append((p, q, c))
    seen.add((p, c))
    seen.add((q, c))
comp = dict()
for i, node in enumerate(seen):
    comp[node] = i

edge = [[] for _ in range(len(comp))]
for key in comp.keys():
    v, c = key
    if c != 0:
        frm = comp[(v, c)]
        too = comp[(v, 0)]
        edge[frm].append((too, 0))
        edge[too].append((frm, 1))

for p, q, c in pqc:
    frm = comp[(p, c)]
    too = comp[(q, c)]
    edge[frm].append((too, 0))
    edge[too].append((frm, 0))

class BFS:
    def __init__(self, adj):
        self.adj = adj
        self.dist = [INF] * len(adj)
        self.q = deque()

    def calc(self, start):
        self.dist[start] = 0
        self.q.append((0, start))
        while len(self.q) != 0:
            prov_cost, src = self.q.popleft()
            if self.dist[src] < prov_cost:
                continue
            for dest, cost in self.adj[src]:
                if self.dist[dest] > self.dist[src] + cost:
                    self.dist[dest] = self.dist[src] + cost
                    if cost == 1:
                        self.q.append((self.dist[dest], dest))
                    else:
                        self.q.appendleft((self.dist[dest], dest))
        return self.dist

bfs = BFS(edge)
bfs.calc(comp[(0, 0)])
ans = bfs.dist[comp[(n-1, 0)]]
if ans == INF:
    print(-1)
else:
    print(ans)
