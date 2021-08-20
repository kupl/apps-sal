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
        S = set(map(tuple, points))
        ans = float('inf')
        for (j, p2) in enumerate(points):
            for (i, p1) in enumerate(points[:j]):
                if p1[0] != p2[0] and p1[1] != p2[1] and ((p1[0], p2[1]) in S) and ((p2[0], p1[1]) in S):
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return ans if ans < float('inf') else 0
