class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, k)])
        visited = set([(0, 0, k)])
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j, remain = q.popleft()
                if (i, j) == (m - 1, n - 1):
                    return steps
                for x, y in (i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j):
                    if m > x >= 0 <= y < n:
                        if grid[x][y] == 0 and (x, y, remain) not in visited:
                            q.append((x, y, remain))
                            visited.add((x, y, remain))
                        elif grid[x][y] == 1 and remain > 0 and (x, y, remain - 1) not in visited:
                            q.append((x, y, remain - 1))
                            visited.add((x, y, remain - 1))
            steps += 1

        return -1
