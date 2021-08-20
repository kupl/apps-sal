class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        if m - 1 == 0 and n - 1 == 0 and (grid[0][0] == 0):
            return 0
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited.add((0, 0, 0))
        queue = [(0, 0, 0, 0)]
        while queue:
            (lvl, out, x, y) = queue.pop(0)
            for (dx, dy) in directions:
                if x + dx < 0 or y + dy < 0 or x + dx >= m or (y + dy >= n):
                    continue
                if x + dx == m - 1 and y + dy == n - 1:
                    return lvl + 1
                if grid[x + dx][y + dy] == 0 and (out, x + dx, y + dy) not in visited:
                    visited.add((out, x + dx, y + dy))
                    queue.append((lvl + 1, out, x + dx, y + dy))
                if grid[x + dx][y + dy] == 1 and out < k and ((out + 1, x + dx, y + dy) not in visited):
                    visited.add((out + 1, x + dx, y + dy))
                    queue.append((lvl + 1, out + 1, x + dx, y + dy))
        return -1
