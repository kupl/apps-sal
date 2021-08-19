class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'B':
                    b = (i, j)
                if grid[i][j] == 'S':
                    s = (i, j)
                if grid[i][j] == 'T':
                    t = (i, j)
        queue = [(b[0], b[1], s[0], s[1], 0)]
        dic = {(b[0], b[1], s[0], s[1]): 0}
        res = float('inf')
        while queue:
            bx, by, sx, sy, step = queue.pop(0)
            if dic[(bx, by, sx, sy)] >= res:
                continue
            if (bx, by) == t:
                res = min(res, step)
                continue
            for i in range(4):
                nsx = sx + dx[i]
                nsy = sy + dy[i]
                if not 0 <= nsx < n or not 0 <= nsy < m or grid[nsx][nsy] == '#':
                    continue
                if nsx == bx and nsy == by:
                    nbx = bx + dx[i]
                    nby = by + dy[i]
                    if (nbx, nby, nsx, nsy) in dic and dic[(nbx, nby, nsx, nsy)] <= step + 1:
                        continue
                    dic[(nbx, nby, nsx, nsy)] = step + 1
                    queue.append((nbx, nby, nsx, nsy, step + 1))
                else:
                    if (bx, by, nsx, nsy) in dic and dic[(bx, by, nsx, nsy)] <= step:
                        continue
                    dic[(bx, by, nsx, nsy)] = step
                    queue.append((bx, by, nsx, nsy, step))
        return res if res != float('inf') else -1
