class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        dp = [[(0, 0) for _ in range(ncols)] for _ in range(nrows)]

        cum_visited = set()
        isl_no = 1
        maxsize = 0
        for r in range(nrows):
            for c in range(ncols):
                if (r, c) not in cum_visited and grid[r][c] == 1:
                    visited = set()
                    self.dfs(grid, r, c, visited)
                    size = len(visited)
                    maxsize = max(maxsize, size)
                    for x, y in visited:
                        dp[x][y] = (isl_no, size)
                    cum_visited = cum_visited.union(visited)
                    isl_no += 1
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 0:
                    sz = self.join_zero(grid, dp, r, c)
                    maxsize = max(maxsize, sz)
        return maxsize

    def join_zero(self, grid, dp, r, c):
        islands = set()
        for nr, nc in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and dp[nr][nc][1] != 0:
                islands.add(dp[nr][nc])
        if len(islands) == 0:
            return 1

        return sum(x[1] for x in islands) + 1

    def dfs(self, grid, r, c, visited):
        visited.add((r, c))
        for n_r, n_c in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
            if n_r >= 0 and n_r < len(grid) and n_c >= 0 and n_c < len(grid[0]) and grid[n_r][n_c] == 1 and (n_r, n_c) not in visited:
                self.dfs(grid, n_r, n_c, visited)
