class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # _grid = [grid[i][:] for i in range(len(grid))]
        m, n = len(grid), len(grid[0])
        self.res = 0
        def helper(r, c, grid, acc):
            acc += grid[r][c]
            self.res = max(self.res, acc)
            temp, grid[r][c] = grid[r][c], 0
            for ir, ic in [[-1,0],[0,-1],[1,0],[0,1]]:
                if 0 <= r+ir < m and 0 <= c+ic < n and grid[r+ir][c+ic] > 0:
                    helper(r+ir, c+ic, grid, acc)
            grid[r][c] = temp
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    helper(i,j,grid,0)
        return self.res
