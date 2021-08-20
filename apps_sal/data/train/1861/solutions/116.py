class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        best = 0
        for p1 in points:
            (x1, y1) = p1
            for p2 in seen:
                (x2, y2) = p2
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    if best == 0:
                        best = area
                    else:
                        best = min(best, area)
            seen.add((x1, y1))
        return best
