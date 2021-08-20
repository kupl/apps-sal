from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (rows, cols) = (len(grid), len(grid[0]))
        if k >= rows + cols - 3:
            return rows + cols - 2
        (q, seen) = (deque([(0, 0, 0, 0)]), set())
        seen.add((0, 0, 0))
        while q:
            (i, j, rem, curr_path) = q.popleft()
            if i == rows - 1 and j == cols - 1:
                return curr_path
            for (m, n) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= m < rows and 0 <= n < cols and ((m, n, rem) not in seen) and (rem + grid[m][n] <= k):
                    q.append((m, n, rem + grid[m][n], curr_path + 1))
                    seen.add((m, n, rem + grid[m][n]))
        return -1
