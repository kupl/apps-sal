class Solution:

    def minAreaRect(self, points):
        (pSet, ans) = (set(map(tuple, points)), float('inf'))
        for (i, (p1x, p1y)) in enumerate(points):
            for (p2x, p2y) in points[i + 1:]:
                area = abs((p2x - p1x) * (p2y - p1y))
                if area > ans or area == 0:
                    continue
                if (p1x, p2y) in pSet and (p2x, p1y) in pSet:
                    ans = area
        return ans if ans < float('inf') else 0
