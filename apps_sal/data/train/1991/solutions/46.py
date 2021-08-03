class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def dp(curr, fuel):
            # print(curr,fuel)
            nonlocal mod
            if fuel < 0:
                return 0
            ans = 0
            if curr == finish:
                ans += 1
            if fuel < 0:
                return 0
            for i in range(len(locations)):
                if i == curr or fuel < abs(locations[i] - locations[curr]):
                    continue
                ans += dp(i, fuel - abs(locations[i] - locations[curr]))
            return ans
        return dp(start, fuel) % mod
        # return ans
