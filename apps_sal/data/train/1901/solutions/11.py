class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROW, COL = len(grid), len(grid[0])
        labels = [ [0] * COL for _ in range(ROW) ]
        id = 0
        def neighbors(r, c):
            for nr, nc in ( (r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if nr >= 0 and nr < ROW and nc >= 0 and nc < COL:
                    yield (nr, nc)
                    
        def dfs(row, col, id):
            if row < 0 or row >= ROW or col < 0 or col >= COL:
                return
            if labels[row][col] > 0 or grid[row][col] == 0:
                return
            labels[row][col] = id
            for (nr, nc) in neighbors(row, col):
                dfs(nr, nc, id)
            
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    id += 1
                    dfs(row, col, id)
        
        size = collections.defaultdict(int)
        for row in range(ROW):
            for col in range(COL):
                id = labels[row][col]
                if id > 0:
                    size[id] += 1
        

        ans = max(list(size.values()) or [0])
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    continue
                seen = { labels[nr][nc] for (nr, nc) in neighbors(row, col) if grid[nr][nc] == 1}
                ans = max(ans, 1 + sum( [size[id] for id in seen] ))
                          
        return ans
                
                    
                

