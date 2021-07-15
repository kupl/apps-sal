class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.maxgold = 0
        
        
        def isValid(i, j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] != 0:
                return True
            else:
                return False
        
        def helper(i, j, cursum):
            for direction in directions:
                new_i = i+direction[0]
                new_j = j+direction[1]
                if isValid(new_i, new_j):
                    gold = grid[new_i][new_j]
                    grid[new_i][new_j] = 0
                    helper(new_i, new_j, cursum+gold)
                    grid[new_i][new_j] = gold
            self.maxgold = max(self.maxgold, cursum)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    gold = grid[i][j]
                    grid[i][j] = 0
                    helper(i, j, gold)
                    grid[i][j] = gold
        
        return self.maxgold
