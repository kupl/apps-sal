class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        bfs = collections.deque([(0, 0, 0, 0)])
        seen = set([(0, 0, 0)])
        while bfs:
            c, used, i, j = bfs.popleft()
            if i == n - 1 and j == m - 1:
                return c
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < n and 0 <= nj < m and used + grid[ni][nj] <= k and (ni, nj, used + grid[ni][nj]) not in seen:
                    bfs.append((c + 1, used + grid[ni][nj], ni, nj))
                    seen.add((ni, nj, used + grid[ni][nj]))

        return -1
