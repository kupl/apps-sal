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
                length = min(dp[j + 1], dp[j]) 
                dp[j + 1] = length + matrix[i - length][j - length]
                tot += dp[j + 1]
        return tot 
