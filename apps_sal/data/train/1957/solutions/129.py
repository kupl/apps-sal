class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited = set()
        q = collections.deque([[0, 0, 0, k]])
        m = len(grid)
        n = len(grid[0])
        while q:
            i, j, d, score = q.popleft()
            if i == m - 1 and j == n - 1:
                return d
            if (i, j, score) in visited:
                continue
            visited.add((i, j, score))
            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                r, c = x + i, y + j
                if r < 0 or r >= m or c < 0 or c >= n or score < grid[r][c] \\
                    or (r, c, score - grid[r][c]) in visited:
                    continue
                q.append([r, c, d + 1, score - grid[r][c]])
            
        return -1
            
            
