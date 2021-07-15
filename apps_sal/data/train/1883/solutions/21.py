class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        m, n = len(grid), len(grid[0])
        candidates = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    si, sj = i, j
                elif grid[i][j] == 0 or grid[i][j] == 2:
                    candidates.add((i, j))
        
        def helper(i, j):
            if grid[i][j] == 2:
                if not candidates:
                    self.ans += 1
                return
            if grid[i][j] == -1:
                return
            if i < m - 1 and (i + 1, j) in candidates:
                candidates.remove((i+1, j))
                helper(i+1, j)
                candidates.add((i+1,j))
            if i > 0 and (i-1, j) in candidates:
                candidates.remove((i-1, j))
                helper(i-1, j)
                candidates.add((i-1,j))
                              
            if j < n - 1 and (i, j+1) in candidates:
                candidates.remove((i, j+1))
                helper(i, j+1)
                candidates.add((i,j+1))
            if j > 0 and (i, j-1) in candidates:
                candidates.remove((i, j-1))
                helper(i, j-1)
                candidates.add((i,j-1))
        
        helper(si, sj)
        return self.ans
