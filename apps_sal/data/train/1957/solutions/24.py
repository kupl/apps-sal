class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (N, M) = (len(grid), len(grid[0]))
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [(N - 1, M - 1, k, 0)]
        visited = set([(N - 1, M - 1, k)])
        for (i, j, k, m) in queue:
            if i == 0 and j == 0:
                return m
            for move in moves:
                (ni, nj) = (i + move[0], j + move[1])
                if N > ni >= 0 <= nj < M:
                    nk = k - grid[ni][nj]
                    if nk >= 0 and (ni, nj, nk) not in visited:
                        visited.add((ni, nj, nk))
                        queue.append((ni, nj, nk, m + 1))
        return -1
