import math


class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        solved = {}
        ps = [0] + piles[:]
        for i in range(1, len(ps)):
            ps[i] += ps[i - 1]

        def solve(p, m, is_alex):
            if (p, m, is_alex) in solved:
                return solved[p, m, is_alex]
            if p >= len(piles):
                return 0
            if is_alex:
                ms = -math.inf
                for x in range(1, 2 * m + 1):
                    if p + x < len(ps):
                        ms = max(ms, ps[p + x] - ps[p] + solve(p + x, max(x, m), not is_alex))
            else:
                ms = math.inf
                for x in range(1, 2 * m + 1):
                    if p + x < len(ps):
                        ms = min(ms, -(ps[p + x] - ps[p]) + solve(p + x, max(x, m), not is_alex))
            solved[p, m, is_alex] = ms
            return solved[p, m, is_alex]
        diff = solve(0, 1, True)
        return (sum(piles) + diff) // 2
