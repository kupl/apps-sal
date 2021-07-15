class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        R = len(arr)
        C = len(arr[0])
        
        dp = [[float('inf') for j in range(C)] for i in range(R)]
        
        for i in range(C):
            dp[0][i] = arr[0][i]
            
        for r in range(1,R):
            for c in range(C):
                dp[r][c] = arr[r][c] + min(dp[r-1][k] if k!=c else float('inf') for k in range(C))
                
        return min(dp[R-1])
