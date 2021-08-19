class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque()
        visited = {}
        queue.append((0, 0, 0, 0))
        while queue:
            (x, y, eliminated, count) = queue.popleft()
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return count
            if (x, y) in visited and eliminated >= visited[x, y]:
                continue
            visited[x, y] = eliminated
            for (i, j) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                (nx, ny) = (x + i, y + j)
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (eliminated + grid[nx][ny] <= k):
                    queue.append((nx, ny, eliminated + grid[nx][ny], count + 1))
        return -1
