class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        xs = collections.defaultdict(list)
        for (x, y) in points:
            xs[x].append(y)
        seen = {}
        result = math.inf
        for (x, ylist) in xs.items():
            for ys in itertools.combinations(ylist, 2):
                if ys in seen:
                    result = min(result, (x - seen[ys]) * (ys[1] - ys[0]))
                seen[ys] = x
        return 0 if math.isinf(result) else result
