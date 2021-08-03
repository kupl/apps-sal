class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        self.mx = 0
        seen = set()

        def dfs(r, c):
            if not 0 <= r < ROWS or not 0 <= c < COLS or (r, c) in seen or grid[r][c] == 0:
                return 0
            val = grid[r][c]
            seen.add((r, c))
            mx = max(dfs(r + 1, c), dfs(r - 1, c), dfs(r, c + 1), dfs(r, c - 1))
            seen.remove((r, c))
            return val + mx

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    self.mx = max(self.mx, dfs(r, c))
        return self.mx
