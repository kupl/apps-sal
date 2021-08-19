class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    (bi, bj) = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == 'S':
                    (si, sj) = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == 'T':
                    (ti, tj) = (i, j)
                    grid[i][j] = '.'
        q = [(bi, bj, si, sj, 0)]
        seen = {(bi, bj, si, sj)}
        while q:
            (bi, bj, si, sj, dist) = q.pop(0)
            if (bi, bj) == (ti, tj):
                return dist
            for (dx, dy) in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                (si_new, sj_new) = (bi + dx, bj + dy)
                (bi_new, bj_new) = (bi - dx, bj - dy)
                if (bi_new, bj_new, bi, bj) not in seen and self.canMoveTo(grid, bi, bj, si, sj, si_new, sj_new) and (0 <= bi_new < m) and (0 <= bj_new < n) and (grid[bi_new][bj_new] == '.'):
                    q.append((bi_new, bj_new, bi, bj, dist + 1))
                    seen.add((bi_new, bj_new, bi, bj))
        return -1

    def canMoveTo(self, grid, bi, bj, si, sj, si_new, sj_new):
        (m, n) = (len(grid), len(grid[0]))
        q = [(si, sj)]
        visited = {(si, sj)}
        while q:
            (si, sj) = q.pop(0)
            if si == si_new and sj == sj_new:
                return True
            for (dx, dy) in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                (i, j) = (si + dx, sj + dy)
                if (i, j) not in visited and 0 <= i < m and (0 <= j < n) and ((i, j) != (bi, bj)) and (grid[i][j] != '#'):
                    q.append((i, j))
                    visited.add((i, j))
        return False
    "\n    def canMoveTo(self, grid, bi, bj, si, sj, si_new, sj_new, visited):\n        m, n = len(grid), len(grid[0])\n        if si == si_new and sj == sj_new:\n            return True\n        visited.add((si, sj))\n        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:\n            i, j = si+dx, sj+dy\n            if (i, j) not in visited and 0 <= i < m and 0 <= j < n and (i, j) != (bi, bj) and grid[i][j] != '#' and self.canMoveTo(grid, bi, bj, i, j, si_new, sj_new, visited):\n                return True\n        return False\n        \n    def canMoveTo(self, grid, bi, bj, si, sj, validSet):\n        m, n = len(grid), len(grid[0])\n        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:\n            i, j = si+dx, sj+dy\n            if (i, j) in validSet:\n                continue\n            if 0 <= i < m and 0 <= j < n and (i, j) != (bi, bj) and grid[i][j] != '#':\n                validSet.add((i, j))\n                self.canMoveTo(grid, bi, bj, i, j, validSet)\n        return validSet\n    "
