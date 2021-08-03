class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def collect(x, y):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] != 0):
                return 0
            gold, grid[x][y] = grid[x][y], 0
            choices = [collect(x + i, y + j) for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]]
            grid[x][y] = gold

            return gold + max(choices)

        return max(collect(x, y) for x in range(m) for y in range(n))
