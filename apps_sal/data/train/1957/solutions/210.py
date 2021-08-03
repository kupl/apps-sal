import queue


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == n and n == 1:
            return 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = queue.Queue()
        q.put(((0, 0), 0, k))
        vis = set()
        vis.add((0, 0, k))
        while not q.empty():
            (x, y), dist, rem = q.get()
            for d in dirs:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny, rem) in vis:
                        continue
                    if (nx, ny) == (m - 1, n - 1):
                        return dist + 1
                    if grid[nx][ny] == 0:
                        q.put(((nx, ny), dist + 1, rem))
                    elif rem > 0:
                        q.put(((nx, ny), dist + 1, rem - 1))
                    vis.add((nx, ny, rem))
        return -1

    def shortestPath1(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = queue.Queue()
        q.put(((0, 0), 0))
        while not q.empty():
            (x, y), dist = q.get()
            for d in dirs:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) == (m - 1, n - 1):
                        return dist + 1
                    if grid[nx][ny] == 0:
                        q.put(((nx, ny), dist + 1))
        return -1
