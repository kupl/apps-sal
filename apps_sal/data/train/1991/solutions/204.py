class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[-1] * (fuel + 1) for _ in range(n)]

        def solve(current, fuel):
            if fuel < 0:
                return 0
            if dp[current][fuel] != -1:
                return dp[current][fuel]
            ans = 1 if current == finish else 0
            for next in range(n):
                if next != current:
                    ans = (ans + solve(next, fuel - abs(locations[current] - locations[next]))) % 1000000007
            dp[current][fuel] = ans
            return ans

        return solve(start, fuel)
