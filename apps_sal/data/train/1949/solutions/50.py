class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_ = 0
        (n, m) = (len(grid), len(grid[0]))

        def backtrack(i, j, accum):
            nonlocal max_
            if grid[i][j] == 0:
                max_ = max(max_, accum)
                return
            (collected, grid[i][j]) = (grid[i][j], 0)
            accum += collected
            for (di, dj) in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                (try_i, try_j) = (i + di, j + dj)
                if 0 <= try_i < n and 0 <= try_j < m:
                    backtrack(try_i, try_j, accum)
            grid[i][j] = collected
            accum -= collected
        for i in range(n):
            for j in range(m):
                backtrack(i, j, 0)
        return max_
