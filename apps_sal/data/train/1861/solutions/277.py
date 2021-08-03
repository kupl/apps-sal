class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        # hash set
        points = {(x, y) for x, y in points}
        min_area = float('inf')

        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 or y1 == y2:
                    continue
                x3, y3, x4, y4 = x1, y2, x2, y1

                theoretical_area = abs((x1 - x2) * (y1 - y2))
                if theoretical_area > min_area:
                    # Don't lookup
                    continue

                if (x3, y3) in points and (x4, y4) in points:
                    min_area = min(min_area, abs((x1 - x2) * (y1 - y2)))

        if min_area == float('inf'):
            return 0
        return min_area
