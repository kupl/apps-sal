from collections import deque
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        r = c = -1
        
        count = 0
        node_count = 0
        ans = []
        for x in range(row):
            for y in range(col):
                if grid[x][y] >= 0:
                    node_count += 1
                  
                if grid[x][y] == 1:
                    r, c = x, y
                
        
        def get_paths(sr, sc, remain):
            
            left = sc - 1
            right = sc + 1
            up = sr - 1
            down = sr + 1
            
            nonlocal count
            
            if left >= 0 and grid[sr][left] == 0:
                #print(sr, left)
                grid[sr][left] = -4
                get_paths(sr, left, remain -1)
                grid[sr][left] = 0
                
            
            if right < col and grid[sr][right] == 0:
                #print(sr, right)
                grid[sr][right] = -4
                get_paths(sr, right, remain -1)
                grid[sr][right] = 0
            
            if up >= 0 and grid[up][sc] == 0:
                #print(up, sc)
                grid[up][sc] = -4
                get_paths(up, sc, remain -1)
                grid[up][sc] = 0
            
            if down < row and grid[down][sc] == 0:
                #print(down, sc)
                grid[down][sc] = -4
                get_paths(down, sc, remain -1)
                grid[down][sc] = 0
            
            if left >= 0 and grid[sr][left] == 2 and remain == 2:
                count += 1
            elif right < col and grid[sr][right] == 2 and remain == 2:
                count += 1
            elif up >= 0 and grid[up][sc] == 2 and remain == 2:
                count += 1
            elif down < row and grid[down][sc] == 2 and remain == 2:
                count += 1
            #print(remain)

        
        get_paths(r, c, node_count)
        return count

