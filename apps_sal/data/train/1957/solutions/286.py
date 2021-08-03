class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MAX_DIST = m * n

        shortest = MAX_DIST
        visited = set([])
        visited.add((m - 1, n - 1, k, 0))

        def dfs(i, j, k, steps):
            nonlocal shortest

            if (i, j) == (0, 0):
                shortest = min(shortest, steps)
                return

            if grid[i][j] == 1:
                k -= 1
                if k < 0:
                    return

            if grid[i][j] == 2:
                return

            if shortest <= steps + i + j:
                return

            grid[i][j], save = 2, grid[i][j]
            for x, y in (i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1):
                if m > x >= 0 <= y < n and (x, y, k, steps + 1) not in visited:
                    visited.add((x, y, k, steps + 1))
                    dfs(x, y, k, steps + 1)

            grid[i][j] = save

        dfs(m - 1, n - 1, k, 0)

        return shortest if shortest != MAX_DIST else -1
