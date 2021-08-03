from collections import Counter
from math import comb


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        c = Counter(item % 60 for item in time)
        for key in c.keys():
            if key == 30 or key == 0:
                if c[key] >= 2:
                    res += comb(c[key], 2)
            else:
                res += (c[key] * c[60 - key]) / 2

        return int(res)
