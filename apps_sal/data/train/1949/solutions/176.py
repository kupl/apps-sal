class Solution:

    def __init__(self):
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(self, r, c):
        if r < 0 or r == self.m or c < 0 or c == self.n or self.grid[r][c] == 0:
            return 0
        original = self.grid[r][c]
        self.grid[r][c] = 0
        maxGold = max(self.dfs(r + x, c + y) for x, y in self.moves)
        self.grid[r][c] = original
        return maxGold + original

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        return max(self.dfs(i, j) for i in range(self.m) for j in range(self.n))
