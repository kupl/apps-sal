class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        dp = [[float(\"inf\")] *n for _ in range(n)]
        
        for i,j,w in edges:
            dp[i][j] = dp[j][i] = w
            
        for i in range(n):
            dp[i][i] = 0
            
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    dp[j][k] = min(dp[j][k] , dp[j][i] + dp[i][k])
                    
        res = { sum(d <= distanceThreshold for d in dp[i]) : i for i in range(n) }
        
        return res[min(res)]
    
        
        
        
