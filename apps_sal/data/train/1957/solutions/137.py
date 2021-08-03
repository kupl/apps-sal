from collections import deque
import numpy as np


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dq = deque()
        cache = {}
        minStep = np.inf
        s = (0, 0, 0, 0)
        cache[s[:3]] = s[-1]
        dq.append(s)
        while dq:
            i, j, ob, step = dq.popleft()
            if i == m - 1 and j == n - 1:
                minStep = min(minStep, step)
                continue
            for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if x >= 0 and x < m and y >= 0 and y < n:
                    if ob + grid[x][y] > k or step + 1 > minStep:
                        continue
                    if (x, y, ob + grid[x][y]) not in cache or step + 1 < cache[(x, y, ob + grid[x][y])]:
                        dq.append((x, y, ob + grid[x][y], step + 1))
                        cache[(x, y, ob + grid[x][y])] = step + 1
        return -1 if minStep == np.inf else minStep

# This is a difficult problem, and illustrate well bfs, definitely need to review
# 1. Basic idea is to BFS the whole grid, state is actually i,j and number of obstacles removed, this state is the key and value is the steps taken so far
