import collections


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        p = collections.defaultdict(list)
        for (x, y) in points:
            p[x].append(y)
        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    (y1, y2) = (p[x][j], p[x][i])
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float('inf') else 0
