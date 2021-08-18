import math
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        solved = {}
        ps = [0] + piles[:]
        for i in range(1, len(ps)):
            ps[i] += ps[i - 1]

        @lru_cache(None)
        def solve(p, m, is_alex):
            if p >= len(piles):
                return 0
            if is_alex:
                ms = -math.inf
                for x in range(1, 2 * m + 1):
                    if p + x < len(ps):
                        ms = max(ms, ps[p + x] - ps[p] + solve(p + x, max(x, m), not is_alex))
                    else:
                        break
            else:
                ms = math.inf
                for x in range(1, 2 * m + 1):
                    if p + x < len(ps):
                        ms = min(ms, - (ps[p + x] - ps[p]) + solve(p + x, max(x, m), not is_alex))
                    else:
                        break
            solved[(p, m, is_alex)] = ms
            return solved[(p, m, is_alex)]

        diff = solve(0, 1, True)
        return (ps[-1] + diff) // 2
