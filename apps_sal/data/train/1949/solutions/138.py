class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        p = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    p = max(p, self.dfs(grid, i, j, m, n))
        return p

    def dfs(self, grid, starti, startj, m, n):
        visited = [[0 for i in range(m)] for j in range(n)]
        return self.dfsUtil(grid, starti, startj, visited, m, n)

    def dfsUtil(self, grid, i, j, visited, m, n):
        ct = grid[i][j]
        k = 0
        if visited[i][j] == 0 and grid[i][j] != 0:
            visited[i][j] = 1
            neighbours = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
            for neighbour in neighbours:
                if neighbour[0] >= 0 and neighbour[0] < n and (neighbour[1] >= 0) and (neighbour[1] < m):
                    k = max(k, self.dfsUtil(grid, neighbour[0], neighbour[1], visited, m, n))
            visited[i][j] = 0
            return ct + k
        else:
            return 0
