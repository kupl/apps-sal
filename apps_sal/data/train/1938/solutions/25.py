from typing import List


class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = sorted(set([x for (x1, y1, x2, y2) in rectangles for x in [x1, x2]]))
        xi = {v: i for (i, v) in enumerate(xs)}
        co = [0] * len(xs)
        ar = []
        for (x1, y1, x2, y2) in rectangles:
            ar.append([y1, x1, x2, 1])
            ar.append([y2, x1, x2, -1])
        ar.sort()
        ly = lx = res = 0
        for (y, x1, x2, sig) in ar:
            res += (y - ly) * lx
            ly = y
            for i in range(xi[x1], xi[x2]):
                co[i] += sig
            lx = sum((xs[i + 1] - xs[i] if co[i] else 0 for i in range(len(xs) - 1)))
        return res % (10 ** 9 + 7)
