class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        nei = [(0,1),(1,0),(0,-1),(-1,0)]
        m, n = len(grid), len(grid[0])
        rec = dict()
        ans = 0
        def count(grid, i, j):
            cnt = 1
            grid[i][j] = -1
            for dx, dy in nei:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    cnt += count(grid, nx, ny)
                    
            return cnt
        
        def flip(grid, i, j, val):
            grid[i][j] = val
            
            for dx, dy in nei:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == -1:
                    flip(grid, nx, ny, val)
                    
            return
        
        color = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = count(grid, i, j)
                    flip(grid, i, j, color)
                    rec[color] = temp
                    color += 1
                    ans = max(ans, temp)
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visit = set()
                    for dx, dy in nei:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 0:
                            visit.add(grid[nx][ny])
                            
                    ans = max(ans, 1 + sum(rec[i] for i in visit))
           
        return ans
                    
        
        
        

