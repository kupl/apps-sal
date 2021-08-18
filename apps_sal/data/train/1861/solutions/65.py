class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        nx, ny = len(set(x for x, _ in points)), len(set(y for _, y in points))

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
        for x1, x2 in itertools.combinations(p, 2):
            if (len(p[x1]) < 2 or len(p[x2]) < 2):
                continue
            for y1, y2 in itertools.combinations(sorted(set(p[x1]) & set(p[x2])), 2):
                res = min(res, abs(x1 - x2) * (y2 - y1))
        return res if res < float('inf') else 0
