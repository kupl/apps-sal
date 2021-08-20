class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        visited = set()
        q = collections.deque([((0, 0), k, 0)])
        while q:
            ((r, c), k_left, dist) = q.popleft()
            if ((r, c), k_left) in visited:
                continue
            visited.add(((r, c), k_left))
            if r == n - 1 and c == m - 1:
                return dist
            for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (0 <= r + dr < n and 0 <= c + dc < m) and (grid[r + dr][c + dc] == 0 or k_left > 0):
                    q.append(((r + dr, c + dc), k_left - grid[r + dr][c + dc], dist + 1))
        return -1
