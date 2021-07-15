class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda a, b, x, y: abs(a-x)+abs(b-y)
        points = sorted(points, key=lambda x: abs(x[0])+abs(x[1]))
        connected = [points[0]]
        cost = 0
        points = list([[x[0], x[1], manhattan(connected[0][0], connected[0][1], x[0], x[1])] for x in points])
        # print(points)
        while len(connected) <= len(points):
            minidx = None
            mindist = float('inf')
            for i in range(len(points)):
                x, y, dist = points[i]
                if dist < mindist:
                    mindist = dist
                    minidx = i
            mx, my, mdist = points.pop(minidx)
            cost += mdist
            for i in range(len(points)):
                x, y, dist = points[i]
                newdist = manhattan(x, y, mx, my)
                if newdist < dist:
                    points[i][2] = newdist
            # print(points, mindist, \"=\", mx,my)
        return cost

