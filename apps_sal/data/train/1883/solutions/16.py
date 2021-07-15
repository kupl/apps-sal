class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # res = 0
        # m, n, empty = len(A), len(A[0]), 1
        # for i in range(m):
        #     for j in range(n):
        #         if A[i][j] == 1:
        #             x, y = (i, j)
        #         elif A[i][j] == 0:
        #             empty += 1
        # def dfs(x, y, empty):
        #     nonlocal res
        #     if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0): return
        #     if A[x][y] == 2:
        #         res += empty == 0
        #         return
        #     A[x][y] = -2
        #     dfs(x + 1, y, empty - 1)
        #     dfs(x - 1, y, empty - 1)
        #     dfs(x, y + 1, empty - 1)
        #     dfs(x, y - 1, empty - 1)
        #     A[x][y] = 0
        # dfs(x, y, empty)
        # return res
        
        m, n = len(grid), len(grid[0])
        start = end = cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: start = (i, j)
                elif grid[i][j] == 2: end = (i, j)
                if grid[i][j] != -1: cnt += 1 
        ans = 0
        def dfs(x, y, cnt):
            nonlocal ans, start, end
            if not (0 <= x < m and 0 <= y < n and grid[x][y] != -1): return
            if (x, y) == end and cnt == 1:
                ans += 1; return 
            val = grid[x][y]
            grid[x][y] = -1
            for i, j in map(lambda t: (t[0]+x, t[1]+y), [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                dfs(i, j, cnt-1)
            grid[x][y] = val
        dfs(*start, cnt)                    
        return ans
