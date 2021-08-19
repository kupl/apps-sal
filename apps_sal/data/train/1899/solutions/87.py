import collections


class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        found = False
        res = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    self.dfs(A, i, j, res)
                    found = True
                    break
            if found:
                break
        cnt = 0
        while res:
            tmp = []
            for (x, y) in res:
                for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if 0 <= x + dx < len(A) and 0 <= y + dy < len(A[0]) and (A[x + dx][y + dy] != 2):
                        if A[x + dx][y + dy] == 0:
                            A[x + dx][y + dy] = 2
                        if A[x + dx][y + dy] == 1:
                            return cnt
                        tmp.append([x + dx, y + dy])
            cnt += 1
            res = tmp
        return -1

    def dfs(self, A, i, j, res):
        if 0 <= i < len(A) and 0 <= j < len(A[0]) and (A[i][j] == 1):
            A[i][j] = 2
            res.append([i, j])
            self.dfs(A, i + 1, j, res)
            self.dfs(A, i - 1, j, res)
            self.dfs(A, i, j - 1, res)
            self.dfs(A, i, j + 1, res)
