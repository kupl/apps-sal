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
                for _ in range(len(q)):
                    b, p = q.pop(0)
                    if b == e:
                        return res
                    
                    for i, j in dirs:
                        nx, ny = b[0] + i, b[1] + j #
                        if check(nx, ny) and \\
                            check(b[0] - i, b[1] - j) and\\
                            ((nx, ny), b) not in visit and \\
                            canmoveto((b[0] - i, b[1] - j), b, [p], set([p])):
                            q.append(((nx, ny), b))
                            visit.add(((nx, ny), b))
                res += 1
            return -1
        return move(T,[(B,S)],set([(B,S)]))
                        
                
                
        
        
