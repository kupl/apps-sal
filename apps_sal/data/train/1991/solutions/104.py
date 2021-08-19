class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0 for x in range(len(locations))] for _ in range(fuel + 1)]
        dp[0][start] = 1
        for i in range(1, fuel + 1):
            for j in range(len(locations)):
                for k in range(len(locations)):
                    if j != k:
                        need = abs(locations[j] - locations[k])
                        if need <= i:
                            dp[i][j] += dp[i - need][k]
        ans = 0
        for i in range(fuel + 1):
            ans += dp[i][finish]
        return ans % (10 ** 9 + 7)

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        M = 10 ** 9 + 7

        @lru_cache(None)
        def helper(curr_city, curr_fuel):
            if curr_fuel < 0:
                return 0
            ans = 0
            if curr_city == finish:
                ans += 1
            for i in range(len(locations)):
                if i != curr_city:
                    ans += helper(i, curr_fuel - abs(locations[i] - locations[curr_city]))
                    ans %= M
            return ans
        return helper(start, fuel)
