class Solution:
    def __init__(self):
        self.max = 0
        self.grid=[[]]
        self.dp = [[]]
        
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] != 0: #and self.dp[i][j] == 0:
                    visit = set()
                    self.dp[i][j] = self.dfs(visit,(i,j))
                    self.max=max(self.max, self.dp[i][j])
        
        #self.dp[4][4] = self.dfs(set(),(4,4))
        #print(self.dp)
        return self.max
        
    def dfs(self, visit, node):
        
        #visit.add(node)
        i,j = node
        #self.dp[i][j] = self.grid[i][j]
        neighborVals = [0]
        #print(visit)
        for di, dj in [(-1,0),(0,1),(1,0),(0,-1)]:
            if 0 <= i+di < len(self.grid) and 0 <= j+dj < len(self.grid[0]) and \\
            (i+di,j+dj) not in visit:
                if self.grid[i+di][j+dj] > 0: #and self.dp[i+di][j+dj] == 0:
                    #self.dfs(visit, (i+di,j+dj))
                    temp = set()
                    temp.add(node)
                    neighborVals.append(self.dfs(visit.union(temp), (i+di,j+dj))) #self.dp[i+di][j+dj])
        #print(node,self.grid[i][j], neighborVals)
        return self.grid[i][j] + max(neighborVals)
