import itertools


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        ybucket = defaultdict(list)
        for x, y in points:
            ybucket[y].append(x)

        for k, v in ybucket.items():
            if len(v) >= 2:
                ybucket[k] = sorted(v)

        ys = [k for k in ybucket.keys() if len(ybucket[k]) >= 2]
        ans = float('inf')
        for y1, y2 in itertools.combinations(ys, 2):
            row1 = set(ybucket[y1])
            row2 = ybucket[y2]
            dy = abs(y2 - y1)
            xlast = None
            for x in row2:
                if x in row1:
                    if xlast is not None:
                        ans = min(ans, abs(x - xlast) * dy)
                    xlast = x

        return ans if ans < float('inf') else 0
