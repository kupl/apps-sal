class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                if dp[i-1][j] != 0 and dp[i][j-1] != 0 and dp[i-1][j-1] != 0:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        count = 0
        for row in dp:
            count += sum(row)
        return count

