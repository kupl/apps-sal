from collections import defaultdict


class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = defaultdict(int)
        for (n, s, e) in trips:
            d[s] += n
            d[e] -= n
        cur = 0
        for k in sorted(d):
            cur += d[k]
            if cur > capacity:
                return False
        return True
