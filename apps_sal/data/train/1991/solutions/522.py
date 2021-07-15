class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        fuel += 1
        r = range(len(locations))
        dp = [[0]*fuel for i in r]
        for k, i in itertools.product(range(fuel), r):
            dp[i][k] = int(i == finish)
            for j, location in enumerate(locations):
                if j != i:
                    f = k - abs(locations[i] - locations[j])
                    if f >= 0:
                        dp[i][k] += dp[j][f]
        return dp[start][-1] % (10**9 + 7)
