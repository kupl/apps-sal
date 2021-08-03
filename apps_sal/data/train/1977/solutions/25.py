class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(x, y):
            grid[x][y] = 1
            for dx, dy in moves:
                if 0 <= x + dx < M and 0 <= y + dy < N and grid[x + dx][y + dy] == 0:
                    dfs(x + dx, y + dy)

        # eliminate outer islands
        for i in range(M):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][N - 1] == 0:
                dfs(i, N - 1)
        for j in range(N):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[M - 1][j] == 0:
                dfs(M - 1, j)
        # count ans
        ans = 0
        for i in range(1, M - 1):
            for j in range(1, N - 1):
                if grid[i][j] == 0:
                    ans += 1
                    dfs(i, j)
        return ans
