class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque([(0, 0, k)])
        visited = set((0, 0, k))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        step = 0
        while q:
            for _ in range(len(q)):
                i, j, ck = q.popleft()
                if i == m - 1 and j == n - 1:
                    return step
                for d in dirs:
                    ni, nj = i + d[0], j + d[1]
                    if ni >= 0 and ni < m and nj >= 0 and nj < n and (ni, nj, ck) not in visited:
                        if grid[ni][nj] == 0:
                            q.append((ni, nj, ck))
                            visited.add((ni, nj, ck))
                        if grid[ni][nj] == 1 and ck > 0 and (ni, nj, ck - 1) not in visited:
                            q.append((ni, nj, ck - 1))
                            visited.add((ni, nj, ck - 1))
            step += 1
        return -1
