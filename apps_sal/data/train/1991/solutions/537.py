class Solution:

    def countRoutes(self, L: List[int], S: int, F: int, FU: int) -> int:

        @lru_cache(None)
        def dp(i, cur_fuel):
            if cur_fuel == 0:
                return i == F
            total = 0
            if i == F:
                total += 1
            for k in range(len(L)):
                if k == i:
                    continue
                consumption = abs(L[k] - L[i])
                if consumption <= cur_fuel:
                    total += dp(k, cur_fuel - consumption)
            return total
        MOD = 10 ** 9 + 7
        return dp(S, FU) % MOD
