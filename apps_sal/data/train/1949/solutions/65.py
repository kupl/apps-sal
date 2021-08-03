class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        self.nrow = len(grid)
        self.ncol = len(grid[0])

        max_gold = 0

        for i in range(self.nrow):
            for j in range(self.ncol):
                if grid[i][j] != 0:
                    max_seen = self._dfs(grid, i, j, set())

                    if max_seen > max_gold:
                        max_gold = max_seen

        return max_gold

    def _dfs(self, grid, i, j, visited):
        child_max = []
        visited.add((i, j))

        for dx, dy in self.dirs:
            if 0 <= i + dx < self.nrow and 0 <= j + dy < self.ncol:
                if grid[i + dx][j + dy] != 0 and (i + dx, j + dy) not in visited:
                    dir_sum = self._dfs(grid, i + dx, j + dy, visited)
                    child_max.append(dir_sum)

        visited.remove((i, j))

        max_child = max(child_max) if child_max else 0

        return grid[i][j] + max_child
