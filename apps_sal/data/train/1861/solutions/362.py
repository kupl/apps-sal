class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        minA = float('inf')
        cache = {(x, y) for (x, y) in points}
        for i in range(len(points)):
            (x1, y1) = points[i]
            for j in range(i + 1, len(points)):
                (x2, y2) = points[j]
                if (x1, y2) in cache and (x2, y1) in cache:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area != 0:
                        minA = min(minA, area)
        return minA if minA < float('inf') else 0
