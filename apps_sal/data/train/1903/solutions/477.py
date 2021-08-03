class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        points = sorted(points, key=lambda r: r[0])
        (x1, y1), (x2, y2) = points[:2]
        cost = abs(x2 - x1) + abs(y2 - y1)

        if len(points) == 2:
            return cost

        n = len(points)
        d = []
        for i, (x, y) in enumerate(points[:-1]):
            for j, (xj, yj) in enumerate(points[i + 1:]):
                d.append([i, i + j + 1, abs(xj - x) + abs(yj - y)])
        connections = sorted(d, key=lambda r: r[2])

        parent = [i for i in range(n)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        res, e, k = 0, 0, 0
        while e < n - 1:
            u, v, w = connections[k]
            k += 1
            x, y = find(u - 1), find(v - 1)
            if x != y:
                e += 1
                res += w
                parent[x] = y
        return res
