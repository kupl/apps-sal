class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        lookup = set()
        for (x1, y1) in points:
            for (x2, y2) in lookup:
                if (x1, y2) in lookup and (x2, y1) in lookup:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))
            lookup.add((x1, y1))
        return res if res != float('inf') else 0
        ys_with_same_x = defaultdict(list)
        for (x, y) in points:
            ys_with_same_x[x].append(y)
        pair_of_ys_history = {}
        res = float('inf')
        for (x, ys) in sorted(ys_with_same_x.items()):
            ys.sort()
            for (i, y1) in enumerate(ys):
                for j in range(i):
                    y2 = ys[j]
                    if (y1, y2) in pair_of_ys_history:
                        res = min(res, (x - pair_of_ys_history[y1, y2]) * (y1 - y2))
                    pair_of_ys_history[y1, y2] = x
        if res == float('inf'):
            return 0
        else:
            return res
