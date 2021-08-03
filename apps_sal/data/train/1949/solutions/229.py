class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def DFS(i, j, sum):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] == 0 or (i, j) in visited:
                return sum
            visited.add((i, j))
            maxi = 0
            for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                maxi = max(maxi, DFS(x, y, sum + grid[i][j]))
            visited.remove((i, j))
            return maxi

        return max(DFS(i, j, 0) for i in range(m) for j in range(n) if grid[i][j] != 0)
