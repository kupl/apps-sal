class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # dp(i, j) = number of squares that have bottom right corner at x1, y1
        
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i-1>=0 and j-1>=0 and matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
                elif matrix[i][j] == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
                        
        count = 0
        for i in range(m):
            for j in range(n):
                count += dp[i][j]
        
        return count

