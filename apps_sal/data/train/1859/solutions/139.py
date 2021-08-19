class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        presum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        tot = 0
        for r in range(len(matrix)):
            cur_row = [0] * (len(matrix[0]) + 1)
            for c in range(len(matrix[0])):
                cur_row[c] = cur_row[c - 1] + matrix[r][c]
                presum[r][c] = presum[r - 1][c] + cur_row[c]
                if matrix[r][c] == 0:
                    dp[r][c] = 0
                else:
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1
                    tot += dp[r][c]
        return tot
