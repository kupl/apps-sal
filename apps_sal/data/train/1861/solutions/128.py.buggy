class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        points = map(tuple, points)
        xdict, ydict = collections.defaultdict(list), collections.defaultdict(list)
        pset = set()
        res = float(\"inf\")
        for point in points:
            xdict[point[0]].append(point)
            ydict[point[1]].append(point)
            pset.add(point)
        for x1 in xdict.keys():
            if len(xdict[x1]) == 1:
                continue
            for i in range(len(xdict[x1]) - 1):
                p1 = xdict[x1][i]
                for j in range(i + 1, len(xdict[x1])):
                    p2 = xdict[x1][j]
                    for p3 in ydict[p1[1]]:
                        if p3 != p1:
                            if (p3[0], p2[1]) in pset:
                                res = min(res, abs((p3[0] - p1[0]) * (p2[1] - p1[1])))
        return res if res != float(\"inf\") else 0
