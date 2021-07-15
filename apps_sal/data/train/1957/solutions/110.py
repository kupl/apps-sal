class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q=[]
        n=len(grid)
        m=len(grid[0])
        v={}
        q.append([0,0,0,k])
        while(q):
            i,j,d,r=q.pop(0)
            if(i==n-1 and j==m-1):
                return d
            let=[[i+1,j],[i,j+1],[i-1,j],[i,j-1]]
            for x,y in let:
                if(0<=x<n and 0<=y<m):
                    if(grid[x][y]==0 and (x,y,r) not in v):
                        v[(x,y,r)]=1
                        q.append([x,y,d+1,r])
                    else:
                        if(r>0 and (x,y,r) not in v):
                            v[(x,y,r)]=1
                            q.append([x,y,d+1,r-1])
        return -1
                        
            

