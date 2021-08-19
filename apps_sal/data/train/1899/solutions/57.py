class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        if len(A) == 0:
            return 0
        m = len(A)
        n = len(A[0])
        queue = []
        component = 2
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(i, j, A, queue, component)
                    print(A)
                    component += 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            (path, x, y) = queue.pop(0)
            if A[x][y] == 3:
                continue
            for (dx, dy) in directions:
                if x + dx < 0 or y + dy < 0 or x + dx >= m or (y + dy >= n):
                    continue
                if A[x + dx][y + dy] == 3:
                    return path
                if A[x + dx][y + dy] == 0:
                    A[x + dx][y + dy] = 2
                    queue.append((path + 1, x + dx, y + dy))

    def dfs(self, i, j, grid, queue, component):
        queue.append((0, i, j))
        grid[i][j] = component
        stack = [(i, j)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while stack:
            (x, y) = stack.pop()
            for (dx, dy) in directions:
                if x + dx < 0 or y + dy < 0 or x + dx >= len(grid) or (y + dy >= len(grid[0])):
                    continue
                if grid[x + dx][y + dy] == 1:
                    queue.append((0, x + dx, y + dy))
                    stack.append((x + dx, y + dy))
                    grid[x + dx][y + dy] = component
