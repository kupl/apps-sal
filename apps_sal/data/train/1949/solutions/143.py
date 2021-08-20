class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(row, col, curgold):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (grid[row][col] > 0):
                temp = grid[row][col]
                grid[row][col] = 0
                dfs(row + 1, col, curgold + temp)
                dfs(row - 1, col, curgold + temp)
                dfs(row, col + 1, curgold + temp)
                dfs(row, col - 1, curgold + temp)
                self.maxgold = max(self.maxgold, curgold + temp)
                grid[row][col] = temp
        self.maxgold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    dfs(i, j, 0)
        return self.maxgold
