from collections import deque
from heapq import heappush
from heapq import heappop
_DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
        (m, n) = (len(grid), len(grid[0]))
        if k >= m + n - 2:
            return m + n - 2
        queue = []
        visited = set()
        queue.append((0, k, 0, 0))
        visited.add((0, 0, k))
        while queue:
            (cost, ck, ci, cj) = heappop(queue)
            if (ci, cj) == (m - 1, n - 1):
                return cost
            for (di, dj) in _DIRS:
                (newi, newj) = (ci + di, cj + dj)
                if not 0 <= newi < m or not 0 <= newj < n:
                    continue
                if grid[newi][newj] == 1 and ck > 0 and ((newi, newj, ck - 1) not in visited):
                    heappush(queue, (cost + 1, ck - 1, newi, newj))
                    visited.add((newi, newj, ck - 1))
                if grid[newi][newj] == 0 and (newi, newj, ck) not in visited:
                    heappush(queue, (cost + 1, ck, newi, newj))
                    visited.add((newi, newj, ck))
        return -1
