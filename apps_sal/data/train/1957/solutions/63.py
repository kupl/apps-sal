from collections import deque
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque([(0, 0, k)])
        visited = set([(0, 0, k)])
        step = 0
        while dq:
            size = len(dq)
            for i in range(size):
                r, c, o = dq.popleft()  # o: remianing eliminate obstacle [o >= 0]
                if r == m - 1 and c == n - 1:
                    return step
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if not (0 <= nr < m) or not (0 <= nc < n):
                        continue
                    if grid[nr][nc] == 0:
                        if (nr, nc, o) not in visited:
                            dq.append((nr, nc, o))
                            visited.add((nr, nc, o))
                    elif grid[nr][nc] == 1:
                        if o > 0 and (nr, nc, o - 1) not in visited:
                            dq.append((nr, nc, o - 1))
                            visited.add((nr, nc, o - 1))
            step += 1
        return -1
