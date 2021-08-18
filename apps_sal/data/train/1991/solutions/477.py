import heapq
from collections import defaultdict


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0] * (fuel + 1) for i in range(n)]
        dp[start][fuel] = 1
        for f in range(fuel, -1, -1):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        need = abs(locations[i] - locations[j])
                        if f + need <= fuel:
                            dp[i][f] += dp[j][f + need]

        ans = 0
        for i in range(fuel + 1):
            ans += (dp[finish][i] % (10**9 + 7))
        return ans % (10**9 + 7)
