class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def nextPos(r, c):
            if r > 0:
                yield (r - 1, c)
            if r < m - 1:
                yield (r + 1, c)
            if c > 0:
                yield (r, c - 1)
            if c < n - 1:
                yield (r, c + 1)
        self.mx = 0

        def backtrack(r, c, visited, gold):
            self.mx = max(self.mx, gold)
            for (nr, nc) in nextPos(r, c):
                if not visited[nr][nc] and grid[nr][nc] > 0:
                    gold += grid[nr][nc]
                    visited[nr][nc] = True
                    backtrack(nr, nc, visited, gold)
                    gold -= grid[nr][nc]
                    visited[nr][nc] = False
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                visited = [[False for _ in range(n)] for _ in range(m)]
                visited[i][j] = True
                if grid[i][j] > 0:
                    backtrack(i, j, visited, grid[i][j])
        return self.mx
