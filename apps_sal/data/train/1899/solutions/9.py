class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if(len(A) == 0):
            return 0
        m = len(A)
        n = len(A[0])
        queue = []
        found = False
        for i in range(m):
            if(found):
                break
            for j in range(n):
                if(A[i][j] == 1):
                    self.dfs(i, j, A, queue)
                    found = True
                    break
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while(queue):
            path, x, y = queue.pop(0)
            for dx, dy in directions:
                if(x + dx < 0 or y + dy < 0 or x + dx >= m or y + dy >= n):
                    continue
                if(A[x + dx][y + dy] == 1):
                    return path
                if(A[x + dx][y + dy] == 0):
                    A[x + dx][y + dy] = 2
                    queue.append((path + 1, x + dx, y + dy))
        return -1

    def dfs(self, i, j, grid, queue):
        queue.append((0, i, j))
        grid[i][j] = 2
        stack = [(i, j)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while(stack):
            x, y = stack.pop()
            for dx, dy in directions:
                if(x + dx < 0 or y + dy < 0 or x + dx >= len(grid) or y + dy >= len(grid[0])):
                    continue
                if(grid[x + dx][y + dy] == 1):
                    queue.append((0, x + dx, y + dy))
                    stack.append((x + dx, y + dy))
                    grid[x + dx][y + dy] = 2
