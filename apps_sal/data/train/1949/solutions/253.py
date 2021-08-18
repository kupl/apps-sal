from collections import defaultdict


class Solution:
    def dfs(self, i, j, m, n, grid):
        tmp = grid[i][j]
        grid[i][j] = 0
        max_next_sum = 0
        for d in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
            new_i, new_j = i + d[0], j + d[1]
            if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j]:
                max_next_sum = max(max_next_sum, self.dfs(new_i, new_j, m, n, grid))
        grid[i][j] = tmp
        return grid[i][j] + max_next_sum

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        res = 0
        if len(grid) < 1 or len(grid[0]) < 1:
            return res

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, self.dfs(i, j, m, n, grid))
        return res
