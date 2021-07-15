class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        # visited = set()
        # visited.add((0, 0, k))
        # candidates = deque()
        # candidates.append((0, 0, 0, k))
        # if len(grid) == 1 and len(grid[0]) == 1: return 0
        # while len(candidates) > 0:
        #     ci, cj, steps, ck = candidates.popleft()
        #     if ci == len(grid) -1 and cj == len(grid[0]) - 1:
        #         return steps
        #     for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        #         ni, nj = ci + x, cj + y
        #         if ni < 0 or nj < 0 or ni >= len(grid) or nj >= len(grid[0]): 
        #             continue
        #         if (ni, nj, ck) in visited: 
        #             continue
        #         if grid[ni][nj] == 1 and ck > 0:
        #             candidates.append((ni, nj, steps+1, ck-1))
        #             visited.add((ni, nj, ck-1))
        #         elif grid[ni][nj] == 0:
        #             candidates.append((ni, nj, steps+1, ck))
        #             visited.add((ni, nj, ck))
        # return -1
    
        rows = len(grid)
        cols = len(grid[0])
\t\t# Directions we'll use to change our location (down, up, right, left).
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # We'll use a deque for our BFS traversal.
        q = collections.deque([])
\t\t# Append our starting details to the q.
\t\t# (row, col, steps, k)
        q.append((0, 0, 0, k))
\t\t# Use a set (O(1) lookup) to track the locations we've visited to avoid revisiting.
        seen = set()
        seen.add((0, 0 , k))
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
\t\t\t\t\t    # If it's a blocker but we still have k left, we'll go there and k -= 1.
                        if grid[nr][nc] == 1 and rk > 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk - 1))
\t\t\t\t\t\t# Otherwise continue on  if it's a 0 - free location.
                        elif grid[nr][nc] == 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk))
\t\t# If we don't hit the end in our traversal we know it's not possible.
        return -1
            

        
