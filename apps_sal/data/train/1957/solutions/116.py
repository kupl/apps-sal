class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] == 1 and k == 0:
            return -1
        m, n = len(grid), len(grid[0])
        a = k if grid[0][0] == 0 else k - 1
        q = collections.deque([(0, 0, 0, a)])
        visited = set()
        visited.add((0, 0))
        while q:
            i, j, step, available = q.popleft()
            if i == m - 1 and j == n - 1:
                return step
            for ni, nj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 1 and not available:
                        continue
                    if (ni, nj, available) not in visited:
                        visited.add((ni, nj, available))
                        if grid[ni][nj] == 0:
                            q.append([ni, nj, step + 1, available])
                        if grid[ni][nj] == 1:
                            if available:
                                q.append([ni, nj, step + 1, available - 1])
        return -1
