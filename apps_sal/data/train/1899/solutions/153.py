class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        # mark first island as -1, find and start at second island, bfs until first island is reached while adding steps along
        # find first island
        self.first = []
        def dfs(i, j, m, n):
            if 0 <= i < m and 0 <= j < n and A[i][j] == 1:               
                A[i][j] = 2
                self.first.append((i,j))
                for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    dfs(r, c, m, n)
        
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    dfs(i, j, m, n)
                    break
            if A[i][j] == 2:
                break
        res = m * n
        while self.first:
            i, j = self.first.pop(0)
            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= r < m and 0 <= c < n:
                    if A[r][c] == 0:
                        A[r][c] = A[i][j] + 1
                        self.first.append((r,c))
                    if A[r][c] == 1:
                        res = min(res, A[i][j] - 2)
                        A[i][j] == -1
                        break
            if A[i][j] == -1:
                break
        return res
