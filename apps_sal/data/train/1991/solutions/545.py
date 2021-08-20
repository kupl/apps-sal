class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0] * n for i in range(fuel + 1)]
        dp[0][start] = 1
        for f in range(fuel):
            for x in range(n):
                if dp[f][x] == 0:
                    continue
                for y in range(n):
                    if x == y:
                        continue
                    g = f + abs(locations[x] - locations[y])
                    if g <= fuel:
                        dp[g][y] += dp[f][x]
        return sum((dp[i][finish] for i in range(fuel + 1))) % 1000000007
