from functools import lru_cache


class Solution:
    def countRoutes(self, A: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def helper(i, fuel):
            if fuel < 0:
                return 0

            res = 0
            if i == finish:
                res += 1

            for nxt in range(len(A)):
                if nxt != i:
                    res = (res + helper(nxt, fuel - abs(A[i] - A[nxt]))) % 1000000007
            return res

        return helper(start, fuel)
