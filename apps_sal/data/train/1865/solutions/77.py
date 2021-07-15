class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='S':
                    S=(i,j)
                if grid[i][j]=='B':
                    B=(i,j)
                if grid[i][j]=='T':
                    T=(i,j)
                    
                    
        def check(x,y):    #判断这个位置是否有效
            return 0<=x<m and 0<=y<n and grid[x][y]!='#'
                    
            
        def canmoveto(e,b,q,visit):          #判断人能否到达目标位置
            while q:
                p=q.pop(0)
                if p==e:
                    return True
                for dx,dy in dirs:
                    nx,ny=p[0]+dx,p[1]+dy
                    if check(nx,ny) and (nx,ny)!=b and (nx,ny) not in visit:
                        q.append((nx,ny))
                        visit.add((nx,ny))
            return False
        
        def move(e,q,visit):   #判断人能否把箱子推到目标位置
            res = 0
            while q:
                size=len(q)
                for _ in range(size):
                    b, p = q.pop(0)
                    if b == e:
                        return res
                    
                    for dx,dy in dirs:
                        nbx, nby = b[0] +dx, b[1] +dy
                        npx,npy=b[0]-dx,b[1]-dy
                        if check(nbx, nby) and \\
                            check(npx,npy) and\\
                            ((nbx, nby), b) not in visit and \\
                            canmoveto((npx,npy), b, [p], set([p])):
                            q.append(((nbx, nby), b))
                            visit.add(((nbx, nby), b))
                res += 1
            return -1
        return move(T,[(B,S)],set([(B,S)]))
                        
                
                
        
        
