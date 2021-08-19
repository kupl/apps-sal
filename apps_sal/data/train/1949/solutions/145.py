class Solution:

    def getNeighbors(self, root, grid):
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        (x, y) = root
        return [(x + dx, y + dy) for (dx, dy) in deltas if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[x])]

    def dfs(self, root, grid, visited):
        if root in visited:
            return 0
        visited.add(root)
        gold = 0
        for (nx, ny) in self.getNeighbors(root, grid):
            if (nx, ny) in visited:
                continue
            if grid[nx][ny] == 0:
                continue
            gold = max(gold, self.dfs((nx, ny), grid, visited))
        visited.remove(root)
        return gold + grid[root[0]][root[1]]

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                maxGold = max(maxGold, self.dfs((i, j), grid, set()))
        return maxGold


[[0, 0, 19, 5, 8], [11, 20, 14, 1, 0], [0, 0, 1, 1, 1], [0, 2, 0, 2, 0]]
