import math
import itertools
import collections


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        x_index = defaultdict(set)
        y_index = defaultdict(set)
        for (x, y) in points:
            x_index[x].add(y)
            y_index[y].add(x)
        rects = []
        for (p1, p2) in itertools.combinations(points, 2):
            (x1, y1) = p1
            (x2, y2) = p2
            if x1 == x2 or y1 == y2:
                continue
            if y1 in x_index[x2] and x1 in y_index[y2]:
                rects.append([p1, p2])
        if len(rects) == 0:
            return 0
        ret = math.inf
        for ((x1, y1), (x2, y2)) in rects:
            area = abs((x1 - x2) * (y1 - y2))
            if area < ret:
                ret = area
        return ret
