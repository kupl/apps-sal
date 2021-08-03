from copy import deepcopy
WATER = 0
LAND = 1
ISLAND = 2
BRIDGE = 3
DIR = ((-1, 0), (1, 0), (0, -1), (0, 1))


class Solution:
    def shortestBridge(self, A):
        x0, y0 = self.findFirstLand(A)
        q = deque([(x0, y0)])
        visited = set([(x0, y0)])
        self.bfs(A, q, visited, LAND)
        q = deque(visited)
        return self.bfs(A, q, visited, WATER, LAND) - 1

    def findFirstLand(self, A):
        m, n = len(A), len(A[0])
        for x in range(m):
            for y in range(n):
                if A[x][y] == LAND:
                    return x, y

    def bfs(self, A, q, visited, target, des=-1):
        m, n = len(A), len(A[0])
        step = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx <= m - 1 and 0 <= ny <= n - 1 and (nx, ny) not in visited:
                        if A[nx][ny] == des:
                            return step + 1
                        if A[nx][ny] == target:
                            q.append((nx, ny))
                            visited.add((nx, ny))
            step += 1
        return step - 1
