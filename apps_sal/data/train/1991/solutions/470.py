class Solution:

    def countRoutes0(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        L = len(locations)

        @lru_cache(None)
        def move(loc, remaining):
            if remaining < 0:
                return 0
            ans = 0
            if loc == finish:
                ans += 1
            for i in range(L):
                if i == loc:
                    continue
                ans += move(i, remaining - abs(locations[i] - locations[loc]))
            return ans
        return move(start, fuel) % 1000000007

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}
        for i in range(len(locations)):
            if i == finish:
                dp[i] = {0: 1}
            else:
                dp[i] = {0: 0}
        for j in range(1, fuel + 1):
            for i in range(len(locations)):
                if i == finish:
                    ans = 1
                else:
                    ans = 0
                for k in range(len(locations)):
                    if k != i:
                        f = j - abs(locations[i] - locations[k])
                        if f >= 0:
                            ans += dp[k][f]
                dp[i][j] = ans % 1000000007
        return dp[start][fuel]
