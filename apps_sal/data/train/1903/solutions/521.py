class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.size = [1] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def unite(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
                if self.size[px] > self.size[py]:
                    px, py = py, px
                self.size[py] += self.size[px]
                self.parent[px] = py
                return True
        n = len(p)
        total = 0
        dsu = DSU(n)
        edges = []
        for x in range(1, n):
            for y in range(x):
                edges.append((x, y, abs(p[x][0] - p[y][0]) + abs(p[x][1] - p[y][1])))
        edges.sort(key=lambda x: x[2])
        for x, y, cost in edges:
            if dsu.unite(x, y):
                total += cost
        return total
