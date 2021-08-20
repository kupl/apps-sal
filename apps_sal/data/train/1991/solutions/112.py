class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def go(pos, f, dp):
            if f == 0:
                return 1 if pos == finish else 0
            if dp[pos][f] > -1:
                return dp[pos][f]
            ans = 1 if pos == finish else 0
            for (idx, loc) in enumerate(locations):
                if idx != pos:
                    c = abs(locations[pos] - loc)
                    ans += go(idx, f - c, dp) if f >= c else 0
            dp[pos][f] = ans
            return ans
        memo = [[-1] * (fuel + 1) for _ in locations]
        memo[finish][0] = 1
        return go(start, fuel, memo) % 1000000007
