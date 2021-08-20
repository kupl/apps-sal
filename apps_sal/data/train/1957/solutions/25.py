import collections


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (m, n) = (len(grid), len(grid[0]))
        queue = collections.deque()
        queue.append([0, 0, k, 0])
        visited = set((0, 0, k))
        while queue:
            (x, y, k, step) = queue.popleft()
            if x == m - 1 and y == n - 1:
                return step
            for (nx, ny) in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
                if 0 <= nx < m and 0 <= ny < n:
                    nk = k - grid[nx][ny]
                    if nk >= 0 and (not (nx, ny, nk) in visited):
                        visited.add((nx, ny, nk))
                        queue.append((nx, ny, nk, step + 1))
        return -1
