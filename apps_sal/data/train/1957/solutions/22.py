class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        q = [(0, 0, k, 0)]
        m, n = len(grid), len(grid[0])

        visited = {(0, 0, k)}

        while q:
            r, c, ob, step = q.pop(0)
            if (r, c) == (m - 1, n - 1):
                return step

            if grid[r][c] == 1:
                if ob == 0:
                    continue
                else:
                    ob -= 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc, ob) not in visited:
                    q.append((nr, nc, ob, step + 1))
                    visited.add((nr, nc, ob))

        return -1
