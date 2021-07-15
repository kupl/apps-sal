# Work our way through the grid one step at a time (multiple searches running at a time given we have 4 different directions to explore at any given step).
# Each step we check if we're at the end of our our grid, if not we continue the search.
# Continuing the search we look at the next step of our 4 directions and make sure its valid (on the board, can afford to move an object or it's a clear 0), we record the step taken deduct 1 from k if it was a 1 location and put it back on the q.
# We repeat this until we hit the end or run out of locations to explore in which case we couldn't make it to the end so we return -1.


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # We'll use a deque for our BFS traversal.
        q = collections.deque([])
\t\t# (row, col, steps, k)
        q.append((0, 0, 0, k))
\t\t# Use a set (O(1) lookup) to track the locations we've visited to avoid revisiting.
        seen = set()
        while q:
\t\t    # Pop the next location from the q.
            r, c, steps, rk = q.popleft()
\t\t\t# If we're at the finish location return the steps, given BFS this will be
\t\t\t# guaranteed to be the first to hit this condition.
            if r == rows-1 and c == cols - 1:
                return steps
\t\t\t# Otherwise we'll keep travelling throught the grid in our 4 directions.
            else:
                for y, x in directions:
                    nr = r + y
                    nc = c + x
\t\t\t\t\t# If the new location is on the board and has not been visited.
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc, rk) not in seen:
                        if grid[nr][nc] == 1 and rk > 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk - 1))
                        elif grid[nr][nc] == 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk))
\t\t# If we don't hit the end in our traversal we know it's not possible.
        return -1
        
