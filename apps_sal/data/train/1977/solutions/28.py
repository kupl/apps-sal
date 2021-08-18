class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for i in range(len(grid))]

        def dfs(grid: List[List[int]], visited: List[List[int]], x, y) -> bool:
            closedIsland = not (x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid[0]) - 1)
            queue = [(x, y)]
            while queue:
                x, y = queue.pop()
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        if nx == 0 or ny == 0 or nx == len(grid) - 1 or ny == len(grid[0]) - 1:
                            closedIsland = False

            return closedIsland

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 0:
                    ans += 1 if dfs(grid, visited, i, j) else 0

        return ans
