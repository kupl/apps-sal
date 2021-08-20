from collections import Counter


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [tuple(it) for it in points]
        ds = []
        for (i1, p1) in enumerate(points):
            for p2 in points[i1 + 1:]:
                if p1 == p2:
                    continue
                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                ds.append((dist, (p1, p2)))
        ds.sort()
        ps = [set([it]) for it in points]
        total = 0
        for (cost, (p1, p2)) in ds:
            s1 = [it for it in ps if p1 in it][0]
            s2 = [it for it in ps if p2 in it][0]
            if s1 is s2:
                continue
            total += cost
            s1 |= s2
            ps.remove(s2)
        return total
