from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        past_points = set()
        for x1, y1 in points:
            for x2, y2 in past_points:
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in past_points and (x2, y1) in past_points:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        res = min(res, area)
            past_points.add((x1, y1))
        return res if res != float('inf') else 0
