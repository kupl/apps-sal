class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def backtrack(r, c):
            grid[r][c] = -grid[r][c]
            maxlen = 0
            for (i, j) in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= i < M and 0 <= j < N and (grid[i][j] > 0):
                    maxlen = max(maxlen, backtrack(i, j))
            grid[r][c] = -grid[r][c]
            return maxlen + grid[r][c]
        res = 0
        (M, N) = (len(grid), len(grid[0]))
        for r in range(M):
            for c in range(N):
                if grid[r][c] > 0:
                    res = max(res, backtrack(r, c))
        return res
