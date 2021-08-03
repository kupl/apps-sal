def getArea(x1, y1, x2, y2, dp):
    return dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        h, w = len(grid), len(grid[0])
        dp = [[0 for j in range(w + 1)] for i in range(h + 1)]
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + grid[i - 1][j - 1]
        for l in range(min(h, w), 0, -1):
            for x1 in range(1, h + 1):
                for y1 in range(1, w + 1):
                    x2 = x1 + l - 1
                    y2 = y1 + l - 1
                    if x2 > h or y2 > w:
                        continue
                    if (getArea(x1, y1, x2, y1, dp) == l
                        and getArea(x1, y1, x1, y2, dp) == l
                        and getArea(x1, y2, x2, y2, dp) == l
                            and getArea(x2, y1, x2, y2, dp) == l):
                        return l * l
        return 0
