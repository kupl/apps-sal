class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def findSum(row, col, total):
            if row < 0 or row >= len(grid) or col < 0 or (col >= len(grid[0])):
                return
            if not grid[row][col]:
                return
            tmp = grid[row][col]
            total += tmp
            grid[row][col] = 0
            if row < len(grid):
                findSum(row + 1, col, total)
            if row >= 0:
                findSum(row - 1, col, total)
            if col < len(grid[0]):
                findSum(row, col + 1, total)
            if col >= 0:
                findSum(row, col - 1, total)
            self.sm = max(self.sm, total)
            grid[row][col] = tmp
        self.sm = 0
        total = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]:
                    findSum(row, col, total)
                    total = 0
        return self.sm
