from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(pos, f):

            # print (pos, f)

            nonlocal finish
            nonlocal MOD

            res = 0

            if f < 0:
                return 0

            if pos == finish:
                res += 1

            if f == 0:
                return res

            for i, vi in enumerate(locations):
                if i == pos:
                    continue

                res += dp(i, f - abs(locations[pos] - vi))

            return res % MOD

        ans = dp(start, fuel)

        return ans % MOD
