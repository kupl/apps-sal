class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q, seen, target = [(0, 0, 0, 0)], set(), (n - 1, n - 2, 0)              # row, column, row difference.
        for r, c, dr, steps in q:
            if (r, c, dr) == target:
                return steps                               # reach target.
            if (r, c, dr) not in seen:                                          # prune duplicates.
                seen.add((r, c, dr))
                if dr:                                                          # vertical position.
                    if c + 1 < n and grid[r][c + 1] + grid[r + 1][c + 1] == 0:  # the two cells right are emtpty.
                        q += [(r, c + 1, 1, steps + 1), (r, c, 0, steps + 1)]   # right and counter-colock-wise rotate.
                    if r + 2 < n and grid[r + 2][c] == 0:                       # the below cell is empty.
                        q += [(r + 1, c, 1, steps + 1)]                         # down.
                else:                                                           # horizontal position
                    if r + 1 < n and grid[r + 1][c] + grid[r + 1][c + 1] == 0:  # the two cells below are empty.
                        q += [(r + 1, c, 0, steps + 1), (r, c, 1, steps + 1)]   # down and colock-wise rotate.
                    if c + 2 < n and grid[r][c + 2] == 0:                       # right cell is empty.
                        q += [(r, c + 1, 0, steps + 1)]                         # right.
        return -1
