class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def travel(grid, x, y, gold):
            def valid(c, grid):
                x, y = c
                if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1 or grid[x][y] == 0:
                    return False
                return True
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            g = grid[x][y]
            grid[x][y] = 0
            maxg = -1
            for i in dirs:
                nc = x + i[0], y + i[1]
                if valid(nc, grid):
                    maxg = max(maxg, travel(grid, nc[0], nc[1], gold + g))
            grid[x][y] = g
            if maxg == -1:
                return gold + g
            return maxg

        maxg = 0
        for ri, row in enumerate(grid):
            for ci, e in enumerate(row):
                if e != 0:

                    k = travel(grid, ri, ci, 0)
                    maxg = max(maxg, k)

        return maxg
