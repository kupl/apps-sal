class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        steps, min_steps = 0, rows + cols - 2
        if k >= min_steps - 1:
            return min_steps

        visited = [[-1] * cols for _ in range(rows)]
        visited[0][0] = k
        q = deque([(0, 0, k)])
        while q:
            steps += 1
            prev_min = min_steps
            for _ in range(len(q)):
                r, c, p = q.popleft()
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    x, y = c + dx, r + dy
                    if x < 0 or x >= cols or y < 0 or y >= rows:
                        continue
                    kk = p - grid[y][x]
                    if kk <= visited[y][x]:
                        continue
                    to_target = rows - y + cols - x - 2
                    if kk >= to_target - 1 and visited[y][x] == -1:
                        return steps + to_target
                    q.append((y, x, kk))
                    visited[y][x] = kk
                    min_steps = min(min_steps, to_target)
        return -1
