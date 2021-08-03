class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        qq = collections.deque()
        xx = [1,2,3]
        yy = [4,5,6]
        qq.appendleft([7,8,9])
        qq.appendleft(yy)
        print(len(qq))
        
        px,py,bx,by,tx,ty = 0,0,0,0,0,0
        visited = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == \"B\":
                    bx = i
                    by = j
                    grid[i][j] = \".\"
                elif grid[i][j] == \"T\":
                    tx = i
                    ty = j
                    grid[i][j] = \".\"
                elif grid[i][j] == \"S\":
                    px = i
                    py = j
                    
                    grid[i][j] = \".\"
                
        
        dir0 = [[0,1],[0,-1],[1,0],[-1,0]]
        visited[(bx,by,px,py)] = 0
        #q = [[bx,by,px,py]]
        q = collections.deque()
        q.append([bx,by,px,py])
        step = 0
        while q:
            #co  = q.pop(0)
            co  = q.popleft()
            if co[0]==tx and co[1]==ty:
                return visited[(co[0],co[1],co[2],co[3])]
            
            for y in range(len(dir0)):
                newx = co[2] + dir0[y][0]
                newy = co[3] + dir0[y][1]
                if newx<0 or newx>= m or newy<0 or newy>=n or (co[0],co[1],newx,newy) in visited:
                    continue
                if newx==co[0] and newy==co[1]:
                    continue
                if grid[newx][newy]!=\".\":
                    continue
                #q.insert(0,[co[0],co[1],newx,newy])
                q.appendleft([co[0],co[1],newx,newy])
                step = visited.get((co[0],co[1],co[2],co[3]),0)
                visited[(co[0],co[1],newx,newy)] = step
                
            
            if abs(co[0]-co[2]) + abs(co[1]-co[3]) == 1:
                for y in range(len(dir0)):
                    if co[2]+dir0[y][0]==co[0] and co[3] + dir0[y][1] == co[1]:
                        newx = co[0] + dir0[y][0]
                        newy = co[1] + dir0[y][1]
                        if newx<0 or newx>= m or newy<0 or newy>=n or (newx,newy,co[0],co[1]) in visited:
                            continue
                        if grid[newx][newy]!=\".\":
                            continue                
                        q.append([newx,newy,co[0],co[1]])
                        step = visited.get((co[0],co[1],co[2],co[3]),0)
                        visited[(newx,newy,co[0],co[1])] = step+1
        return -1       
            
            
            
            
            
            
