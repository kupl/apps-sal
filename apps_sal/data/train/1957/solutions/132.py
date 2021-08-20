class Solution:

    def shortestPath(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        q = [(0, 0, 0, 0)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set((0, 0, 0))
        i = j = obs = 0
        while q:
            (x, y, obs, steps) = q.pop(0)
            if x == m - 1 and y == n - 1:
                return steps
            for (dx, dy) in dirs:
                i = x + dx
                j = y + dy
                if 0 <= i < m and 0 <= j < n:
                    newObs = obs + grid[i][j]
                    if newObs <= k and (i, j, newObs) not in visited:
                        q.append((i, j, newObs, steps + 1))
                        visited.add((i, j, newObs))
        return -1
