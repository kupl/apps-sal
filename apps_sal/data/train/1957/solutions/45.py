class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:  # 43

        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        q = collections.deque([(0, 0, 0, 0)])
        m, n = len(grid), len(grid[0])
        visited = set()

        while q:
            x, y, obstacle, path = q.popleft()
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 1 and obstacle < k and (i, j, obstacle + 1) not in visited:
                        visited.add((i, j, obstacle + 1))
                        q.append((i, j, obstacle + 1, path + 1))
                    if grid[i][j] == 0 and (i, j, obstacle) not in visited:
                        if (i, j) == (m - 1, n - 1):
                            return path + 1
                        visited.add((i, j, obstacle))
                        q.append((i, j, obstacle, path + 1))

        return -1
