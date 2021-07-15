class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = min(dp[i][j+1], min(dp[i+1][j], dp[i][j])) + 1
        
        cnts = [0 for _ in range(min(m, n) + 1)]
        for i in range(1, min(m, n) + 1):
            cnts[i] = i ** 2 + cnts[i-1]
        
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                res += dp[i][j]
        return res
