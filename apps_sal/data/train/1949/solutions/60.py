class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])

        def isValid(x, y):
            return 0 <= x < m and 0 <= y < n

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if grid[x][y] == 0:
                return 0
            visited.add((x, y))
            ans = 0
            for dx, dy in dirs:
                if isValid(x + dx, y + dy) and (x + dx, y + dy) not in visited:
                    ans = max(ans, dfs(x + dx, y + dy))
            visited.remove((x, y))
            return ans + grid[x][y]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
