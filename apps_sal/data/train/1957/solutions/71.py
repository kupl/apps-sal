class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        q = []
        q.append((0, 0, 0, 0))
        (m, n) = (len(grid), len(grid[0]))
        visited = set()
        while q:
            (x, y, obstacle_eliminated, count) = q.pop(0)
            for (nx, ny) in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) == (m - 1, n - 1):
                        return count + 1
                    if grid[nx][ny] == 1 and obstacle_eliminated < k and ((nx, ny, obstacle_eliminated + 1) not in visited):
                        visited.add((nx, ny, obstacle_eliminated + 1))
                        q.append((nx, ny, obstacle_eliminated + 1, count + 1))
                    if grid[nx][ny] == 0 and (nx, ny, obstacle_eliminated) not in visited:
                        visited.add((nx, ny, obstacle_eliminated))
                        q.append((nx, ny, obstacle_eliminated, count + 1))
        return -1
