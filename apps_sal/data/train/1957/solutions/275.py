class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = defaultdict(lambda :float('inf'))
        dp[(m-1,n-1,k)]=0
        todo = [(m-1,n-1,k)]
        seen = {(m-1,n-1):k}
        while todo:
            new = []
            for i,j,r in todo:
                if (i,j)==(0,0):return dp[(i,j,r)]
                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if  0<=x<m and 0<=y<n and(grid[x][y] == 0 or r>0):
                        
                        new_r = r if grid[x][y] == 0 else r-1
                        
                        dp[(x,y,new_r)] = min(dp[(x,y,new_r)], dp[(i,j,r)]+1)
                        
                        if (x,y) not in seen or seen[(x,y)]<new_r:
                            
                            new.append((x,y,new_r))
                            seen[(x,y)] = new_r
                    
                            
            todo = new
        
        return -1
