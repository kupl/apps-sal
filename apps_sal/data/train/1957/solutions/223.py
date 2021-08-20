from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return -1
        if k >= len(grid) + len(grid[0]) - 2:
            return len(grid) + len(grid[0]) - 2
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        q = deque([(0, 0, k, 0)])
        visited = set((0, 0, k))
        while q:
            (r, c, obst_rem, steps) = q.popleft()
            for (x, y) in directions:
                (nxt_r, nxt_c) = (r + x, c + y)
                if 0 <= nxt_r < len(grid) and 0 <= nxt_c < len(grid[0]):
                    if grid[nxt_r][nxt_c] == 0 and (nxt_r, nxt_c, obst_rem) not in visited or (grid[nxt_r][nxt_c] == 1 and obst_rem > 0 and ((nxt_r, nxt_c, obst_rem - 1) not in visited)):
                        if nxt_r == len(grid) - 1 and nxt_c == len(grid[0]) - 1:
                            return steps + 1
                        else:
                            visited.add((nxt_r, nxt_c, obst_rem - grid[nxt_r][nxt_c]))
                            q.append((nxt_r, nxt_c, obst_rem - grid[nxt_r][nxt_c], steps + 1))
        return -1
