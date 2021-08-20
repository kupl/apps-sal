class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res = 0
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j, cur):
            cur += grid[i][j]
            end = True
            for (di, dj) in direction:
                (i1, j1) = (i + di, j + dj)
                if 0 <= i1 < len(grid) and 0 <= j1 < len(grid[0]) and (grid[i1][j1] > 0) and ((i1, j1) not in visited):
                    visited.add((i1, j1))
                    dfs(i1, j1, cur)
                    visited.discard((i1, j1))
                    end = False
            if end:
                self.res = max(self.res, cur)
            return
        (m, n) = (len(grid), len(grid[0]))
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    visited = set([(i, j)])
                    dfs(i, j, 0)
        return self.res
