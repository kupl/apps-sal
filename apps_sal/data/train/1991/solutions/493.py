class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0 for _ in range(len(locations))] for _ in range(fuel + 1)]
        dp[0][start] = 1
        for f in range(fuel + 1):
            for i in range(len(locations)):
                for j in range(len(locations)):
                    next_move = abs(locations[j] - locations[i]) + f
                    if i != j and next_move <= fuel:
                        dp[next_move][j] += dp[f][i]
        return sum(dp[row][finish] for row in range(fuel + 1)) % (10 ** 9 + 7)
