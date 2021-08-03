from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def inBounds(x, y):
            if x < 0:
                return False
            elif y < 0:
                return False
            elif x >= len(grid[0]):
                return False
            elif y >= len(grid):
                return False

            return True

        target = (len(grid[0]) - 1, len(grid) - 1)

        queue = deque([(0, 0, k, 0)])

        visited = set([(0, 0, k)])

        if target == (0, 0):
            return 0

        while queue:
            x, y, k, dist = queue.popleft()

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (x + dx, y + dy) == target:
                    return dist + 1

                if not inBounds(x + dx, y + dy):
                    continue

                if grid[y + dy][x + dx] == 0 and (x + dx, y + dy, k) not in visited:
                    visited.add((x + dx, y + dy, k))
                    queue.append((x + dx, y + dy, k, dist + 1))
                elif k > 0 and (x + dx, y + dy, k - 1) not in visited:
                    visited.add((x + dx, y + dy, k - 1))
                    queue.append((x + dx, y + dy, k - 1, dist + 1))

        return -1
