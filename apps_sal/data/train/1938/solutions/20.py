import numpy as np


class Solution:
    def rectangleArea(self, A: List[List[int]]) -> int:
        sa = sorted(set(a for x1, y1, x2, y2 in A for a in [x1, x2]))
        xs = sorted(sa)
        dic = {v: i for i, v in enumerate(xs)}
        B = []
        for x1, y1, x2, y2 in A:
            B.append([y1, x1, x2, 1])
            B.append([y2, x1, x2, -1])
        B.sort()
        sum_x = ret = cur_y = 0
        ct = np.zeros(len(xs))
        for y, x1, x2, flag in B:
            ret += sum_x * (y - cur_y)
            cur_y = y
            ct[dic[x1]:dic[x2]] += flag
            sum_x = sum([x2 - x1 for x1, x2, f in zip(xs, xs[1:], ct) if f])
        return ret % (10 ** 9 + 7)
