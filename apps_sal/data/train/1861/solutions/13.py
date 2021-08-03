class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        cache_x = defaultdict(set)
        cache_y = defaultdict(set)
        cache = set()
        for i, p in enumerate(points):
            cache_x[p[0]].add(i)
            cache_y[p[1]].add(i)
            cache.add((p[0], p[1]))

        res = float('inf')
        for i, (x0, y0) in enumerate(points):
            cache_x[x0].remove(i)
            cache_y[y0].remove(i)
            cache.remove((x0, y0))
            for ix in cache_y[y0]:
                for iy in cache_x[x0]:
                    x1, y1 = points[ix][0], points[iy][1]
                    if (x1, y1) in cache:
                        res = min(res, abs(x1 - x0) * abs(y1 - y0))
        return 0 if res == float('inf') else res
