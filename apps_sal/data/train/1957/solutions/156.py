from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        queue = deque([(0, 0, k, 0)])
        visited = set((0, 0, k))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            row, col, elim, steps = queue.popleft()

            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if (new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0])):
                    continue
                if grid[new_row][new_col] == 1 and elim > 0 and (new_row, new_col, elim - 1) not in visited:
                    queue.append((new_row, new_col, elim - 1, steps + 1))
                    visited.add((new_row, new_col, elim - 1))
                if grid[new_row][new_col] == 0 and (new_row, new_col, elim) not in visited:
                    if new_row == len(grid) - 1 and new_col == len(grid[0]) - 1:
                        return steps + 1
                    queue.append((new_row, new_col, elim, steps + 1))
                    visited.add((new_row, new_col, elim))

        return -1
