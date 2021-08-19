from collections import defaultdict
from math import inf


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        byrow = defaultdict(set)  # row: {col,}
        bycol = defaultdict(set)  # col: {row,}
        for x, y in points:
            byrow[y].add(x)
            bycol[x].add(y)

        area = inf
        for x1, ys in list(bycol.items()):
            if len(ys) < 2:
                continue
            for y1 in ys:
                for y2 in ys - {y1}:
                    for x2 in byrow[y1] & byrow[y2] - {x1}:
                        area = min(area, abs(x1 - x2) * abs(y1 - y2))
        return area if area < inf else 0
