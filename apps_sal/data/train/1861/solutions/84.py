class Solution(object):
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        setx = set()
        sety = set()
        for x, y in points:
            setx.add(x)
            sety.add(y)
        nx = len(setx)
        ny = len(sety)

        if nx == n or ny == n:
            return 0
        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        res = float('inf')
        dic_last = {}
        for x in sorted(p):
            p[x].sort()
            for y1, y2 in itertools.combinations(p[x], 2):
                if (y1, y2) in dic_last:
                    res = min(res, (x - dic_last[y1, y2]) * (y2 - y1))
                dic_last[y1, y2] = x
        return res if res < float('inf') else 0
