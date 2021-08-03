class Solution:

    def _help(self, locations, start, finish, fuel, dp):
        if fuel < 0:
            return 0
        elif dp[fuel][start] is not None:
            return dp[fuel][start]

        ni = 1 if start == finish else 0
        for i, loc in enumerate(locations):
            if i != start:
                ni += self._help(locations, i, finish, fuel - abs(locations[i] - locations[start]), dp)
        dp[fuel][start] = ni
        return ni

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[None] * n for _ in range(fuel + 1)]

        self._help(locations, start, finish, fuel, dp)
        return dp[-1][start] % 1000000007
