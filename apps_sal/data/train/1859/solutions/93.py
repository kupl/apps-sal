class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        grid = matrix
        self.dp = [[[0, 0] for j in grid[0]] for i in grid]
        dp = self.dp

        def ut(r, c):
            if r >= 0 and c >= 0:
                return self.dp[r][c][0]
            return 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r and c and grid[r][c]:
                    dp[r][c][1] = min(dp[r][c - 1][1], dp[r - 1][c][1], dp[r - 1][c - 1][1])
                    if dp[r][c][1]:
                        dp[r][c][1] += 1

                dp[r][c][1] = max(dp[r][c][1], grid[r][c])
                dp[r][c][0] += dp[r][c][1]

                dp[r][c][0] += ut(r, c - 1) + ut(r - 1, c) - ut(r - 1, c - 1)
        print(dp)

        return dp[-1][-1][0]
