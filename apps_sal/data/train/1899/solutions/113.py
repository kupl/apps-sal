class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        (x, y) = self.get_first(A)
        q = collections.deque()
        self.dfs(A, x, y, q)
        step = 0
        while q:
            new_q = collections.deque()
            size = len(q)
            for i in range(size):
                (x, y) = q.popleft()
                for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    (nx, ny) = (x + d[0], y + d[1])
                    if 0 <= nx < len(A) and 0 <= ny < len(A[0]):
                        if A[nx][ny] == 1:
                            return step
                        elif A[nx][ny] == 0:
                            new_q.append([nx, ny])
                            A[nx][ny] = -1
            step += 1
            q = new_q
        return -1

    def get_first(self, A):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    return (i, j)

    def dfs(self, A, x, y, q):
        A[x][y] = -1
        q.append([x, y])
        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            (nx, ny) = (x + d[0], y + d[1])
            if 0 <= nx < len(A) and 0 <= ny < len(A[0]) and (A[nx][ny] == 1):
                self.dfs(A, nx, ny, q)
