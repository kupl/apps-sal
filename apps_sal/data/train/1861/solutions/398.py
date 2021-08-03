class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        pmap = {(i, j) for i, j in points}
        area = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                if x1 != x2 and y2 != y1 and x1 != y2 and x2 != y1:
                    if (x1, y2) in pmap and (x2, y1) in pmap:
                        area = min(area, abs(x1 - x2) * abs(y2 - y1))

        return 0 if area == float('inf') else area
