class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2):
            (x1, y1) = p1
            (x2, y2) = p2
            return abs(x1 - x2) + abs(y1 - y2)
        s = len(points)
        components = [i for i in range(s)]
        costs = [(manhattan(points[j], points[i]), j, i) for i in range(s) for j in range(s)]
        costs = sorted(costs, key=lambda x: x[0])
        totalCost = 0
        for (c, p1, p2) in costs:
            if p1 != p2:
                if not self.find(p1, p2, components):
                    self.union(p1, p2, components)
                    totalCost += c
        return totalCost

    def root(self, a, roots):
        while roots[a] != a:
            roots[a] = roots[roots[a]]
            a = roots[a]
        return a

    def find(self, a, b, roots):
        return self.root(a, roots) == self.root(b, roots)

    def union(self, a, b, roots):
        ra = self.root(a, roots)
        rb = self.root(b, roots)
        roots[rb] = ra
