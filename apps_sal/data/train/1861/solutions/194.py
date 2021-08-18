class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        points = {(x, y) for x, y in points}
        min_area = float('inf')

        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 or y1 == y2:
                    continue
                if abs((x1 - x2) * (y1 - y2)) > min_area:
                    continue
                if (x1, y2) in points and (x2, y1) in points:
                    min_area = min(min_area, abs((x1 - x2) * (y1 - y2)))

        if min_area == float('inf'):
            return 0
        return min_area
