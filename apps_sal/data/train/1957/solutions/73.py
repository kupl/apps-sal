from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] == 1:
            k -= 1
        q = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])
        while len(q) > 0:
            (r, c, avail, path) = q.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return path
            for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                (nr, nc) = (r + dr, c + dc)
                if nr < 0 or nr >= len(grid) or nc < 0 or (nc >= len(grid[0])):
                    continue
                if grid[nr][nc] == 1 and (not avail):
                    continue
                if (nr, nc, avail) in visited:
                    continue
                visited.add((nr, nc, avail))
                if grid[nr][nc] == 0:
                    q.append((nr, nc, avail, path + 1))
                elif avail > 0:
                    q.append((nr, nc, avail - 1, path + 1))
        return -1
