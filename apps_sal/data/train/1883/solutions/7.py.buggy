class Solution:
  def dfs(self, grid, r, c, i, j, count):
    if 0 <= i < r and 0 <= j < c and grid[i][j] != -1:
        if count == -1 and grid[i][j] == 2:
            self.res += 1
        val = grid[i][j]
        grid[i][j] = -1
        self.dfs(grid, r, c, i+1, j, count-1) 
        self.dfs(grid, r, c, i-1, j, count-1) 
        self.dfs(grid, r, c, i, j+1, count-1) 
        self.dfs(grid, r, c, i, j-1, count-1) 
        grid[i][j] = val   

  def uniquePathsIII(self, grid: List[List[int]]) -> int:
    \"\"\"
    1. Find start and end using a double for loop
    2. Use DFS to visit all available paths until we arrive at end then increment counter
    3. Use cache to return number of paths for lower trees
    4. Return the total amount of paths using the counter
    \"\"\"
    r, c, count = len(grid), len(grid[0]), 0
    for i in range(r):
        for j in range(c):
            count += grid[i][j] == 0
    self.res = 0 # treat it as a nonlocal variable
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                self.dfs(grid, r, c, i, j, count)
    return self.res
                        
