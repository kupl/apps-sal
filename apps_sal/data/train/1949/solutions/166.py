class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.maxgold = 0

        def isvalid(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        def backtrack(cell, gold, visited):
            self.maxgold = max(self.maxgold, gold)
            x, y = cell[0], cell[1]
            neighbours = [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]
            for nbr in neighbours:
                if isvalid(nbr[0], nbr[1]) and not visited[nbr[0]][nbr[1]] and grid[nbr[0]][nbr[1]] != 0:
                    visited[nbr[0]][nbr[1]] = True
                    gold += grid[nbr[0]][nbr[1]]
                    backtrack(nbr, gold, visited)
                    self.maxgold = max(self.maxgold, gold)
                    gold -= grid[nbr[0]][nbr[1]]
                    visited[nbr[0]][nbr[1]] = False
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited[i][j] = True
                    backtrack([i, j], grid[i][j], visited)
                    visited[i][j] = False
        return self.maxgold
