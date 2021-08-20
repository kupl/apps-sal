def getDistance(i, j, points):
    (x1, y1, x2, y2) = (points[i][0], points[i][1], points[j][0], points[j][1])
    return abs(y1 - y2) + abs(x1 - x2)


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        nextPoint = 0
        vis = set([0])
        count = 1
        disMap = {}
        while count < n:
            (minPoint, minLength) = (0, sys.maxsize)
            for i in range(n):
                if i in vis:
                    continue
                l = getDistance(nextPoint, i, points)
                if i not in disMap or l < disMap[i]:
                    disMap[i] = l
                if disMap[i] < minLength:
                    minLength = disMap[i]
                    minPoint = i
            res += minLength
            vis.add(minPoint)
            count += 1
            nextPoint = minPoint
        return res
