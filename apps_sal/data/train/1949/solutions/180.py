class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        x = [0, 1, 0, -1]
        y = [1, 0, -1, 0]
        (m, n) = (len(grid), len(grid[0]))
        ans = -math.inf
        visited = [[False for _ in range(n)] for _ in range(m)]

        def helper(cur, total):
            (curX, curY) = cur
            total += grid[curX][curY]
            visited[curX][curY] = True
            nonlocal ans
            ans = max(ans, total)
            for (dx, dy) in zip(x, y):
                (candX, candY) = (curX + dx, curY + dy)
                if 0 <= candX < m and 0 <= candY < n and grid[candX][candY] and (not visited[candX][candY]):
                    print(candX, candY)
                    helper([candX, candY], total)
            visited[curX][curY] = False
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    helper([r, c], 0)
        return ans
