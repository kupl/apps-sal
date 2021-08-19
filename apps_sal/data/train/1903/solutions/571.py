class Solution:
    def minCostConnectPoints(self, points):
        def distance(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        points.sort(key=lambda p: p[0] + p[1])
        total_cost = 0
        points = [[p, distance(p, points[0])] for p in points]
        while points:
            minIdx, mindist = None, float('inf')
            for i, (p1, dist) in enumerate(points):
                if dist < mindist:
                    minIdx, mindist = i, dist
            p1, cost = points.pop(minIdx)
            total_cost += cost
            for i, (p2, dist) in enumerate(points):
                points[i][1] = min(points[i][1], distance(p1, p2))
                #newdist = distance(p1, p2)
                # if newdist < dist:
                #    points[i][1] = newdist
        return total_cost
