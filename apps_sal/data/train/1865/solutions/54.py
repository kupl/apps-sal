class Solution:

    def minPushBox(self, A: List[List[str]]) -> int:

        def reachable(sx, sy, tsx, tsy, bx, by, A, dirs):
            (m, n) = (len(A), len(A[0]))
            visited = [[0] * 20 for _ in range(20)]
            visited[sx][sy] = 1
            q = deque()
            q.append([sx, sy])
            while q:
                (sx, sy) = q.popleft()
                for (dx, dy) in dirs:
                    (nsx, nsy) = (sx + dx, sy + dy)
                    if 0 <= nsx < m and 0 <= nsy < n and (visited[nsx][nsy] == 0) and (A[nsx][nsy] in '.T' and [nsx, nsy] != [bx, by]):
                        if [nsx, nsy] == [tsx, tsy]:
                            return True
                        visited[nsx][nsy] = 1
                        q.append([nsx, nsy])
            return False
        (m, n) = (len(A), len(A[0]))
        for i in range(m):
            for j in range(n):
                if A[i][j] == 'B':
                    (bx, by) = (i, j)
                    A[i][j] = '.'
                if A[i][j] == 'S':
                    (sx, sy) = (i, j)
                    A[i][j] = '.'
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = [[0] * 400 for _ in range(400)]
        visited[bx * 20 + by][sx * 20 + sy] = 1
        q = deque()
        q.append([bx, by, sx, sy, 0])
        while q:
            (bx, by, sx, sy, step) = q.popleft()
            for (dx, dy) in dirs:
                (nbx, nby) = (bx + dx, by + dy)
                if 0 <= nbx < m and 0 <= nby < n and (A[nbx][nby] in '.T'):
                    (nsx, nsy) = (2 * bx - nbx, 2 * by - nby)
                    if 0 <= nsx < m and 0 <= nsy < n and reachable(sx, sy, nsx, nsy, bx, by, A, dirs) and (visited[nbx * 20 + nby][nsx * 20 + nsy] == 0):
                        if A[nbx][nby] == 'T':
                            return step + 1
                        visited[nbx * 20 + nby][nsx * 20 + nsy] = 1
                        q.append([nbx, nby, nsx, nsy, step + 1])
        return -1
