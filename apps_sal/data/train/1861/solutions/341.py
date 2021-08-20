import itertools


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        ybucket = defaultdict(list)
        for (x, y) in points:
            ybucket[y].append(x)
        for (k, v) in ybucket.items():
            if len(v) >= 2:
                ybucket[k] = sorted(v)
        ys = [k for k in ybucket.keys() if len(ybucket[k]) >= 2]
        ans = 2 ** 31 - 1
        for (y1, y2) in itertools.combinations(ys, 2):
            row1 = set(ybucket[y1])
            row2 = ybucket[y2]
            for (idx, x) in enumerate(row2):
                if x in row1:
                    print(x)
                    xlast = x
                    idx_last = idx
                    break
            else:
                continue
            dy = abs(y2 - y1)
            for x in row2[idx_last + 1:]:
                if x in row1:
                    ans = min(ans, abs(x - xlast) * dy)
                    xlast = x
        return ans if ans < 2 ** 31 - 1 else 0
