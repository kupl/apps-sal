class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(i, j, total):
            if i < 0 or j < 0 or i >= m or (j >= n) or (grid[i][j] == 0) or (grid[i][j] > 100):
                return total
            total += grid[i][j]
            grid[i][j] += 1000
            temp_max = 0
            for (x, y) in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                temp_max = max(dfs(x, y, total), temp_max)
            grid[i][j] -= 1000
            return temp_max
        m = len(grid)
        n = len(grid[0])
        return max((dfs(i, j, 0) for i in range(m) for j in range(n)))
