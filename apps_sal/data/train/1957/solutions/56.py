from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque()
        cur = (0, 0, k, 0)
        visited = set()
        q.append(cur)
        visited.add(cur)
        m = len(grid)
        n = len(grid[0])

        diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while len(q) != 0:
            i, j, l, s = q.popleft()
            if i == m - 1 and j == n - 1:
                return s

            for d in diffs:
                n_i = i + d[0]
                n_j = j + d[1]
                if 0 <= n_i < m and 0 <= n_j < n:
                    if grid[n_i][n_j] and l != 0 and (n_i, n_j, l - 1) not in visited:
                        q.append((n_i, n_j, l - 1, s + 1))
                        visited.add((n_i, n_j, l - 1))
                    elif not grid[n_i][n_j] and (n_i, n_j, l) not in visited:
                        q.append((n_i, n_j, l, s + 1))
                        visited.add((n_i, n_j, l))

        return -1
