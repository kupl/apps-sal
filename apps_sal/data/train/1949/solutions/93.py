class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        \"\"\"
        :type grid: List[List[int]]
        :rtype: int
        \"\"\"
        res = 0
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        

        def dfs(i, j, sum):
            if not( 0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                return sum
            sum += grid[i][j]
            mx = 0
            tmp = grid[i][j]
            grid[i][j] = 0 
            for x, y in [[i, j+1], [i, j-1], [i-1, j], [i+1, j]]:
                mx = max(mx, dfs(x, y, sum))
            grid[i][j] = tmp
            return mx
            

            
        max_val = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    max_val = max(max_val, dfs(i, j, 0))
        return max_val
        
