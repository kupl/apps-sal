class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        (r, c) = (len(grid), len(grid[0]))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        q = [(0, 0, 0, k)]
        visited.add((0, 0, 0))
        while q:
            (x, y, steps, obs) = q.pop(0)
            if obs < 0:
                continue
            if x == r - 1 and y == c - 1:
                return steps
            for (dx, dy) in dirs:
                (nx, ny) = (x + dx, y + dy)
                if 0 <= nx < r and 0 <= ny < c and (grid[nx][ny] == 0):
                    if (nx, ny, obs) not in visited:
                        q.append((nx, ny, steps + 1, obs))
                        visited.add((nx, ny, obs))
                elif 0 <= nx < r and 0 <= ny < c and (grid[nx][ny] == 1):
                    if obs > 0:
                        if (nx, ny, obs - 1) not in visited:
                            q.append((nx, ny, steps + 1, obs - 1))
                            visited.add((nx, ny, obs - 1))
        return -1
