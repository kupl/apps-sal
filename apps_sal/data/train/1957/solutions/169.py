class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m * n == 1:
            return 0
        dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][k] = 0
        q = deque([(0, 0, k)])
        def move(i, j, k):
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and k >= grid[ni][nj]:
                    yield ni, nj, k - grid[ni][nj]
        while q:
            i, j, k = q.pop()
            for ni, nj, nk in move(i, j, k):
                if ni == m -1 and nj == n -1:
                    return dp[i][j][k] + 1
                
                if dp[i][j][k] + 1 < dp[ni][nj][nk]:
                    dp[ni][nj][nk] = dp[i][j][k] + 1
                    q.appendleft((ni, nj, nk))
        
        return -1
            

