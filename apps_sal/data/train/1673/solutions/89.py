class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
        for i in range(len(dp[0])):
            dp[0][i] = arr[0][i]
            
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                mi = -1
                for k in range(len(dp[0])):
                    if not j == k:
                        if mi == -1 or dp[i-1][k] + arr[i][j] < mi:
                            mi = dp[i-1][k] + arr[i][j]
                dp[i][j] = mi
        
        return min(dp[-1])
