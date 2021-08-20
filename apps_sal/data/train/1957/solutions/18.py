class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = collections.deque([(0, 0, 0, 0)])
        m = len(grid)
        n = len(grid[0])
        visited = {}
        visited[0, 0] = 0
        steps = 0
        while queue:
            (x, y, used_k, steps) = queue.popleft()
            if x == m - 1 and y == n - 1:
                return steps
            for (i, j) in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                (nx, ny) = (x + i, y + j)
                if 0 <= nx < m and 0 <= ny < n:
                    if visited.get((nx, ny), float('inf')) <= used_k:
                        continue
                    if used_k >= k:
                        if grid[nx][ny] == 1:
                            continue
                        else:
                            visited[nx, ny] = used_k
                            queue.append([nx, ny, used_k, steps + 1])
                    elif grid[nx][ny] == 1:
                        visited[nx, ny] = used_k + 1
                        queue.append([nx, ny, used_k + 1, steps + 1])
                    else:
                        visited[nx, ny] = used_k
                        queue.append([nx, ny, used_k, steps + 1])
        return -1
