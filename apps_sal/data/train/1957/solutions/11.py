from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        if k > (len(grid) - 1 + len(grid[0]) - 1):
            return len(grid) - 1 + len(grid[0]) - 1
        queue = deque([(0, 0, k, 0)])
        visited = set((0, 0, k))
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue:
            row, col, k, step = queue.popleft()
            for d in directions:
                x = row + d[0]
                y = col + d[1]
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                    if grid[x][y] == 1 and k > 0 and (x, y, k - 1) not in visited:
                        if x == len(grid) - 1 and y == len(grid[0]) - 1:
                            return step + 1
                        visited.add((x, y, k - 1))
                        queue.append((x, y, k - 1, step + 1))
                    if grid[x][y] == 0 and (x, y, k) not in visited:
                        if x == len(grid) - 1 and y == len(grid[0]) - 1:
                            return step + 1
                        visited.add((x, y, k))
                        queue.append((x, y, k, step + 1))
        return -1
