class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque([(0, 0, k)])
        visited = set()
        m = len(grid)
        n = len(grid[0])
        res = 0
        while q:
            l = len(q)
            for _ in range(l):
                i, j, k = q.popleft()
                if i == m - 1 and j == n - 1:
                    return res
                for ii, jj in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
                    if 0 <= ii < m and 0 <= jj < n:
                        if grid[ii][jj] == 0:
                            if (ii, jj, k) not in visited:
                                visited.add((ii, jj, k))
                                q.append((ii, jj, k))
                        else:
                            if k > 0 and (ii, jj, k - 1) not in visited:
                                visited.add((ii, jj, k - 1))
                                q.append((ii, jj, k - 1))
            res += 1
        return -1
