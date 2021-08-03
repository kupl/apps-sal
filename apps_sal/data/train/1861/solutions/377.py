class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pointsSet = set(tuple(point) for point in points)
        minarea = sys.maxsize
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x_i = points[i][0]
                y_i = points[i][1]
                x_j = points[j][0]
                y_j = points[j][1]
                if x_i != x_j and y_i != y_j and (x_i, y_j) in pointsSet and (x_j, y_i) in pointsSet:
                    minarea = min(minarea, abs(x_j - x_i) * abs(y_j - y_i))
        return minarea if minarea != sys.maxsize else 0
