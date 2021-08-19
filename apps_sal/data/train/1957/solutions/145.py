from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return 0
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        (m, n) = (len(grid), len(grid[0]))
        queue = deque([(0, 0, 0, k)])
        visited = set()
        visited.add((0, 0, k))
        direction = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        while queue:
            (cur_x, cur_y, cur_count, cur_k) = queue.popleft()
            for (i, j) in direction:
                next_x = cur_x + i
                next_y = cur_y + j
                if 0 <= next_x < m and 0 <= next_y < n:
                    if grid[next_x][next_y] == 1 and cur_k > 0 and ((next_x, next_y, cur_k - 1) not in visited):
                        visited.add((next_x, next_y, cur_k - 1))
                        queue.append((next_x, next_y, cur_count + 1, cur_k - 1))
                    if grid[next_x][next_y] == 0 and (next_x, next_y, cur_k) not in visited:
                        if next_x == m - 1 and next_y == n - 1:
                            return cur_count + 1
                        visited.add((next_x, next_y, cur_k))
                        queue.append((next_x, next_y, cur_count + 1, cur_k))
        return -1
