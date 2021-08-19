class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        (R, C) = (len(matrix), len(matrix[0]))
        dp = [[0 for i in range(C)] for j in range(R)]
        ans = 0
        for i in range(R):
            dp[i][0] = matrix[i][0]
            ans += dp[i][0]
        for j in range(C):
            dp[0][j] = matrix[0][j]
            ans += dp[0][j]
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    ans += dp[i][j]
                    print(i, j, ans)
        return ans if dp[0][0] == 0 else ans - 1
