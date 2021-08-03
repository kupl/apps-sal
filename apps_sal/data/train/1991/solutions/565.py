MOD = 10 ** 9 + 7


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        @lru_cache(None)
        def dp(pos, left):
            ans = int(pos == finish)
            if left == 0:
                return ans
            for i in range(n):
                if i != pos:
                    cost = abs(locations[pos] - locations[i])
                    if cost <= left:
                        ans += dp(i, left - cost)
                        if ans > MOD:
                            ans %= MOD
            return ans
        return dp(start, fuel)
