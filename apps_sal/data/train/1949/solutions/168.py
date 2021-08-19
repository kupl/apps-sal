class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def dfs(i, j, gold, visited):
            nonlocal ans
            if i < 0 or i >= rows or j < 0 or (j >= cols) or ((i, j) in visited) or (grid[i][j] == 0):
                ans = max(ans, gold)
                return
            visited.add((i, j))
            for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + di, j + dj, gold + grid[i][j], visited)
            visited.remove((i, j))
        (ans, rows, cols) = (0, len(grid), len(grid[0]))
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, 0, set())
        return ans
