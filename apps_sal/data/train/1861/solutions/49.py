from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0
        # x1,y2  x2,y2
        # x1,y1  x2,y1

        xp = defaultdict(set)
        yp = defaultdict(set)
        for x, y in points:
            xp[x].add(y)
            yp[y].add(x)

        a_min = None
        for x1, ys in xp.items():
            if len(ys) < 2:
                continue
            for y1 in ys:
                for y2 in ys:
                    if y1 >= y2:
                        continue
                    for x2 in yp.get(y2, []):
                        if x1 >= x2:
                            continue
                        if y1 in xp[x2]:
                            area = (x2 - x1) * (y2 - y1)
                            if a_min is None:
                                a_min = area
                            else:
                                a_min = min(area, a_min)
        if a_min is None:
            return 0
        return a_min
