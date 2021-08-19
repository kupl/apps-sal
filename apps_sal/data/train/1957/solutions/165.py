import math
import collections
import heapq


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (m, n) = (len(grid), len(grid[0]))

        def neighbors(x, y):
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if x + dx >= 0 and x + dx < m and (y + dy >= 0) and (y + dy < n):
                    yield (x + dx, y + dy)
        bfs = collections.deque([(0, 0, 0, k)])
        visited = set()
        while bfs:
            (i, j, cost, rems) = bfs.popleft()
            if i == m - 1 and j == n - 1:
                return cost
            if (i, j, rems) in visited:
                continue
            visited.add((i, j, rems))
            for (x, y) in neighbors(i, j):
                if grid[x][y] == 1 and rems == 0:
                    continue
                if grid[x][y] == 1:
                    bfs.append((x, y, cost + 1, rems - 1))
                else:
                    bfs.append((x, y, cost + 1, rems))
        return -1
