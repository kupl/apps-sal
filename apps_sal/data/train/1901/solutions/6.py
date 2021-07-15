class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
    
        def move(i, j):
            for (x, y) in ((1,0),(-1,0),(0,1),(0,-1)):
                if 0<=i+x<m and 0<=j+y<n:
                    yield i+x, j+y

        def dfs(i, j, key):
            res = 0
            grid[i][j] = key
            for x, y in move(i, j):
                if grid[x][y] == 1:
                    res += dfs(x, y, key)
            return res + 1

        ## map each island to distinct keys
        mappings = {0:0}
        index = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    mappings[index] = dfs(i, j, index)
                    index += 1

        res = max(mappings.values()) 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    temp = set(grid[x][y] for x,y in move(i, j))
                    res = max(res, sum(mappings[key] for key in temp)+1)

        return res           

