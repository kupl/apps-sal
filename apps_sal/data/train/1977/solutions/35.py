from collections import deque


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set()
        m, n = len(grid), len(grid[0])
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and grid[i][j] == 0:
                    curr_seen = {(i, j)}
                    q = deque([(i, j)])
                    closed = True
                    while q:
                        x, y = q.popleft()
                        curr_seen.add((x, y))
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            closed = False

                        for dx, dy in moves:
                            next_x, next_y = x + dx, y + dy
                            if 0 <= next_x < m and 0 <= next_y < n:
                                if grid[next_x][next_y] == 0:
                                    if (next_x, next_y) not in curr_seen:
                                        curr_seen.add((next_x, next_y))
                                        q.append((next_x, next_y))
                    if closed:
                        ans += 1
                    seen = seen | curr_seen
        return ans
