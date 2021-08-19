class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = collections.deque()
        queue.append((0, 0, 0, k))
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()
        while queue:
            (x, y, level, k) = queue.popleft()
            if x == m - 1 and y == n - 1:
                return level
            if (x, y, k) in visited:
                continue
            visited.add((x, y, k))
            for (dx, dy) in dirs:
                xx = x + dx
                yy = y + dy
                if xx < 0 or xx >= m or yy < 0 or (yy >= n):
                    continue
                if grid[xx][yy] == 0:
                    queue.append((xx, yy, level + 1, k))
                elif k > 0:
                    queue.append((xx, yy, level + 1, k - 1))
        return -1
