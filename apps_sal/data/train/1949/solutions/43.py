class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.orig_grid = grid
        self.M = len(grid)
        self.N = len(grid[0])
        max_gold = 0
        for i in range(self.M):
            for j in range(self.N):
                self.soln =  [ [ 0 for j in range(self.N) ] for i in range(self.M) ]
                curr = self.trackGold(i, j)#, self.soln)
                max_gold = max(max_gold, curr)
        return max_gold

    def trackGold(self, i, j):#, soln):
        if (i < 0 or i >= self.M or j < 0 or j >= self.N or self.orig_grid[i][j] == 0 or self.soln[i][j] == 1):
            return 0
        
        self.soln[i][j] = 1
        future_gold = max(self.trackGold(i+1, j), self.trackGold(i, j+1), self.trackGold(i-1, j), self.trackGold(i, j-1))
        curr_gold = self.orig_grid[i][j] + future_gold
        self.soln[i][j] = 0
        return curr_gold
