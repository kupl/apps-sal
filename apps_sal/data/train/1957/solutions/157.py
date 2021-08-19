class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (m, n) = (len(grid), len(grid[0]))
        frontier = collections.deque([(0, 0, k, 0)])
        seen = {(0, 0, k)}
        while frontier:
            (i, j, d, steps) = frontier.popleft()
            if i == m - 1 and j == n - 1:
                return steps
            for (a, b) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                (r, c) = (i + a, j + b)
                if 0 <= r < m and 0 <= c < n and ((r, c, d - grid[r][c]) not in seen) and (d >= grid[r][c]):
                    seen.add((r, c, d - grid[r][c]))
                    frontier.append((r, c, d - grid[r][c], steps + 1))
        return -1
