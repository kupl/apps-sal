class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Floyd Washall
        # dp[i][j] 表示 uv 之间的最小距离
        dp = [ n * [float('inf')] for _ in range(n)]
        
        for f, t, w in edges:
            dp[f][t] = dp[t][f] = w
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])
                    
        res = -1
        minv = float('inf')
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dp[i][j] <= distanceThreshold:
                    count += 1
            if count <= minv:
                minv = count
                res = i
        return res
        
        

                    
                    
            
                    
            
            

