DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]


class Solution:
    def dfs(self, grid, i, j, memo):
        if memo[i][j]:
            return 0
        memo[i][j] = True
        gold = 0
        for direction in DIRECTIONS:
            x = i + direction[0]
            y = j + direction[1]
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] != 0:
                gold = max(gold, self.dfs(grid, x, y, memo))
        memo[i][j] = False
        return gold + grid[i][j]

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        max_gold = 0
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or visited[i][j]:
                    continue
                max_gold = max(max_gold, self.dfs(grid, i, j, visited))
        return max_gold
