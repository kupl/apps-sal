class Solution:
    def __init__(self):
        self.EMPTY = 0
        self.DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_gold = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != self.EMPTY:
                    visited = set()
                    visited.add((i, j))
                    max_gold = max(max_gold, self.dfs(grid, i, j, visited))

        return max_gold

    def dfs(self, grid, i, j, visited):
        gold = 0

        for delta_i, delta_j in self.DIR:
            next_i, next_j = i + delta_i, j + delta_j

            if not self.inbound(grid, next_i, next_j) or (next_i, next_j) in visited or grid[next_i][next_j] == self.EMPTY:
                continue

            visited.add((next_i, next_j))
            gold = max(gold, self.dfs(grid, next_i, next_j, visited))
            visited.discard((next_i, next_j))

        return gold + grid[i][j]

    def inbound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
