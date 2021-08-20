class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        self.bfs = []
        flag = 1
        step = 0
        for i in range(len(A)):
            if flag:
                for j in range(len(A[0])):
                    if A[i][j] == 1:
                        self.dfs(A, i, j)
                        flag = 0
                        break
        while self.bfs:
            size = len(self.bfs)
            while size:
                (i, j) = self.bfs.pop(0)
                for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < len(A) and 0 <= y < len(A[0]):
                        if A[x][y] == 1:
                            return step
                        elif A[x][y] == 0:
                            A[x][y] = -1
                            self.bfs.append([x, y])
                size -= 1
            step += 1
        return step

    def dfs(self, A, i, j):
        if i >= len(A) or j >= len(A[0]) or i < 0 or (j < 0) or (A[i][j] != 1):
            return
        A[i][j] = -1
        self.bfs.append([i, j])
        self.dfs(A, i + 1, j)
        self.dfs(A, i - 1, j)
        self.dfs(A, i, j + 1)
        self.dfs(A, i, j - 1)
