from collections import deque
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque([(0, 0, k)])
        visited = set([(0, 0, k)])
        step = 0
        while dq:
            size = len(dq)
            for i in range(size):
                r, c, p = dq.popleft()
                if r == m - 1 and c == n - 1:
                    return step
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if not (0 <= nr < m) or not (0 <= nc < n):
                        continue
                    elif grid[nr][nc] == 0:
                        if (nr, nc, p) not in visited:
                            visited.add((nr, nc, p))
                            dq.append((nr, nc, p))
                    elif grid[nr][nc] == 1:
                        if p > 0 and (nr, nc, p - 1) not in visited:
                            visited.add((nr, nc, p - 1))
                            dq.append((nr, nc, p - 1))
            step += 1
        return -1
