from queue import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        def can_visit(grid, x, y, k, visited, queue, n_steps):
            if grid[x][y] == 0 or k > 0:
                if grid[x][y] > 0:
                    k -= 1
                if (x, y) not in visited or k > visited[x, y][0] or n_steps < visited[x, y][1]:
                    visited[x, y] = (k, n_steps)
                    queue.append((x, y, k, n_steps))
        rows = len(grid)
        cols = len(grid[0])
        x = 0
        y = 0
        queue = deque()
        visited = {}
        n_steps = 0
        visited[x, y] = (k, n_steps)
        queue.append((x, y, k, n_steps))
        min_steps = float(inf)
        while len(queue) > 0:
            (x, y, k_remaining, n_steps) = queue.popleft()
            if x == rows - 1 and y == cols - 1:
                min_steps = min(n_steps, min_steps)
            n_steps += 1
            if x > 0:
                left_x = x - 1
                can_visit(grid, left_x, y, k_remaining, visited, queue, n_steps)
            if y > 0:
                down_y = y - 1
                can_visit(grid, x, down_y, k_remaining, visited, queue, n_steps)
            if x < rows - 1:
                right_x = x + 1
                can_visit(grid, right_x, y, k_remaining, visited, queue, n_steps)
            if y < cols - 1:
                up_y = y + 1
                can_visit(grid, x, up_y, k_remaining, visited, queue, n_steps)
        return min_steps if min_steps != inf else -1
