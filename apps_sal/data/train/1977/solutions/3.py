class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.visited = [ [ 0 for _ in range(len(grid[0])) ] for _ in range(len(grid))]
        def dfs(i, j):
            if i < 0 or j < 0 or i>=len(self.grid) or j>=len(self.grid[0]) :
                return False
            if self.grid[i][j] == 1 or self.visited[i][j]==1:
                return True
            self.visited[i][j] = 1
            neighbs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            ans = True
            for x, y in neighbs:
                curr = dfs(i+x, j+y)
                if curr == False:
                    ans = False
            return ans
        
        ans = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.visited[i][j]==0 and self.grid[i][j]==0:
                    isclosed = dfs(i, j)
                    if isclosed==True:
                        ans+=1
        return ans

