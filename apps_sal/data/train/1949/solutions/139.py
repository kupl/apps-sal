class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def walk(grid, i, j):
            nonlocal m, n
            if not grid or i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] < 1:
                return 0
            g = []
            for k in range(m):
                g.append(grid[k][:])
            ans = grid[i][j]
            g[i][j] = 0
            ans += max(walk(g, i - 1, j), walk(g, i + 1, j), walk(g, i, j - 1), walk(g, i, j + 1))
            return ans
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, walk(grid, i, j))
        return ans
