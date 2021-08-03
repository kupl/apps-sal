class Solution:
    def minCostConnectPoints(self, points):
        def helper(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        points, res = [[p, helper(p, points[0])] for p in points], 0
        while points:
            minI = min(range(len(points)), key=lambda i: points[i][1])
            p1, cost = points.pop(minI)
            res += cost
            for i, (p2, _) in enumerate(points):
                points[i][1] = min(points[i][1], helper(p1, p2))
        return res
