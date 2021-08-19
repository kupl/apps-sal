from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (m, n) = (len(grid), len(grid[0]))
        queue = deque([(0, 0, 0)])
        seen = set([(0, 0, 0)])
        nsteps = -1
        while queue:
            levelSize = len(queue)
            nsteps += 1
            for _ in range(levelSize):
                (i, j, t) = queue.popleft()
                if i == m - 1 and j == n - 1:
                    return nsteps
                for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n:
                        is_obs = grid[x][y] == 1
                        q = t + int(is_obs)
                        if q <= k and (x, y, q) not in seen:
                            queue.append((x, y, q))
                            seen.add((x, y, q))
        return -1
