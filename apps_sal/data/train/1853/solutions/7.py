class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        
        for s, e, w in edges:
            dp[s][e] = w
            dp[e][s] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                    
                    
        minlen = n
        res = -1

        for i, row in enumerate(dp):
            cnt = sum(v <= distanceThreshold and j != i for j, v in enumerate(row))
            if cnt <= minlen:
                minlen = cnt
                res = i
                
        return res
