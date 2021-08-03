class Solution:
    def _getMaximumGold(self, cur_sum, i, j, grid):
        m = len(grid)
        n = len(grid[0])

        max_sum = cur_sum

        if i + 1 < m and grid[i + 1][j] != 0:
            val = grid[i + 1][j]
            grid[i + 1][j] = 0

            temp_max_sum = self._getMaximumGold(cur_sum + val, i + 1, j, grid)

            grid[i + 1][j] = val

            if temp_max_sum > max_sum:
                max_sum = temp_max_sum

        if j + 1 < n and grid[i][j + 1] != 0:
            val = grid[i][j + 1]
            grid[i][j + 1] = 0

            temp_max_sum = self._getMaximumGold(cur_sum + val, i, j + 1, grid)

            grid[i][j + 1] = val

            if temp_max_sum > max_sum:
                max_sum = temp_max_sum

        if i - 1 >= 0 and grid[i - 1][j] != 0:
            val = grid[i - 1][j]
            grid[i - 1][j] = 0

            temp_max_sum = self._getMaximumGold(cur_sum + val, i - 1, j, grid)

            grid[i - 1][j] = val

            if temp_max_sum > max_sum:
                max_sum = temp_max_sum

        if j - 1 >= 0 and grid[i][j - 1] != 0:
            val = grid[i][j - 1]
            grid[i][j - 1] = 0

            temp_max_sum = self._getMaximumGold(cur_sum + val, i, j - 1, grid)

            grid[i][j - 1] = val

            if temp_max_sum > max_sum:
                max_sum = temp_max_sum

        return max_sum

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0

        m = len(grid)
        n = len(grid[0])

        total_max_sum = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                start = grid[i][j]
                grid[i][j] = 0

                max_sum = self._getMaximumGold(start, i, j, grid)

                if max_sum > total_max_sum:
                    total_max_sum = max_sum

                grid[i][j] = start

        return total_max_sum
