class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (nrow, ncol) = (len(grid), len(grid[0]))
        q = collections.deque([(0, 0, 0, k)])
        visited = set()
        visited.add((0, 0, k))
        while q:
            (i, j, d, life) = q.popleft()
            if i == nrow - 1 and j == ncol - 1:
                return d
            if grid[i][j] == 1:
                if life == 0:
                    continue
                else:
                    life -= 1
            for (x, y) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < nrow and 0 <= y < ncol and ((x, y, life) not in visited):
                    q.append((x, y, d + 1, life))
                    visited.add((x, y, life))
        return -1
