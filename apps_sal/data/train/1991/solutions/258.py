class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        memo = [[-1 for j in range(fuel + 1)] for i in range(len(locations))]

        def dp(start, fuel):
            nonlocal memo
            nonlocal finish
            nonlocal locations
            if memo[start][fuel] == -1:
                memo[start][fuel] = 1 if start == finish else 0
                for i in range(len(locations)):
                    if i != start and fuel >= abs(locations[start] - locations[i]):
                        memo[start][fuel] += dp(i, fuel - abs(locations[start] - locations[i]))
                        memo[start][fuel] %= 10 ** 9 + 7
            return memo[start][fuel]
        return dp(start, fuel)
