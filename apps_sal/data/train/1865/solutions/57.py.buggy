from collections import deque 
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        
        def check(sx, sy, px, py):
            q = deque([(px, py)])
            visited = set((px, py))
            while q:
                x, y = q.popleft()
                if (x, y) == (sx, sy):
                    return True
                for dx, dy in (-1, 0), (0,-1), (0,1), (1,0):
                    x_, y_ = x+dx, y+dy
                    if valid(x_, y_) and (x_,y_) not in visited:
                        visited.add((x_, y_))
                        q.append((x_, y_))
            return False
        
        def valid(x_, y_):
            return 0<=x_<m and 0<=y_<n and grid[x_][y_] ==\".\"
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == \"B\":
                    bx, by = i, j
                    grid[i][j] = \".\"
                if grid[i][j] == \"S\":
                    sx, sy = i, j
                    grid[i][j] = \".\"
                if grid[i][j] == \"T\":
                    tx, ty = i, j
                    
        q = deque([(bx, by, x, y) for x, y in [(-1, 0), (0,-1), (0,1), (1,0)] if (valid(bx+x, by+y) and check(bx+x, by+y,sx,sy))])
        visited = set()
        level = 0
        while q:
            level += 1
            print(q)
            for _ in range(len(q)):
                
                bx, by, x, y = q.popleft()

                visited.add((bx, by, x, y))
                x_, y_ = bx-x, by-y
                if (x_, y_) == (tx, ty):
                    return level
                if valid(x_,y_) and (x_, y_, x, y) not in visited:
                    q.append((x_, y_, x, y))
                    visited.add((x_, y_, x, y))
                    grid[x_][y_] = \"b\"
                    # print((x_, y_, x, y))
                    px, py = x_+x, y_+y
                    for dx, dy in (-1, 0), (0,-1), (0,1), (1,0):
                        x2, y2 = x_+dx, y_+dy
                        # print(x2, y2)
                        
                        if (x2, y2) != (px, py) and valid(x2, y2) and check(x2, y2, px, py) and (x_,y_,x2-x_,y2-y_) not in visited:
                            q.append((x_,y_,x2-x_,y2-y_))
                            visited.add((x_,y_,x2-x_,y2-y_))
                            # print((x_,y_,x_-x2,y_-y2))
                    grid[x_][y_] = \".\"
        return -1
            
            
        
