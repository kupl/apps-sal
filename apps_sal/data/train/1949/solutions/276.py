class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m = len(grid) - 1
        n = len(grid[0]) - 1

        def dfs(i, j, visited):

            val = 0
            visited[i][j] = True

            for co in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x = i + co[0]
                y = j + co[1]

                if 0 <= x <= m and 0 <= y <= n and grid[x][y] != 0 and visited[x][y] == False:
                    val = max(val, dfs(x, y, visited))

            visited[i][j] = False
            return val + grid[i][j]

        vis = [[False] * (n + 1) for _ in range(m + 1)]

        res = 0
        for i in range(m + 1):
            for j in range(n + 1):

                if grid[i][j] != 0:
                    res = max(res, dfs(i, j, vis))

        return res
