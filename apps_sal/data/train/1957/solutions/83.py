from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque([(0, 0, 0, k)])
        visited = set([(0, 0, k)])
        if len(grid[0]) == 1 and len(grid) == 1:
            return 0
        while q:
            (row, col, dist, cur_k) = q.popleft()
            for (nr, nc) in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
                d = dist + 1
                if nr < len(grid) and nr >= 0 and (nc < len(grid[0])) and (nc >= 0):
                    if (nr, nc, cur_k) not in visited and grid[nr][nc] == 0:
                        if nr == len(grid) - 1 and nc == len(grid[0]) - 1:
                            return dist + 1
                        q.append((nr, nc, d, cur_k))
                        visited.add((nr, nc, cur_k))
                    if (nr, nc, cur_k - 1) not in visited and grid[nr][nc] == 1:
                        if cur_k > 0:
                            if nr == len(grid) - 1 and nc == len(grid[0]) - 1:
                                return dist + 1
                            q.append((nr, nc, d, cur_k - 1))
                            visited.add((nr, nc, cur_k - 1))
        return -1
