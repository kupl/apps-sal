class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(r, c, n):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == -1:
                return 0
            if grid[r][c] == 2:
                return n == 0
            grid[r][c] = -1
            paths = dfs(r + 1, c, n - 1) + dfs(r - 1, c, n - 1) + dfs(r, c + 1, n - 1) + dfs(r, c - 1, n - 1)
            grid[r][c] = 0
            return paths
        
        R = len(grid)
        C = len(grid[0])
        n = 1
        sr, sc = -1, -1
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    n += 1
                elif grid[r][c] == 1:
                    sr, sc = r, c
        
        return dfs(sr, sc, n)

