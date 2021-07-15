class Solution(object):
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)
        
        # init dp array (dp[i][j] min sum from i,j forward)
        dp = [[0 for i in range(N)] for j in range(N)]
        
        # init last row of dp (base case)
        for j in range(N):
            dp[-1][j] = A[-1][j]
            
        for i in range(N-2, -1, -1):
            for j in range(N):
                if j == 0:
                    # left column
                    dp[i][j] = A[i][j] + min(dp[i+1][1:])
                elif j == N-1:
                    # right column
                    dp[i][j] = A[i][j] + min(dp[i+1][:-1])
                else:
                    # not border column
                    dp[i][j] = A[i][j] + min(dp[i+1][:j]+dp[i+1][j+1:])
        
        print(dp)
        return min(dp[0])
