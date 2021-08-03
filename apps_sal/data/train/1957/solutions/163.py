class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])

        def move(i, j, k):
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nk = k - grid[ni][nj]
                    if nk >= 0 and (ni, nj, nk) not in visited:
                        yield ni, nj, nk
        while q:
            i, j, k, s = q.pop()
            if i == m - 1 and j == n - 1:
                return s

            for ni, nj, nk in move(i, j, k):
                visited.add((ni, nj, nk))
                q.appendleft((ni, nj, nk, s + 1))

        return -1
