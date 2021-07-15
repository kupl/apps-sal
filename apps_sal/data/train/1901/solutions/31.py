class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        def neighbours(r,c):
            result = []
            for nr, nc in [(r-1,c),(r+1,c),(r, c-1), (r, c+1)]:
                if 0 <= nr < N and 0 <= nc < N:
                    result.append((nr,nc))
            return result 
        
        def dfs(r, c, index):
            ans = 1 
            grid[r][c] = index
            for nr, nc in neighbours(r,c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans 
        
        areas = {}
        index = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    areas[index] = dfs(r,c,index)
                    index += 1 
        ans = max(list(areas.values()) or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbours(r,c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(areas[i] for i in seen))
        
        return ans 
                    
        
                    
                    
        

