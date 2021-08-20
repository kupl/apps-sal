class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
        ptSet = set([(x, y) for (x, y) in points])
        area = math.inf
        for i in range(n):
            for j in range(i):
                if points[i][0] != points[j][0] and points[i][1] != points[j][1]:
                    if (points[i][0], points[j][1]) in ptSet and (points[j][0], points[i][1]) in ptSet:
                        area = min(area, abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[j][1]))
        return area if area < math.inf else 0
