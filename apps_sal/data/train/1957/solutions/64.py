class Solution:

    def shortestPath(self, grid, k):
        if not grid or not grid[0]:
            return -1
        n = len(grid)
        m = len(grid[0])
        q = [[0, 0, 0, k]]
        seen = set()
        seen.add((0, 0, k))
        while q:
            (d, r, c, ob) = q.pop(0)
            if r == n - 1 and c == m - 1:
                return d
            for (dr, dc) in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    new_ob = ob
                    if grid[nr][nc] == 1:
                        new_ob -= 1
                        if new_ob < 0:
                            continue
                    if (nr, nc, new_ob) in seen:
                        continue
                    q.append([d + 1, nr, nc, new_ob])
                    seen.add((nr, nc, new_ob))
        return -1
