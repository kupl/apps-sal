class Solution:

    DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def shortestBridge(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        m, n = len(A), len(A[0])
        queue = collections.deque()
        found = False
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(A, i, j, m, n, queue)
                    found = True
                    break
            if found:
                break
        bridge = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for d in self.DIRS:
                    next_x, next_y = x + d[0], y + d[1]
                    if 0 <= next_x < m and 0 <= next_y < n and A[next_x][next_y] == 0:
                        queue.append((next_x, next_y))
                        A[next_x][next_y] = 2
                    if 0 <= next_x < m and 0 <= next_y < n and A[next_x][next_y] == 1:
                        return bridge
            bridge += 1
        return bridge

    def dfs(self, A, i, j, m, n, queue):
        if i < 0 or i >= m or j < 0 or j >= n or A[i][j] != 1:
            return
        A[i][j] = 2
        queue.append((i, j))
        self.dfs(A, i + 1, j, m, n, queue)
        self.dfs(A, i - 1, j, m, n, queue)
        self.dfs(A, i, j + 1, m, n, queue)
        self.dfs(A, i, j - 1, m, n, queue)
