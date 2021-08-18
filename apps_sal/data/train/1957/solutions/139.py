from typing import *
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dis = [[[float('inf') for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]
        dis[0][0][0] = 0

        vis = [[[False for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]
        q = deque([(0, 0, k, 0)])
        vis[0][0][k] = True

        while q:
            x, y, remain_chance, d = q.popleft()
            if x == m - 1 and y == n - 1:
                return d
            dis[x][y][k] = d
            for x1, y1 in [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]:
                if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
                    continue
                if grid[x1][y1] == 1:
                    if remain_chance == 0:
                        continue
                    if vis[x1][y1][remain_chance - 1]:
                        continue
                    q.append((x1, y1, remain_chance - 1, d + 1))
                    vis[x1][y1][remain_chance - 1] = True
                else:
                    if vis[x1][y1][remain_chance]:
                        continue
                    q.append((x1, y1, remain_chance, d + 1))
                    vis[x1][y1][remain_chance] = True
        return -1
