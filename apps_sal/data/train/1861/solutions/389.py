

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = {(point[0], point[1]) for point in points}
        minArea = math.inf
        for i, point1 in enumerate(points):
            for j in range(i):
                point2 = points[j]
                x1, x2, y1, y2 = point1[0], point2[0], point1[1], point2[1]
                diagPoints = (x1 != x2) and (y1 != y2)
                if diagPoints and (x1, y2) in S and (x2, y1) in S:
                    minArea = min(minArea, abs(x1 - x2) * abs(y1 - y2))
        return minArea if minArea != math.inf else 0
