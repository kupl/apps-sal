class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:
        (n, m) = (len(grid), len(grid[0]))
        B = T = S = None
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'B':
                    B = (i, j)
                if grid[i][j] == 'T':
                    T = (i, j)
                if grid[i][j] == 'S':
                    S = (i, j)
        heap = [(0, B[0], B[1], S[0], S[1])]
        heapq.heapify(heap)
        seen = set()
        while heap:
            (c, bi, bj, si, sj) = heapq.heappop(heap)
            if (bi, bj) == T:
                return c
            if (bi, bj, si, sj) in seen:
                continue
            seen.add((bi, bj, si, sj))
            for (nsi, nsj) in [(si + 1, sj), (si - 1, sj), (si, sj + 1), (si, sj - 1)]:
                if 0 <= nsi < n and 0 <= nsj < m and (grid[nsi][nsj] != '#'):
                    if (nsi, nsj) != (bi, bj) and (bi, bj, nsi, nsj) not in seen:
                        heapq.heappush(heap, (c, bi, bj, nsi, nsj))
                    elif (bi, bj) == (nsi, nsj):
                        (nbi, nbj) = (nsi - (si - nsi), nsj - (sj - nsj))
                        if 0 <= nbi < n and 0 <= nbj < m and ((nbi, nbj, nsi, nsj) not in seen):
                            heapq.heappush(heap, (c + 1, nbi, nbj, nsi, nsj))
        return -1
