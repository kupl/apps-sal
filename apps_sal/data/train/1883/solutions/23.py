class Solution:
    def uniquePathsIII(self, A: List[List[int]]) -> int:
        self.res = 0
        rows = len(A)
        cols = len(A[0])
        empty = 1
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1: 
                    x,y = (i, j)
                elif A[i][j] == 2:
                    end = (i, j)
                elif A[i][j] == 0: 
                    empty += 1
        self.dfs(A,x,y, empty, end)
        return self.res
    def dfs(self, A, x, y, empty, end):
            if x < 0 or x >= len(A) or y < 0 or y >= len(A[0]) or A[x][y] < 0:
                return
            if (x, y) == end:
                self.res += empty == 0
                return
            A[x][y] = -2
            self.dfs(A,x + 1, y, empty - 1, end)
            self.dfs(A,x - 1, y, empty - 1, end)
            self.dfs(A,x, y + 1, empty - 1, end)
            self.dfs(A,x, y - 1, empty - 1, end)
            A[x][y] = 0
