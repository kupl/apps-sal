class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (m, n) = (len(grid), len(grid[0]))
        K = k
        q = []
        q.append((0, 0, K, 0))
        seen = set()
        while q:
            q2 = []
            for (i, j, k, c) in q:
                if i == m - 1 and j == n - 1:
                    return c
                for (ii, jj) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= ii < m and 0 <= jj < n:
                        if grid[ii][jj] == 0 and (ii, jj, k) not in seen:
                            seen.add((ii, jj, k))
                            q2.append((ii, jj, k, c + 1))
                        if grid[ii][jj] == 1 and k > 0 and ((ii, jj, k - 1) not in seen):
                            seen.add((ii, jj, k - 1))
                            q2.append((ii, jj, k - 1, c + 1))
            q = q2
        return -1
