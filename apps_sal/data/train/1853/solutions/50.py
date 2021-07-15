class Solution:
    \"\"\"
    Floyd-Warshall
    \"\"\"
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        
        for u, v, w in edges:
            dp[u][v] = w
            dp[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == k or j == k:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
        
        min_city = n-1
        min_reachable = float('inf')
        for i in range(n):
            reachable = sum([dp[i][dst] <= distanceThreshold for dst in range(n)])
            if reachable <= min_reachable:
                min_city = i
                min_reachable = reachable
        
        return min_city
