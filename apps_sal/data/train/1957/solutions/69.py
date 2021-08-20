from collections import defaultdict, deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        def getNei(x, y):
            for (dx, dy) in dirs:
                (xn, yn) = (x + dx, y + dy)
                if 0 <= xn < M and 0 <= yn < N:
                    yield (xn, yn)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        (M, N) = (len(grid), len(grid[0]))
        inf_num = float(inf)
        visited = [[[inf_num] * (k + 1) for _ in range(N)] for _ in range(M)]
        queue = deque([(0, 0, k, 0)])
        while queue:
            (i, j, kk, cost) = queue.popleft()
            if i == M - 1 and j == N - 1:
                return cost
            if visited[i][j][kk] < inf:
                continue
            visited[i][j][kk] = cost
            for (x, y) in getNei(i, j):
                if grid[x][y] == 1:
                    if kk > 0 and cost + 1 < visited[x][y][kk]:
                        queue.append((x, y, kk - 1, cost + 1))
                elif cost + 1 < visited[x][y][kk]:
                    queue.append((x, y, kk, cost + 1))
        return -1
