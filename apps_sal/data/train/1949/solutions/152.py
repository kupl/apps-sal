class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_gold = 0
        for row in range(m):
            for col in range(n):
                max_gold = max(max_gold, self.findMaxGold(grid, row, col, 0))
        return max_gold

    def findMaxGold(self, grid, row, col, curr_gold):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (grid[row][col] != 0):
            origin = grid[row][col]
            grid[row][col] = 0
            max_gold = 0
            x_moves = [1, -1, 0, 0]
            y_moves = [0, 0, 1, -1]
            for i in range(0, 4):
                max_gold = max(max_gold, self.findMaxGold(grid, row + x_moves[i], col + y_moves[i], max_gold))
            grid[row][col] = origin
            return max_gold + origin
        else:
            return 0
