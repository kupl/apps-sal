class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1 for _ in range(fuel + 1)] for _ in locations]

        def search(start, fuel):
            if fuel == 0:
                if start == finish:
                    return 1
                return 0
            if dp[start][fuel] != -1:
                return dp[start][fuel]
            dp[start][fuel] = 1 if start == finish else 0
            for i in range(len(locations)):
                left = fuel - abs(locations[i] - locations[start])
                if i != start and left >= 0:
                    dp[start][fuel] += search(i, left)
            return dp[start][fuel] % 1000000007
        return search(start, fuel) % 1000000007
