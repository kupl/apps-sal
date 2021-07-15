import numpy as np
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        R, C, count = len(grid), len(grid[0]), 0
        dp=[[[0,0]for _ in range(C +1)]for _ in range(R + 1)]
        for i in range(1,R + 1):
            for j in range(1,C + 1):
                if grid[i - 1][j - 1]==1:
                    dp[i][j][0], dp[i][j][1] = dp[i - 1][j][0] + 1, dp[i][j - 1][1] + 1
                    for k in range(min(dp[i][j][0], dp[i][j][1]), count, -1):
                        if min(dp[i - k + 1][j][1], dp[i][j - k + 1][0]) >= k:
                            count = max(count, k)
                            break
        return count**2
