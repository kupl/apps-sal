from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = {}
        queue = deque()
        queue.append([0, 0])
        visited[(0, 0)] = 0
        step = 0
        offset = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            size = len(queue)
            while size:
                size -= 1
                x, y = queue.popleft()
                obs = visited[(x, y)]
                if x == m - 1 and y == n - 1:
                    return step

                for dx, dy in offset:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny):
                        n_obs = obs + grid[nx][ny]
                        if n_obs > k:
                            continue
                        if (nx, ny) in visited and n_obs < visited[(nx, ny)]:
                            visited[(nx, ny)] = n_obs
                            queue.append((nx, ny))
                        elif (nx, ny) not in visited:
                            visited[(nx, ny)] = n_obs
                            queue.append((nx, ny))

            step += 1

        return -1
