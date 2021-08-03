from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return -1

        def boundary_check(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        q = deque([((0, 0, k), 0)])
        visited = set((0, 0, k))
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        end_cell = (len(grid) - 1, len(grid[0]) - 1)

        while q:
            (r, c, obst_rem), jumps = q.popleft()
            if (r, c) == end_cell:
                return jumps

            for x, y in directions:
                nxt_r, nxt_c = r + x, c + y
                if boundary_check(nxt_r, nxt_c):
                    if grid[nxt_r][nxt_c] == 0:
                        nxt_state = (nxt_r, nxt_c, obst_rem)
                    elif obst_rem > 0:
                        nxt_state = (nxt_r, nxt_c, obst_rem - 1)
                    else:
                        continue
                    if nxt_state not in visited:
                        visited.add(nxt_state)
                        q.append((nxt_state, jumps + 1))
        return -1
