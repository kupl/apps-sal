import heapq


class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        (xb, yb, xs, ys, xt, yt) = (-1, -1, -1, -1, -1, -1)
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 'B':
                    (xb, yb) = (x, y)
                    grid[x][y] = '.'
                if grid[x][y] == 'S':
                    (xs, ys) = (x, y)
                    grid[x][y] = '.'
                if grid[x][y] == 'T':
                    (xt, yt) = (x, y)
                    grid[x][y] = '.'
        (q, seen) = ([(abs(xb - xt) + abs(yb - yt) + 0, 0, xb, yb, xs, ys)], set())
        while q:
            (h, d, xb, yb, xs, ys) = heapq.heappop(q)
            if (xb, yb) == (xt, yt):
                return d
            if (xb, yb, xs, ys) not in seen:
                seen.add((xb, yb, xs, ys))
                for (dx, dy) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    (xr, yr) = (xs + dx, ys + dy)
                    if 0 <= xr < m and 0 <= yr < n and (grid[xr][yr] == '.'):
                        if (xr, yr) == (xb, yb):
                            (xc, yc) = (xb + dx, yb + dy)
                            if 0 <= xc < m and 0 <= yc < n and (grid[xc][yc] == '.'):
                                heapq.heappush(q, (abs(xc - xt) + abs(yc - yt) + d + 1, d + 1, xc, yc, xr, yr))
                        else:
                            heapq.heappush(q, (h, d, xb, yb, xr, yr))
        return -1
