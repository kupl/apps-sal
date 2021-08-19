class Solution:

    def dfs(self, grid, i, j, m, n):
        tmp = 0

        # print(self.visited)
        # base case
        if grid[i][j] == 0 or self.visited[i][j] == 1:
            return 0

        self.visited[i][j] = 1

        for x, y in self.direction:
            x = i + x
            y = j + y
            if x >= 0 and y >= 0 and x < m and y < n and grid[x][y] != 0 and self.visited[x][y] != 1:
                tmp = max(tmp, self.dfs(grid, x, y, m, n))

        self.visited[i][j] = 0
        return tmp + grid[i][j]

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        n = len(grid[0])
        self.visited = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(grid, i, j, m, n))
        return res
