class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q, seen, target = [(0, 0, 0, 0)], set(), (n - 1, n - 2, 0)
        for r, c, dr, steps in q:
            if (r, c, dr) == target:
                return steps
            if (r, c, dr) not in seen:
                seen.add((r, c, dr))
                if dr:
                    if c + 1 < n and grid[r][c + 1] + grid[r + 1][c + 1] == 0:
                        q += [(r, c + 1, 1, steps + 1), (r, c, 0, steps + 1)]
                    if r + 2 < n and grid[r + 2][c] == 0:
                        q += [(r + 1, c, 1, steps + 1)]
                else:
                    if r + 1 < n and grid[r + 1][c] + grid[r + 1][c + 1] == 0:
                        q += [(r + 1, c, 0, steps + 1), (r, c, 1, steps + 1)]
                    if c + 2 < n and grid[r][c + 2] == 0:
                        q += [(r, c + 1, 0, steps + 1)]
        return -1
