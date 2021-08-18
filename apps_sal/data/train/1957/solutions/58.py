class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = [(0, 0, k)]
        step = 0
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = {(0, 0, k)}
        if n == 1 and m == 1:
            return 0
        while queue:
            tmp = queue
            queue = []
            for i, j, eliminate in tmp:
                for d in ds:
                    x = i + d[0]
                    y = j + d[1]
                    if x == n - 1 and y == m - 1:
                        return step + 1
                    if x >= 0 and x < n and y >= 0 and y < m:
                        if grid[x][y] == 0 and (x, y, eliminate) not in visited:
                            visited.add((x, y, eliminate))
                            queue.append((x, y, eliminate))
                        elif grid[x][y] == 1 and eliminate >= 1 and (x, y, eliminate - 1) not in visited:
                            visited.add((x, y, eliminate - 1))
                            queue.append((x, y, eliminate - 1))
            step += 1
        return -1
