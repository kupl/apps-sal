class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        es = []
        n = len(points)
        for i, p in enumerate(points):
            x, y = p
            for j in range(i + 1, n):
                pb = points[j]
                x2, y2 = pb
                val = abs(x - x2) + abs(y - y2)
                es.append((val, i, j))
        es.sort()
        self.father = {i: i for i in range(n)}
        ans = size = 0
        for cost, u, v in es:
            if self.find(u) != self.find(v):
                ans += cost
                self.union(u, v)
                size += 1
            if size == n - 1:
                break
        return ans

    def find(self, a):
        path = []
        nd = a
        fa = self.father
        while fa[nd] != nd:
            path.append(nd)
            nd = fa[nd]
        root = nd
        for nd in path:
            fa[nd] = root
        return root

    def union(self, a, b):
        fa = self.father
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            fa[ra] = rb
