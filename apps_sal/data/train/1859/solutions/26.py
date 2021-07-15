class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = min(dp[i+1][j],dp[i][j+1],dp[i][j]) + 1
                    res += dp[i+1][j+1]
        return res
        

