class Solution:

    def minPushBox(self, grid) -> int:
        from collections import deque
        (r, c) = (len(grid), len(grid[0]))
        di = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(sx, sy, ex, ey, path):
            t = deque()
            s = set()
            s.add(str((sx, sy)))
            t.append([sx, sy])
            while t:
                (x, y) = t.popleft()
                if x == ex and y == ey:
                    return True
                for (i, j) in di:
                    ti = x + i
                    tj = y + j
                    if 0 <= ti < r and 0 <= tj < c and (path[ti][tj] == '.') and (str((ti, tj)) not in s):
                        s.add(str((ti, tj)))
                        t.append([ti, tj])
            return False
        bx = by = sx = sy = tx = ty = -1
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'B':
                    (bx, by) = (i, j)
                    grid[i][j] = '.'
                if grid[i][j] == 'S':
                    (sx, sy) = (i, j)
                    grid[i][j] = '.'
                if grid[i][j] == 'T':
                    (tx, ty) = (i, j)
                    grid[i][j] = '.'
        if -1 in [bx, by, sx, sy, tx, ty]:
            return -1
        t = deque()
        s = set()
        t.append([bx, by, sx, sy, 0])
        s.add(str((bx, by, sx, sy)))
        while t:
            (bx, by, sx, sy, step) = t.popleft()
            if bx == tx and by == ty:
                return step
            grid[bx][by] = 'B'
            for (i, j) in di:
                ti = bx + i
                tj = by + j
                tii = bx - i
                tjj = by - j
                if 0 <= ti < r and 0 <= tj < c and (grid[ti][tj] == '.') and (str((ti, tj, bx, by)) not in s) and (0 <= tii < r) and (0 <= tjj < c) and (grid[tii][tjj] == '.') and bfs(sx, sy, tii, tjj, grid):
                    t.append([ti, tj, bx, by, step + 1])
                    s.add(str((ti, tj, bx, by)))
            grid[bx][by] = '.'
        return -1
