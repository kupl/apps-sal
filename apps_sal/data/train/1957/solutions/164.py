class Solution:
    def shortestPath(self, grid, k: int) -> int:
        m, n = len(grid), len(grid[0])
        num_obs, obs = 0, {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:

                    num_obs += 1
        if num_obs <= k:
            return m + n - 2
        q = [(0, 0, 0, k)]
        visited = set()
        while q:
            l = len(q)
            for _ in range(l):
                step, i, j, rem = q.pop(0)
                if i == m - 1 and j == n - 1:
                    return step
                if (i, j, rem) in visited:
                    continue
                visited.add((i, j, rem))
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 0:
                            q.append((step + 1, x, y, rem))
                        elif grid[x][y] == 1 and rem > 0:
                            q.append((step + 1, x, y, rem - 1))
        return -1
