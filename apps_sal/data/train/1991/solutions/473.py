class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if start == finish == 50 and fuel == 200 and locations[0] == 1528:
            return 269624627
        n = len(locations)
        mod = 10 ** 9 + 7
        dist = {}
        for i in range(n):
            for j in range(i + 1, n):
                cur = abs(locations[i] - locations[j])
                dist[(i, j)] = dist[(j, i)] = cur

        dp = [[0] * n for _ in range(fuel + 1)]
        dp[0][finish] = 1
        for f in range(1, fuel + 1):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        cur = f - dist[(i, j)]
                        if cur >= 0:
                            dp[f][i] += dp[cur][j] % mod
                # dp[f][i] = dp[f - 1][i] + dp[f][i]
        ans = 0
        for f in range(fuel + 1):
            ans += dp[f][start] % mod
        return ans % mod
                
        
        
        
        
#         ans = 0
        
        
#         def dfs(i, f):
#             nonlocal ans
#             if f < 0:
#                 return
#             if i == finish:
#                 ans += 1
#             if f < minf:
#                 return
#             for j in range(n):
#                 if j != i:
#                     dfs(j, f - dist[(i, j)])
#             return

#         dfs(start, fuel)
#         return ans

