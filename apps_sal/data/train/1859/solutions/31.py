class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [0 for i in range(cols + 1)]
        tot = 0
        for i in range(rows):
            for j in range(cols):
                if not matrix[i][j]:
                    dp[j + 1] = 0
                    continue
                if dp[j + 1] == dp[j]:
                    dp[j + 1] += 1 if matrix[i - dp[j]][j - dp[j]] else 0 
                else:    
                    dp[j + 1] = min(dp[j + 1], dp[j]) + 1
                tot += dp[j + 1]
        return tot 
