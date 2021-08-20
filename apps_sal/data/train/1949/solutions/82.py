class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.max_gold = 0

        def backtrack(grid, row, col, current):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col]:
                temp = grid[row][col]
                grid[row][col] = 0
                for (drow, dcol) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    backtrack(grid, row + drow, col + dcol, current + temp)
                grid[row][col] = temp
            else:
                self.max_gold = max(self.max_gold, current)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    backtrack(grid, i, j, 0)
        return self.max_gold
