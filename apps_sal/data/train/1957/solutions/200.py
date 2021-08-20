from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M = len(grid)
        N = len(grid[0])
        visited = set()
        q = deque([(0, 0, k, 0)])
        while q:
            data = q.popleft()
            (x, y) = (data[0], data[1])
            k = data[2]
            if (x, y, k) not in visited:
                visited.add((x, y, k))
                if x == M - 1 and y == N - 1:
                    return data[3]
                k = data[2]
                steps = data[3]
                for (i, j) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    if 0 <= x + i < M and 0 <= y + j < N:
                        if grid[x + i][y + j] == 1:
                            if k >= 1:
                                q.append((x + i, y + j, k - 1, steps + 1))
                        else:
                            q.append((x + i, y + j, k, steps + 1))
        return -1
