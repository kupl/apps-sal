class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        if n == 1 and m == 1:
            return 0

        dist = {(0, 0, k): 0}
        queue = deque([(0, 0, k)])

        while queue:
            i, j, p = queue.popleft()
            for r, s in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if r == n - 1 and s == m - 1:
                    return dist[(i, j, p)] + 1
                if 0 <= r < n and 0 <= s < m:
                    if grid[r][s] == 0 and (r, s, p) not in dist:
                        dist[(r, s, p)] = dist[(i, j, p)] + 1
                        queue.append((r, s, p))
                    elif p > 0 and (r, s, p - 1) not in dist:
                        dist[(r, s, p - 1)] = dist[(i, j, p)] + 1
                        queue.append((r, s, p - 1))
        return -1
