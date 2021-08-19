class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = []
        n = len(points)
        for i in range(n):
            for j in range(i):
                p1 = points[i]
                p2 = points[j]
                dist.append((abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), i, j))
        dist.sort()
        ps = list(range(n))

        def find(x):
            while ps[x] != x:
                ps[x] = ps[ps[x]]
                x = ps[x]
            return x

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return False
            else:
                ps[px] = py
                return True
        res = 0
        for (d, x, y) in dist:
            if union(x, y):
                res += d
        return res
