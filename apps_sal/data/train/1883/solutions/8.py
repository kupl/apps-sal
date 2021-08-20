class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def dfs(i, j, out, to_visit):
            if i < 0 or j < 0 or i >= len(grid) or (j >= len(grid[0])) or (grid[i][j] == '#') or (grid[i][j] == -1):
                return
            if grid[i][j] == 2 and to_visit == 0:
                out[0] += 1
            else:
                tmp = grid[i][j]
                grid[i][j] = '#'
                dfs(i, j + 1, out, to_visit - 1)
                dfs(i, j - 1, out, to_visit - 1)
                dfs(i + 1, j, out, to_visit - 1)
                dfs(i - 1, j, out, to_visit - 1)
                grid[i][j] = tmp
        res = [0]
        (ori, orj) = (0, 0)
        to_visit = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    (ori, orj) = (i, j)
                if grid[i][j] != -1:
                    to_visit += 1
        dfs(ori, orj, res, to_visit - 1)
        return res[0]
