class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        def dp(i, f, memo):
            if i == finish and f == 0:
                return 1
            if (i, f) not in memo:
                ans = int(i == finish)
                for j in range(len(locations)):
                    d = abs(locations[j] - locations[i])
                    if i != j and f >= d:
                        ans += dp(j, f - d, memo)
                        ans %= MOD
                memo[(i, f)] = ans
            return memo[(i, f)]
        return dp(start, fuel, {})
