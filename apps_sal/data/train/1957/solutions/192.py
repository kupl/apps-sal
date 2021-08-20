class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (m, n) = (len(grid), len(grid[0]))
        queue = collections.deque([(0, 0, k, 0)])
        visited = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if m == 1 and n == 1:
            return 0
        while queue:
            (row, col, elim, steps) = queue.popleft()
            for (x, y) in dirs:
                (new_row, new_col) = (row + x, col + y)
                if 0 <= new_row < m and 0 <= new_col < n:
                    if grid[new_row][new_col] == 1 and elim > 0 and ((new_row, new_col, elim + 1) not in visited):
                        queue.append((new_row, new_col, elim - 1, steps + 1))
                        visited.add((new_row, new_col, elim - 1))
                    if grid[new_row][new_col] == 0 and (new_row, new_col, elim) not in visited:
                        if new_row == m - 1 and new_col == n - 1:
                            return steps + 1
                        else:
                            queue.append((new_row, new_col, elim, steps + 1))
                            visited.add((new_row, new_col, elim))
        return -1
