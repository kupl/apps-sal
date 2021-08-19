class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        min_area = math.inf
        for (x1, y1) in points:
            for (x2, y2) in seen:
                if (x1, y2) in seen and (x2, y1) in seen and ((x1, y2) != (x2, y1)):
                    area = abs(x2 - x1) * abs(y2 - y1)
                    if area < min_area:
                        min_area = area
            seen.add((x1, y1))
        return min_area if min_area < math.inf else 0
