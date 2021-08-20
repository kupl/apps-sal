class Solution:

    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        (m, n) = (len(grid), len(grid[0]))
        islandId = 2
        areaDict = {}
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    areaDict[islandId] = self.dfs(grid, i, j, m, n, islandId)
                    maxArea = max(maxArea, areaDict[islandId])
                    islandId += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    neighborIslands = set()
                    for (ni, nj) in self.getNeighbors(grid, i, j, m, n):
                        if grid[ni][nj] > 0:
                            neighborIslands.add(grid[ni][nj])
                    maxArea = max(maxArea, 1 + sum([areaDict[islandId] for islandId in neighborIslands]))
        return maxArea

    def dfs(self, grid, i, j, m, n, islandId):
        area = 1
        grid[i][j] = islandId
        for (ni, nj) in self.getNeighbors(grid, i, j, m, n):
            if grid[ni][nj] != 1:
                continue
            area += self.dfs(grid, ni, nj, m, n, islandId)
        return area

    def bfs(self, grid, i, j, m, n, islandId):
        grid[i][j] = islandId
        area = 1
        q = [(i, j)]
        while q:
            (x, y) = q.pop(0)
            for (nx, ny) in self.getNeighbors(grid, x, y, m, n):
                if grid[nx][ny] != 1:
                    continue
                area += 1
                grid[nx][ny] = islandId
                q.append((nx, ny))
        return area

    def getNeighbors(self, grid, x, y, m, n):
        result = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [(a, b) for (a, b) in result if 0 <= a < m and 0 <= b < n and (grid[a][b] > 0)]
