from typing import List


class Solution:

    def __init__(self):
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        res = -1
        m = len(grid)
        n = len(grid[0])
        q = [(0, 0, 0, 0)]
        (head, tail) = (0, 1)
        visited = set()
        while head < tail:
            (ci, cj, uk, d) = q[head]
            head += 1
            if ci == m - 1 and cj == n - 1:
                res = d
                break
            else:
                for i in range(0, 4):
                    ni = ci + self.dx[i]
                    nj = cj + self.dy[i]
                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            if uk + 1 <= k and (ni, nj, uk + 1) not in visited:
                                visited.add((ni, nj, uk + 1))
                                q.append((ni, nj, uk + 1, d + 1))
                                tail += 1
                        elif (ni, nj, uk) not in visited:
                            visited.add((ni, nj, uk))
                            q.append((ni, nj, uk, d + 1))
                            tail += 1
        return res
