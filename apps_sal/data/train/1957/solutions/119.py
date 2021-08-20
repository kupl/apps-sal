from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rowlen = len(grid)
        collen = len(grid[0])
        visited = set()
        visited.add((0, 0, k))
        q = deque([(0, 0, k, 0)])

        def get_nexts(x, y):
            return [(nx, ny) for (nx, ny) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if 0 <= nx < rowlen and 0 <= ny < collen]
        while q:
            (x, y, k, path_count) = q.popleft()
            if (x, y) == (rowlen - 1, collen - 1):
                return path_count
            nexts = get_nexts(x, y)
            for (nx, ny) in nexts:
                if grid[nx][ny] == 1 and (not k):
                    continue
                if grid[nx][ny] == 1 and (nx, ny, k - 1) in visited:
                    continue
                if grid[nx][ny] == 0 and (nx, ny, k) in visited:
                    continue
                if grid[nx][ny] == 1:
                    visited.add((nx, ny, k - 1))
                    q.append((nx, ny, k - 1, path_count + 1))
                else:
                    if (nx, ny) == (rowlen - 1, collen - 1):
                        return path_count + 1
                    visited.add((nx, ny, k))
                    q.append((nx, ny, k, path_count + 1))
        return -1
