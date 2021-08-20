from collections import defaultdict


class Solution:

    def minAreaRect(self, points):
        (setr, setc) = (set(), set())
        for (r, c) in points:
            setr.add(r)
            setc.add(c)
        if len(points) in (len(setr), len(setc)):
            return 0
        columns = defaultdict(list)
        for (r, c) in points:
            columns[r].append(c)
        (ans, lastc) = (float('inf'), dict())
        for r in sorted(columns):
            cols = sorted(columns[r])
            for (j, y2) in enumerate(cols):
                for (i, y1) in enumerate(cols[:j]):
                    if (y1, y2) in lastc:
                        ans = min(ans, (r - lastc[y1, y2]) * (y2 - y1))
                    lastc[y1, y2] = r
        return ans if ans < float('inf') else 0


class Solution:

    def minAreaRect(self, points):
        X = list(zip(*points))
        if len(points) in (len(set(X[0])), len(set(X[1]))):
            return 0
        (seen, ans) = (set(map(tuple, points)), float('inf'))
        for (i, (p1x, p1y)) in enumerate(points):
            for (p2x, p2y) in points[i + 1:]:
                if p1x != p2x and p1y != p2y and ((p1x, p2y) in seen) and ((p2x, p1y) in seen):
                    ans = min(ans, abs((p1x - p2x) * (p1y - p2y)))
        return ans if ans < float('inf') else 0
