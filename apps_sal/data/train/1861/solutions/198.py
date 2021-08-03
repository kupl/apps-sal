from collections import defaultdict


class Solution:
    def minAreaRect(self, points):
        pSet, ans = set(map(tuple, points)), float('inf')
        for i, (p1x, p1y) in enumerate(points):
            for (p2x, p2y) in points[i + 1:]:
                if (p1x != p2x) and (p1y != p2y) and ((p1x, p2y) in pSet) and ((p2x, p1y) in pSet):
                    ans = min(ans, abs((p1x - p2x) * (p1y - p2y)))
        return ans if ans < float('inf') else 0


class Solution:
    def minAreaRect(self, points):
        X = list(zip(*points))
        if len(set(X[0])) == 1 or len(set(X[1])) == 1:
            return 0

        pSet, ans = set(map(tuple, points)), float('inf')
        for i, (p1x, p1y) in enumerate(points):
            for (p2x, p2y) in points[i + 1:]:
                area = abs((p2x - p1x) * (p2y - p1y))
                if area > ans or area == 0:
                    continue
                if (p1x, p2y) in pSet and (p2x, p1y) in pSet:
                    ans = area
        return ans if ans < float('inf') else 0


class Solution:
    def minAreaRect(self, points):
        X = list(zip(*points))
        Nr, Nc = len(set(X[0])), len(set(X[1]))
        if Nr == 1 or Nc == 1:
            return 0

        points.sort()
        columns = defaultdict(list)
        for r, c in points:
            columns[r].append(c)
        ans, lastc = float('inf'), dict()
        for r, cols in list(columns.items()):
            for i, c1 in enumerate(cols):
                for c2 in cols[i + 1:]:
                    if (c1, c2) in lastc:
                        area = (r - lastc[(c1, c2)]) * (c2 - c1)
                        #ans = min(ans, area)
                        if area < ans:
                            ans = area
                    lastc[(c1, c2)] = r
        return ans if ans < float('inf') else 0
