#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Graph:
    def __init__(self, nvert, edges):
        self.adj = [[False] * nvert for i in range(nvert)]
        for e in edges:
            u, v = e
            self.adj[u][v] = True
            self.adj[v][u] = True

    def __str__(self):
        return str(self.adj)

    # 節点数
    def nvertices(self):
        return len(self.adj)

    # 補グラフ
    def complement(self):
        nv = len(self.adj)
        g = Graph(nv, [])
        for u in range(nv):
            for v in range(nv):
                if u == v:
                    continue
                g.adj[u][v] = not self.adj[u][v]
                g.adj[v][u] = not self.adj[v][u]
        return g

    # 連結成分であるグラフのリスト
    def connectedcomps(self):
        self.visited = [False] * self.nvertices()
        ccs = []
        for v in range(self.nvertices()):
            if not self.visited[v]:
                vs = []
                self.__connectedcomp(v, vs)
                cc = self.inducedsubgraph(vs)
                ccs.append(cc)
        self.visited = None
        return ccs

    # vを含む連結成分 (節点のリスト)
    def __connectedcomp(self, v, vs):
        if self.visited[v]:
            return
        self.visited[v] = True
        vs.append(v)
        for u in range(self.nvertices()):
            if self.adj[v][u]:
                self.__connectedcomp(u, vs)

    # 誘導部分グラフ
    def inducedsubgraph(self, vs):
        n = len(vs)
        # [3, 1, 4] -> {3:0, 1:1, 4:2}
        m = {}
        for i in range(n):
            m[vs[i]] = i

        sg = Graph(n, [])
        for v in vs:
            for u in range(self.nvertices()):
                if self.adj[v][u]:
                    sg.adj[m[v]][m[u]] = True
                    sg.adj[m[u]][m[v]] = True
        return sg

    # 2部グラフならば2グループの各節点数の組。2部グラフでなければFalse
    # 組を返すときは(大,小)の順
    def isbipartite(self):
        self.color = [None] * self.nvertices()
        self.color[0] = 0
        if not self.__isbipartite(0):
            return False
        m = sum(1 for c in self.color if c == 0)
        n = sum(1 for c in self.color if c == 1)
        assert m + n == self.nvertices()
        return (max(m, n), min(m, n))

    def __isbipartite(self, v):
        for u in range(self.nvertices()):
            if self.adj[v][u]:
                if self.color[u] == None:
                    self.color[u] = 1 - self.color[v]
                    if not self.__isbipartite(u):
                        return False
                elif self.color[u] != 1 - self.color[v]:
                    return False
        return True


# 入力
N, M = [int(w) for w in input().split()]
edges = []
for i in range(M):
    a, b = [int(w) for w in input().split()]
    edges.append((a - 1, b - 1))

# 入力されたグラフの補グラフ g が2部グラフ
g = Graph(N, edges).complement()
ccs = g.connectedcomps()
bs = [cc.isbipartite() for cc in ccs]
if not all(bs):
    print(-1)
    return

# (連結成分が複数ある場合),
# 2グループの節点数の差が最小となるような分け方を求める
diffs = [t[0] - t[1] for t in bs]
sums = {0}
for d in diffs:
    newsums = set()
    for s in sums:
        newsums.add(s + d)
    sums.update(newsums)

halfdiff = sum(diffs) / 2
nearlyhalfdiff = min((abs(s - halfdiff), s) for s in sums)[1]

# 節点数の差を最小にすると，その差はdiffになる
diff = abs(sum(diffs) - 2 * nearlyhalfdiff)

# グループの節点数 (x, y)
x = (N - diff) // 2
y = N - x

# 完全グラフの辺数
x = x * (x - 1) // 2
y = y * (y - 1) // 2

print(x + y)
