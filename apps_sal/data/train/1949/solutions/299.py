class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x, y, total):
            nonlocal maxTotal, visited
            maxTotal = max(maxTotal, total)
            visited.add((x, y))

            for move in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
                i = x + move[0]
                j = y + move[1]

                if 0 <= i < n and 0 <= j < m and grid[i][j] and (i, j) not in visited:
                    dfs(i, j, total + grid[i][j])

            visited.remove((x, y))

        if not grid or not grid[0]:
            return 0

        n = len(grid)
        m = len(grid[0])
        result = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    maxTotal = 0
                    visited = set()
                    dfs(i, j, grid[i][j])

                    if maxTotal > result:
                        result = maxTotal

        return result
