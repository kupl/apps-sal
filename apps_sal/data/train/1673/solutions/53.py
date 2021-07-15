class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        
        m, n = len(arr), len(arr[0])
        
        dp = [[float('inf')] * n for _ in range(m)]
        
        
        
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[0][j] = arr[0][j]
                else:
                    dp[i][j] = arr[i][j] + min(dp[i-1][x] for x in range(n) if x != j)
                    
        return min(dp[-1])
                

