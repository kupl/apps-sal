class Solution:

    def calculateCost(self, i, j, points):
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

    def find(self, x, roots):
        if roots[x] != x:
            roots[x] = self.find(roots[x], roots)
        return roots[x]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) < 2:
            return 0
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                weight = self.calculateCost(i, j, points)
                edges.append((weight, i, j))
        edges.sort()
        roots = [i for i in range(n)]
        res = 0
        components = n
        for edge in edges:
            (weight, x, y) = edge
            root_x = self.find(x, roots)
            root_y = self.find(y, roots)
            if root_x != root_y:
                components -= 1
                res += weight
                if components == 1:
                    break
                roots[root_x] = root_y
        return res
