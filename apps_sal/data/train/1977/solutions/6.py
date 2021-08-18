class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        output = 0

        def dfs(i, j):
            if i in range(row) and j in range(col):
                if grid[i][j] == 0:
                    grid[i][j] = 1

                    bot = dfs(i + 1, j)
                    top = dfs(i - 1, j)
                    right = dfs(i, j + 1)
                    left = dfs(i, j - 1)
                    return (bot and top and right and left)
                else:
                    return True
            else:
                return False

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        output += 1

        return output
