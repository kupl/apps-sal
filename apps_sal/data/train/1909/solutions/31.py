class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[None] * cols for _ in range(rows)]
        maxSize = 0
        for i in range(rows):
            for j in range(cols):
                (x, y) = (0, 0)
                if grid[i][j] == 1:
                    if i > 0 and dp[i - 1][j]:
                        x = dp[i - 1][j][0] + 1
                    if j > 0 and dp[i][j - 1]:
                        y = dp[i][j - 1][1] + 1
                    dp[i][j] = (x, y)
                    sqlen = min(x, y)
                    while sqlen >= maxSize:
                        left = dp[i][j - sqlen]
                        up = dp[i - sqlen][j]
                        if left[0] >= sqlen and up[1] >= sqlen:
                            maxSize = sqlen + 1
                        sqlen -= 1
        return maxSize * maxSize
