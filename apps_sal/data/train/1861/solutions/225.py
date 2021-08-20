from collections import defaultdict
from itertools import combinations


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        mPoints = set(((x, y) for (x, y) in points))
        area = float('inf')
        for ((x1, y1), (x2, y2)) in combinations(points, 2):
            if x1 != x2 and y1 != y2 and ((x1, y2) in mPoints) and ((x2, y1) in mPoints):
                area = min(area, abs(x1 - x2) * abs(y1 - y2))
        return area if area < float('inf') else 0
