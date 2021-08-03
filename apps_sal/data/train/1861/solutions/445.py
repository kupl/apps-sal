from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0

        d = defaultdict(set)
        for (x, y) in points:
            d[x].add(y)

        xs = sorted(d.keys())
        # print(d, xs)
        ans = float('inf')

        exist = False
        for i in range(len(xs) - 1):
            x1 = xs[i]
            ys1 = d[x1]
            for j in range(i + 1, len(xs)):
                x2 = xs[j]
                ys2 = d[x2]
                ys = sorted(ys1 & ys2)
                # print(x1, x2, ys)
                if len(ys) >= 2:
                    exist = True
                    minHeight = ys[1] - ys[0]
                    for j in range(2, len(ys)):
                        minHeight = min(minHeight, ys[j] - ys[j - 1])
                    ans = min(ans, minHeight * (x2 - x1))

        return 0 if not exist else ans
