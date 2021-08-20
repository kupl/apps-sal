class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:

        def dfs(i, j, n, m):
            A[i][j] = 2
            queue.append((i, j))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for (dx, dy) in directions:
                (x, y) = (i + dx, j + dy)
                if 0 <= x < n and 0 <= y < m and (A[x][y] == 1):
                    dfs(x, y, n, m)
        from collections import deque
        queue = deque()
        (n, m) = (len(A), len(A[0]))
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    dfs(i, j, n, m)
                    break
            else:
                continue
            break
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        step = 0
        while queue:
            size = len(queue)
            flag = False
            for i in range(size):
                point = queue.popleft()
                (x, y) = (point[0], point[1])
                for (dx, dy) in directions:
                    (_x, _y) = (x + dx, y + dy)
                    if _x < 0 or _x >= n or _y < 0 or (_y >= m) or (A[_x][_y] == 2):
                        continue
                    if A[_x][_y] == 1:
                        return step
                    A[_x][_y] = 2
                    queue.append((_x, _y))
            step += 1
