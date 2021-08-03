class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.ans = 0
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                self.dfs(grid, r, c, grid[r][c], set([(r, c)]))

        return self.ans

    def dfs(self, g, r, c, tot, used):
        if tot > self.ans:
            self.ans = tot

        dirs = (0, 1), (1, 0), (0, -1), (-1, 0)
        R, C = len(g), len(g[0])

        for dr, dc in dirs:
            r2, c2 = r + dr, c + dc
            if not (0 <= r2 < R and 0 <= c2 < C):
                continue
            if (r2, c2) in used or g[r2][c2] == 0:
                continue
            used.add((r2, c2))
            self.dfs(g, r2, c2, tot + g[r2][c2], used)
            used.remove((r2, c2))
