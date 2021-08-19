class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        (row, col) = (len(grid), len(grid[0]))
        maxgold = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def collectgold(r, c, path, tot):
            nonlocal maxgold
            tot += grid[r][c]
            if tot > maxgold:
                maxgold = tot
            for (x, y) in directions:
                if 0 <= r + x < row and 0 <= c + y < col and ((r + x, c + y) not in path) and grid[r + x][c + y]:
                    collectgold(r + x, c + y, path + [(r + x, c + y)], tot)
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    collectgold(i, j, [(i, j)], 0)
        return maxgold
