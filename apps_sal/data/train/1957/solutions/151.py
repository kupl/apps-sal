from collections import deque


class Solution:

    def shortestPath(self, g: List[List[int]], k: int) -> int:
        (m, n) = (len(g), len(g[0]))
        q = collections.deque([(0, 0, k, 0)])
        seen = {(0, 0, k)}
        while q:
            (x, y, r, s) = q.popleft()
            if x == m - 1 and y == n - 1:
                return s
            for (i, j) in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if 0 <= x + i < m and 0 <= y + j < n:
                    nr = r - (g[x + i][y + j] == 1)
                    if (x + i, y + j, nr) not in seen and nr >= 0:
                        q.append((x + i, y + j, nr, s + 1))
                        seen.add((x + i, y + j, nr))
        return -1
