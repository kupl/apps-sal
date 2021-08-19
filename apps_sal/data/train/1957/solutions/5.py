class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        # （steps, k left）
        m, n = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        queue = collections.deque([(0, 0, 0, k)])
        seen = set([(0, 0, k)])

        while queue:
            x, y, steps, k = queue.popleft()

            # exit immediatly when we see
            if x == m - 1 and y == n - 1:
                return steps

            for d in range(4):
                nxt_x, nxt_y = x + dx[d], y + dy[d]
                if (nxt_x, nxt_y, k) not in seen and nxt_x >= 0 and nxt_x < m and nxt_y >= 0 and nxt_y < n:
                    if grid[nxt_x][nxt_y] == 0:
                        queue.append((nxt_x, nxt_y, steps + 1, k))
                        seen.add((nxt_x, nxt_y, k))
                    else:
                        if k > 0 and (nxt_x, nxt_y, k - 1) not in seen:
                            queue.append((nxt_x, nxt_y, steps + 1, k - 1))
                            seen.add((nxt_x, nxt_y, k - 1))

        return -1
