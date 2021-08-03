\"\"\"
level 0: [bx,by,px,py]

level 1: [bx-1, by, px-1, py]

level 3: 


\"\"\"



class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])        
        bx, by, px, py = 0, 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    px, py = i, j
                    grid[i][j] = '.'
                elif grid[i][j] == 'B':
                    bx, by = i, j
                    grid[i][j] = '.'
                elif grid[i][j] == 'T':
                    tx, ty = i, j
                    grid[i][j] = '.'
                
        queue = collections.deque()
        queue.append([bx, by, px, py])
        memo = collections.defaultdict(lambda : -1)
        memo[(bx, by, px, py)] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            bx, by, px, py = queue.popleft()
            if bx == tx and by == ty:
                return memo[(bx, by, px, py)]
                             
            for k in range(4):
                x = px + directions[k][0]
                y = py + directions[k][1]
                if x<0 or x>=m or y<0 or y>=n:
                    continue
                if grid[x][y] != '.':
                    continue
                if x == bx and y == by:
                    continue
                if memo[(bx, by, x, y)] >= 0:
                    continue
                memo[(bx, by, x, y)] = memo[(bx, by, px, py)]
                queue.appendleft([bx, by, x, y])
            
            #相邻
            if abs(px-bx) + abs(py-by) == 1:
                for k in range(4):
                    if px+directions[k][0] == bx and py+directions[k][1] == by:
                        bx2 = bx+directions[k][0]
                        by2 = by+directions[k][1]
                        if bx2<0 or bx2>=m or by2<0 or by2>=n:
                            continue
                        if grid[bx2][by2] != '.':
                            continue
                        if memo[(bx2, by2, bx, by)] >= 0:
                            continue
                        memo[(bx2, by2, bx, by)] = memo[(bx, by, px, py)] + 1
                        queue.append([bx2, by2, bx, by])
            
        return -1
            
        
        
        
        
        
