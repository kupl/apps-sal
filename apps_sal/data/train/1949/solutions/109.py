class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,runsum):
            # ending condition ==> when all the nodes around you are visited or zero. there is no way to proceed further
            runsum+= grid[i][j]
            visited[i][j] = 1
            dirr = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
            for r,c in dirr:
                if r >= 0 and r <len(grid) and c>=0 and c <len(grid[0]):
                    if visited[r][c] == 0 and grid[r][c]!=0:
                        dfs(r,c,runsum)
            visited[i][j] = 0
            runningmax.append(runsum)
            
        def getCleanVisited():            
            visited = []
            for i in range(len(grid)):
                visited.append([])
                for j in range(len(grid[0])):
                    visited[i].append(0)
            return visited
        
        
        overallmax = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                visited = getCleanVisited()
                runningmax = []
                dfs(i,j,0)
                overallmax = max(overallmax,max(runningmax))
        
        return overallmax
