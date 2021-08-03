class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        d = deque([(0, 0, k)])
        visited = {(0, 0, k)}

        def get_neigbour(x, y, z):
            for x0, y0 in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= x0 < m and 0 <= y0 < n:
                    z0 = z - grid[x0][y0]
                    if z0 >= 0:
                        yield (x0, y0, z0)
        steps = 0

        while d:
            size = len(d)
            for i in range(size):
                x, y, z = d.popleft()
                if (x, y) == (m - 1, n - 1):
                    return steps
                for nxt in get_neigbour(x, y, z):
                    if nxt in visited:
                        continue
                    visited.add(nxt)
                    d.append(nxt)
            steps += 1
        return -1
