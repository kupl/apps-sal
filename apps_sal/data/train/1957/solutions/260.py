class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows == 1 and cols == 1:
            return 0

        # queue = deque([(0,0,k,0)])
        # visited = set([(0,0,k)])

        if k > (rows - 1 + cols - 1):
            return rows - 1 + cols - 1

        queue = deque([(0, 0, k)])
        visited = set([(0, 0, k)])
        steps = 0
        while queue:
            nxt = []
            # for r, c, eliminate, steps in queue:
            for r, c, eliminate in queue:
                for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        if grid[nr][nc] == 1 and eliminate > 0 and (nr, nc, eliminate - 1) not in visited:
                            visited.add((nr, nc, eliminate - 1))
                            nxt.append((nr, nc, eliminate - 1))  # , steps+1))
                        if grid[nr][nc] == 0 and (nr, nc, eliminate) not in visited:
                            if nr == rows - 1 and nc == cols - 1:
                                return steps + 1
                            visited.add((nr, nc, eliminate))
                            nxt.append((nr, nc, eliminate))  # , steps+1))
            queue = nxt
            steps += 1

        return -1

#         while queue:
#             r, c, eliminate, steps = queue.popleft()
#             for nr, nc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
#                 if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
#                     if grid[nr][nc] == 1 and eliminate > 0 and (nr, nc, eliminate-1) not in visited:
#                         visited.add((nr, nc, eliminate-1))
#                         queue.append((nr, nc, eliminate-1, steps+1))
#                     if grid[nr][nc] == 0 and (nr, nc, eliminate) not in visited:
#                         if nr == rows-1 and nc == cols-1:
#                             return steps+1
#                         visited.add((nr, nc, eliminate))
#                         queue.append((nr, nc, eliminate, steps+1))

#         return -1
