class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        m,n=len(grid),len(grid[0])
        seen=[[float('inf')]*n for _ in range(m)]
        q=[(0,0,0)]
        step=0
        seen[0][0]=0
        while q:
            size=len(q)
            for _ in range(size):
                x,y,o=q.pop(0)
                if x==m-1 and y==n-1:
                    return step
                for dx,dy in dirs:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=m or ny>=n:
                        continue
                    no=o+grid[nx][ny]
                    if no>=seen[nx][ny] or no>k:
                        continue
                    seen[nx][ny]=no
                    q.append((nx,ny,no))
            step+=1
        return -1
