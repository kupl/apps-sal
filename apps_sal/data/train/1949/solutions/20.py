class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.answer = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return 0
            if j < 0 or j >= len(grid[0]):
                return 0

            if grid[i][j] == 0:
                return 0

            temp = grid[i][j]
            grid[i][j] = 0

            storage = temp + max(dfs(i + 1, j), dfs(i - 1, j), dfs(i, j - 1), dfs(i, j + 1))
            self.answer = max(self.answer, storage)
            grid[i][j] = temp
            return storage

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i, j)

        return self.answer
