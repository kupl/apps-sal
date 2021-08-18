class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        min_area = float('inf')
        seen = set()

        for x0, y0 in points:
            for x1, y1 in seen:
                if (x0, y1) in seen and (x1, y0) in seen:
                    current_area = (abs(y1 - y0)) * (abs(x1 - x0))
                    min_area = min(min_area, current_area)
            seen.add((x0, y0))

        return min_area if min_area != float('inf') else 0
