class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        ds = [float('inf')] * n

        for i in range(1, n):
            ds[i] = dist(0, i)

        res = 0
        for i in range(1, n):
            cost = min(ds)
            res += cost
            j = ds.index(cost)
            ds[j] = float('inf')
            for k in range(n):
                if ds[k] == float('inf'):
                    continue
                ds[k] = min(ds[k], dist(j, k))
        return res
