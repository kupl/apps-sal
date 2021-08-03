class Solution:
    from collections import deque

    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        D = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        Q = deque([])
        Q.append((0, 0, k, 0))
        visited = set()

        while(Q):
            x, y, rem, lv = Q.popleft()
            if x == m - 1 and y == n - 1:
                return lv
            for dx, dy in D:
                if 0 <= x + dx < m and 0 <= y + dy < n and (x + dx, y + dy, rem) not in visited:
                    visited.add((x + dx, y + dy, rem))
                    if grid[x + dx][y + dy] == 0:
                        Q.append((x + dx, y + dy, rem, lv + 1))
                    elif grid[x + dx][y + dy] == 1 and rem > 0:
                        Q.append((x + dx, y + dy, rem - 1, lv + 1))
        return -1
