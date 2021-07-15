class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        cnt = 0
        self.stones = [[0]*n for _ in range(m)]
        cols = [[0]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    self.stones[i][j] = grid[i][j]
                    cols[i][j] = grid[i][j]
                elif j==n-1:
                    self.stones[i][j] = grid[i][j] + self.stones[i+1][j]
                    cols[i][j] = grid[i][j] + cols[i+1][j]
                elif i==m-1:
                    self.stones[i][j] = grid[i][j] + self.stones[i][j+1]
                    cols[i][j] = grid[i][j]
                else:
                    self.stones[i][j] = grid[i][j] + self.stones[i][j+1] + cols[i+1][j]
                    cols[i][j] = grid[i][j] + cols[i+1][j]
                        
            
        self.memo = {}
        
        path = self.dfs(grid, 0, 0, k, set([(0,0,k)]))
        if path == sys.maxsize:
            return -1
        return path
        
    def dfs(self, grid, x, y, k, visited):
        
        m, n = len(grid), len(grid[0])
        if self.stones[x][y] <= k:
            self.memo[x,y,k] = (m-1-x)+(n-1-y)
            return self.memo[x,y,k]
        
        if grid[x][y] == 1: k -= 1
           
        if k < 0: return sys.maxsize
        if x == m-1 and y==n-1: return 0
        if (x,y,k) in self.memo: return self.memo[x,y,k] 
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        shortest = sys.maxsize
        for dx, dy in directions:
            nx, ny = dx+x, dy+y
            if nx<0 or ny<0 or nx>=m or ny>=n or (nx,ny,k) in visited:
                continue
                
            visited.add((nx, ny, k))
            shortest = min(shortest, self.dfs(grid, nx, ny, k, visited)+1)
            visited.remove((nx, ny, k))
           
         
        self.memo[x,y,k] = shortest
        
        return shortest
            
        
        
        

