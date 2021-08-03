class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            res = grid[r][c]
            nxt = 0
            for ro, co in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + ro, c + co
                if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    nxt = max(nxt, dfs(nr, nc))
                    seen.remove((nr, nc))

            return res + nxt

        M, N = len(grid), len(grid[0])
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    seen = {(i, j)}
                    res = max(res, dfs(i, j))

        return res
