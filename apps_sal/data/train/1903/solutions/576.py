class DSU:

    def __init__(self, size):
        self.indexes = {i: i for i in range(size)}

    def root(self, i):
        node = i
        while i != self.indexes[i]:
            i = self.indexes[i]
        while node != i:
            nnode = self.indexes[node]
            self.indexes[node] = i
            node = nnode
        return i

    def unite(self, i, j):
        (ri, rj) = (self.root(i), self.root(j))
        if ri == rj:
            return
        self.indexes[rj] = ri


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                (x, y) = (points[i][0], points[i][1])
                (u, v) = (points[j][0], points[j][1])
                edges.append((abs(u - x) + abs(v - y), i, j))
        edges.sort()
        dsu = DSU(len(points))
        ans = 0
        for (dis, u, v) in edges:
            if dsu.root(u) == dsu.root(v):
                continue
            dsu.unite(u, v)
            ans += dis
        return ans
