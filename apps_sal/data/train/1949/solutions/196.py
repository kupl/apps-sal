class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def bfs(i, j, path):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in path:
                return 0
            return grid[i][j] + max([bfs(i - 1, j, path + [(i, j)]),
                                     bfs(i + 1, j, path + [(i, j)]),
                                     bfs(i, j - 1, path + [(i, j)]),
                                     bfs(i, j + 1, path + [(i, j)])])

        maxval = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    path = []
                    val = bfs(i, j, path)
                    if maxval is None or val > maxval:
                        maxval = val
        return maxval
