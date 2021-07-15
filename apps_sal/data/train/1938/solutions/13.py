class Solution:
    def rectangleArea(self, rects: List[List[int]]) -> int:
        xs = sorted(set([x for x1, y1, x2, y2 in rects for x in [x1, x2]]))
        xi = {v: i for i, v in enumerate(xs)}
        cnt = [0] * len(xs)
        L = []
        for x1, y1, x2, y2 in rects:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()
        res = last_y = sum_x = 0
        for y, x1, x2, sig in L:
            res += (y-last_y) * sum_x
            last_y = y
            for i in range(xi[x1], xi[x2]):
                cnt[i] += sig
            sum_x = sum(x2-x1 for x1, x2, c in zip(xs, xs[1:], cnt) if c)
        return res %(10**9+7)
