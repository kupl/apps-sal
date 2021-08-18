class Solution:
    def dfs(self, A, i, j):
        if 0 > i or i >= self.m or 0 > j or j >= self.n or A[i][j] == 0 or A[i][j] == 2:
            return

        A[i][j] = 2
        self.que.append([i, j])
        for i0, j0 in self.offset:
            ii, jj = i + i0, j + j0
            self.dfs(A, ii, jj)

    def shortestBridge(self, A: List[List[int]]) -> int:
        self.offset = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.m, self.n = len(A), len(A[0])
        self.que = []
        ok = 0
        for i in range(self.m):
            for j in range(self.n):
                if A[i][j]:
                    self.dfs(A, i, j)
                    ok = 1
                    break
            if ok:
                break
        rt = 0
        while len(self.que) > 0:
            qlen = len(self.que)
            for k in range(qlen):
                i, j = self.que.pop(0)
                for i0, j0 in self.offset:
                    ii, jj = i + i0, j + j0
                    if 0 <= ii < self.m and 0 <= jj < self.n:
                        if A[ii][jj] == 0:
                            A[ii][jj] = 3
                            self.que.append([ii, jj])
                        elif A[ii][jj] == 1:
                            return rt
            rt += 1
        return rt
