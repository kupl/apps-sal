class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10 ** 9 + 7
        dist = {}
        for i in range(n):
            for j in range(i + 1, n):
                dist[(i, j)] = dist[(j, i)] = abs(locations[i] - locations[j])

        dp = [[0] * n for _ in range(fuel + 1)]
        dp[0][start] = 1
        for f in range(1, fuel + 1):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        cur = f - dist[(i, j)]
                        if cur >= 0:
                            dp[f][i] += dp[cur][j] % mod
        ans = 0
        for f in range(fuel + 1):
            ans += dp[f][finish] % mod
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

