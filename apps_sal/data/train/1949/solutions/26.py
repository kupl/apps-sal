class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        (n, m) = (len(grid), len(grid[0]))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.max_gold = 0
        self.v = set()

        def dfs(r, c, gold):
            self.max_gold = max(self.max_gold, gold)
            for d in dirs:
                (row, col) = (r + d[0], c + d[1])
                if 0 <= row < n and 0 <= col < m and (grid[row][col] != 0) and ((row, col) not in self.v):
                    self.v.add((row, col))
                    dfs(row, col, gold + grid[row][col])
                    self.v.remove((row, col))
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    self.v.add((i, j))
                    dfs(i, j, grid[i][j])
                    self.v.remove((i, j))
        return self.max_gold
