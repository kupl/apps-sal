class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # O(fuel*n^2)
        n = len(locations)
        dp = [[-1] * (fuel + 1) for _ in range(n)]

        def solve(current, fuel):
            # 4. if there is no fuel left
            if fuel < 0:
                return 0
            if dp[current][fuel] != -1:
                return dp[current][fuel]
            # 3. if current city is finish, add 1 to the ans and keep going further
            ans = 1 if current == finish else 0
            for next in range(n):
                # 1. visit all cities except current
                if next != current:
                    # continue this process recursively
                    ans = (ans + solve(next, fuel - abs(locations[current] - locations[next]))) % 1000000007
            dp[current][fuel] = ans
            return ans

        return solve(start, fuel)
