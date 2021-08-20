class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:
        (n, m) = (len(grid), len(grid[0]))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'T':
                    t = (i, j)
                elif grid[i][j] == 'S':
                    s = (i, j)
                elif grid[i][j] == 'B':
                    b = (i, j)
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = [tuple(s + b)]
        seen = set(q)
        steps = 0
        while q:
            nq = []
            for (si, sj, bi, bj) in q:
                if t == (bi, bj):
                    return steps
                for (di, dj) in dirs:
                    (nsi, nsj) = (si + di, sj + dj)
                    if nsi == bi and nsj == bj:
                        (nbi, nbj) = (bi + di, bj + dj)
                        ds = 1
                    else:
                        (nbi, nbj) = (bi, bj)
                        ds = 0
                    if not (0 <= nsi < n and 0 <= nsj < m):
                        continue
                    if not (0 <= nbi < n and 0 <= nbj < m):
                        continue
                    if grid[nsi][nsj] == '#' or grid[nbi][nbj] == '#':
                        continue
                    nsb = (nsi, nsj, nbi, nbj)
                    if nsb in seen:
                        continue
                    seen.add(nsb)
                    if ds == 0:
                        q.append(nsb)
                    else:
                        nq.append(nsb)
            q = nq
            steps += 1
        return -1
