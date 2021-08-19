class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        pointsSet = set([(x, y) for (x, y) in points])
        points = list(pointsSet)
        numberOfPoints = len(points)
        minimumArea = float('inf')
        for i in range(numberOfPoints):
            for j in range(i + 1, numberOfPoints):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                if x1 != x2 and y1 != y2 and ((x1, y2) in pointsSet) and ((x2, y1) in pointsSet):
                    minimumArea = min(minimumArea, abs(x2 - x1) * abs(y2 - y1))
        return 0 if minimumArea == float('inf') else minimumArea
