class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        area = float('inf')

        points_set = {tuple(p) for p in points}

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                (x1, y1) = points[i]
                (x2, y2) = points[j]

                if x1 != x2 and y1 != y2:
                    if (x2, y1) in points_set and (x1, y2) in points_set:
                        area = min(abs(y2 - y1) * abs(x2 - x1), area)

        return area if area < float('inf') else 0
