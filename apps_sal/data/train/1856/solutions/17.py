class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[float('inf'), float('inf')] for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0][1][0] = dp[1][0][0] = -1
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                h, v = False, False
                if grid[r - 1][c - 1] == 0 and c < n and grid[r - 1][c] == 0:
                    dp[r][c][0] = min(dp[r - 1][c][0], dp[r][c - 1][0]) + 1
                    h = True
                if grid[r - 1][c - 1] == 0 and r < n and grid[r][c - 1] == 0:
                    dp[r][c][1] = min(dp[r - 1][c][1], dp[r][c - 1][1]) + 1
                    v = True
                if v and c < n and grid[r][c] == 0:
                    dp[r][c][1] = min(dp[r][c][1], dp[r][c][0] + 1)
                if h and r < n and grid[r][c] == 0:
                    dp[r][c][0] = min(dp[r][c][0], dp[r][c][1] + 1)
        return dp[n][n - 1][0] if dp[n][n - 1][0] < float('inf') else -1

