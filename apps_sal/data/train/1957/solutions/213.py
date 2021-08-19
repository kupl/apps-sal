class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (m, n) = (len(grid), len(grid[0]))
        queue = collections.deque([(0, 0, k, 0)])
        visited = set()
        visited.add((0, 0, k))
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if m == 1 and n == 1:
            return 0
        while queue:
            (row, col, remain, steps) = queue.popleft()
            for (x, y) in dirs:
                (new_row, new_col) = (row + x, col + y)
                if 0 <= new_row < m and 0 <= new_col < n:
                    if remain > 0 and grid[new_row][new_col] == 1 and ((new_row, new_col, remain + 1) not in visited):
                        queue.append((new_row, new_col, remain - 1, steps + 1))
                        visited.add((new_row, new_col, remain - 1))
                    if grid[new_row][new_col] == 0 and (new_row, new_col, remain) not in visited:
                        if new_row == m - 1 and new_col == n - 1:
                            return steps + 1
                        else:
                            queue.append((new_row, new_col, remain, steps + 1))
                            visited.add((new_row, new_col, remain))
        return -1
