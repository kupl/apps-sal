from collections import deque


class Solution:
    dx = [1, 0]
    dy = [0, 1]

    def minimumMoves(self, grid: List[List[int]]) -> int:
        visit = set()
        q = deque()
        n = len(grid)
        answer = float('inf')
        init_pos = [0, 0, 0, 1, 1, 0]
        q.append(init_pos)

        while q:
            x1, y1, x2, y2, is_horizon, cost = q.popleft()
            if cost >= 20:
                print((x1, y1, x2, y2, is_horizon, cost))

            if is_horizon and x1 == n - 1 and x2 == n - 1 and y2 == n - 1 and y1 == n - 2:
                answer = min(answer, cost)

            visit.add(((x1, y1), (x2, y2)))

            for i in range(2):
                nx1 = x1 + self.dx[i]
                ny1 = y1 + self.dy[i]
                nx2 = x2 + self.dx[i]
                ny2 = y2 + self.dy[i]

                if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n and grid[nx1][ny1] == 0 and grid[nx2][ny2] == 0:
                    if ((nx1, ny1), (nx2, ny2)) not in visit:
                        nxt_hrizon = 1 if nx1 == nx2 else 0
                        visit.add(((nx1, ny1), (nx2, ny2)))
                        q.append([nx1, ny1, nx2, ny2, nxt_hrizon, cost + 1])
            if is_horizon:
                if x1 < n - 1 and grid[x1 + 1][y1] == 0 and grid[x2 + 1][y2] == 0:
                    if ((x1, y1), (x2 + 1, y2 - 1)) not in visit:
                        visit.add(((x1, y1), (x2 + 1, y2 - 1)))
                        q.append([x1, y1, x2 + 1, y2 - 1, 0, cost + 1])

            else:
                if y1 < n - 1 and grid[x1][y1 + 1] == 0 and grid[x2][y2 + 1] == 0:
                    if ((x1, y1), (x2 - 1, y2 + 1)) not in visit:
                        visit.add(((x1, y1), (x2 - 1, y2 + 1)))
                        q.append([x1, y1, x2 - 1, y2 + 1, 1, cost + 1])
        if answer != float('inf'):
            return answer
        else:
            return -1
