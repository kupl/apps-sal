class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        r, c = len(grid), len(grid[0])
        dp = [[[0, 0] for i in range(c + 1)] for j in range(r + 1)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    dp[i + 1][j + 1][0] = dp[i][j + 1][0] + 1
                    dp[i + 1][j + 1][1] = dp[i + 1][j][1] + 1

        ans = 0
        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                poss_length = min(dp[i + 1][j + 1])
                while poss_length > ans:
                    if dp[i + 1][j - poss_length + 2][0] >= poss_length and dp[i - poss_length + 2][j + 1][1] >= poss_length:
                        ans = poss_length

                    poss_length -= 1

        return ans ** 2
