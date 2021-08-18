class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        start = end = cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] != -1:
                    cnt += 1
        ans = 0

        def dfs(x, y, cnt):
            nonlocal ans, start, end
            if not (0 <= x < m and 0 <= y < n and grid[x][y] != -1):
                return
            if (x, y) == end and cnt == 1:
                ans += 1
                return
            val = grid[x][y]
            grid[x][y] = -1
            for i, j in map(lambda t: (t[0] + x, t[1] + y), [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                dfs(i, j, cnt - 1)
            grid[x][y] = val
        dfs(*start, cnt)
        return ans
