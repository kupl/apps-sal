class Solution:
    def minCostConnectPoints(self, points):
        def distance(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        points.sort(key=lambda p: p[0] + p[1])
        points = [[p, distance(p, points[0])] for i, p in enumerate(points)]
        total_cost = 0
        while points:
            minI, minD = None, float('inf')
            for i, (p1, dist) in enumerate(points):
                if dist < minD:
                    minI, minD = i, dist
            p1, cost = points.pop(minI)
            total_cost += cost
            for i, (p2, _) in enumerate(points):
                points[i][1] = min(points[i][1], distance(p1, p2))
        return total_cost


class Solution:
    def minCostConnectPoints(self, points):
        def distance(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        points.sort(key=lambda p: p[0] + p[1])   # points.sort(key = lambda p: abs(p[0]) + abs(p[1]))
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
                #points[i][1] = min(points[i][1], distance(p1, p2))
                newdist = distance(p1, p2)
                if newdist < dist:
                    points[i][1] = newdist
        return total_cost
