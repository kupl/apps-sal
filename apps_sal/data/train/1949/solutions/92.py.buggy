class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        \"\"\"
        At each square, look at adjacent squares.
        
        If adjacent square is 0 then skip
        If adjacent square has already been visited during this path then skip
        If adjacent square is not in bounds of grid then skip
        
        Else add it to the list of squares visited on this path, then explore
        that adjacent square.
        
        If there are no more adjacent squares to visit, then
        record the path total and update the nonlocal total.
        
        Caveats:
            - We can't cache because the max path from a square differs depending on the preceding path
        \"\"\"
        self.max_gold = 0
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(path_gold = 0, i = 0, j = 0):
            g = grid[i][j]
            if g == 0:
                if path_gold > self.max_gold:
                    self.max_gold = path_gold
                return
            
            curr_path_gold = path_gold + g
            grid[i][j] = 0
            if i > 0:
                dfs(curr_path_gold, i - 1, j)
            if i < m-1:
                dfs(curr_path_gold, i + 1, j)

            if j > 0:
                dfs(curr_path_gold, i, j - 1)
            if j < n-1:
                dfs(curr_path_gold, i, j + 1)
            grid[i][j] = g
        
        for i in range(m):
            for j in range(n):
                dfs(i = i, j = j)
        
        return self.max_gold
            
        
            
                
                    
