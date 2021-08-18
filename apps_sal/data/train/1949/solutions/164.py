class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j, sum):
            if i < 0 or i == m or j < 0 or j == n or (i, j) in visited or grid[i][j] == 0:
                return sum
            visited.add((i, j))
            maxi = 0
            for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                maxi = max(maxi, dfs(x, y, sum + grid[i][j]))
            visited.remove((i, j))
            return maxi

        return max(dfs(i, j, 0) for i in range(m) for j in range(n) if grid[i][j] != 0)
