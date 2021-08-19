import math
from collections import defaultdict


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        horizontal_lines = defaultdict(set)
        vertical_lines = defaultdict(set)
        for (x, y) in points:
            vertical_lines[x].add(y)
            horizontal_lines[y].add(x)
        min_area = math.inf
        for (x, y) in points:
            for next_y in vertical_lines[x]:
                if next_y > y:
                    for intersect_x in horizontal_lines[y] & horizontal_lines[next_y]:
                        if intersect_x < x:
                            min_area = min((x - intersect_x) * (next_y - y), min_area)
        if min_area == math.inf:
            return 0
        else:
            return min_area
