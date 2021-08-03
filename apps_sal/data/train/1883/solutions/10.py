class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = end = None
        cnt = ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 1:
                    end = (i, j)
                if grid[i][j] != -1:
                    cnt += 1

        def dfs(i, j, cnt):
            nonlocal m, n, ans
            if grid[i][j] == 2 and cnt == 1:
                ans += 1
                return
            val = grid[i][j]
            grid[i][j] = -1
            for x, y in map(lambda t: (t[0] + i, t[1] + j), [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                if 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                    dfs(x, y, cnt - 1)
            grid[i][j] = val
        dfs(*start, cnt)
        return ans
