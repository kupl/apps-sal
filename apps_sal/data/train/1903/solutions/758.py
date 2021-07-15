class Solution:
    def minCostConnectPoints(self, points):
        helper = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        points = [[p, helper(p, points[0])] for p in points]
        total_cost = 0
        while points:
            minI = min(range(len(points)), key = lambda i: points[i][1])
            p1, cost = points.pop(minI)
            total_cost += cost
            for i, (p2, _) in enumerate(points):
                points[i][1] = min(points[i][1], helper(p1, p2))
        return total_cost
