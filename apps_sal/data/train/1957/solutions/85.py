class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = collections.deque([(0, 0, k)])
        m, n = len(grid), len(grid[0])
        step = 0
        visited = set()
        while q:
            nq = collections.deque()

            while q:
                x, y, curk = q.popleft()
                visited.add((x, y, curk))
                if x == m - 1 and y == n - 1:
                    return step
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if grid[nx][ny] == 1 and curk - 1 >= 0 and (nx, ny, curk - 1) not in visited:
                        nq.append((nx, ny, curk - 1))
                        visited.add((nx, ny, curk - 1))
                    elif grid[nx][ny] == 0 and (nx, ny, curk) not in visited:
                        nq.append((nx, ny, curk))
                        visited.add((nx, ny, curk))
                    # if grid[nx][ny] == 0:
                    #     if (nx, ny, curk) not in visited:
                    #         # visited.add((nx, ny, curk))
                    #         nq.append((nx, ny, curk))
                    # elif curk > 0:
                    #     if (nx, ny, curk) not in visited:
                    #         # visited.add((nx, ny, curk))
                    #         nq.append((nx, ny, curk-1))
            # print(nq)
            step += 1
            q = nq
        return -1
