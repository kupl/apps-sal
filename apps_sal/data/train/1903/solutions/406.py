class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        parent = list(range(len(points)))
        g = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                g.append((i, j, abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])))
        cost = 0
        for (u, v, w) in sorted(g, key=lambda x: x[2]):
            (ru, rv) = (find(u), find(v))
            if ru == rv:
                continue
            parent[ru] = rv
            cost += w
        return cost
