class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        queue = deque([])
        m, n = len(grid), len(grid[0])
        start_point = (0, 0, 0) if grid[0][0] != 1 else (0, 0, 1)
        queue.append(start_point)
        step = 0
        seen = [[float(\"inf\")] * n for _ in range(m)]
        
        while len(queue) > 0:
            count = len(queue)
            for _ in range(count):
                x, y, obs = queue.popleft()
                if x == m - 1 and y == n - 1:
                    return step

                for next_x, next_y in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                    if 0 <= next_x < m and 0 <= next_y < n:
                        num_obs = obs + grid[next_x][next_y]
                        if num_obs >= seen[next_x][next_y] or num_obs > k:
                            continue
                        seen[next_x][next_y] = num_obs
                        queue.append((next_x, next_y, num_obs))
            step += 1

        return -1
        
        
