from collections import defaultdict
from math import inf


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        byrow = defaultdict(set)  # row: {col,}
        bycol = defaultdict(list)  # col: [row,]
        for x, y in points:
            byrow[y].add(x)
            bycol[x].append(y)

        area = inf
        for x1, ys in list(bycol.items()):
            if len(ys) < 2:
                continue
            for j, y1 in enumerate(ys):
                for y2 in ys[j + 1:]:
                    lens = [abs(x1 - x2) for x2 in byrow[y1] & byrow[y2] - {x1}]
                    if lens:
                        area = min(area, min(lens) * abs(y1 - y2))
        return area if area < inf else 0
