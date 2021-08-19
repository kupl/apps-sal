from typing import List


class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or (j >= cols) or (grid[i][j] == 0):
                return 0
            val = grid[i][j]
            _sum = val
            grid[i][j] = 0
            _sum = max(_sum, val + dfs(i - 1, j))
            _sum = max(_sum, val + dfs(i, j - 1))
            _sum = max(_sum, val + dfs(i + 1, j))
            _sum = max(_sum, val + dfs(i, j + 1))
            grid[i][j] = val
            return _sum
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))
        return ans
