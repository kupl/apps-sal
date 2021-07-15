class Solution:
    def getDegree(self, i, j, grid: List[List[int]]) -> int:
        \"\"\"
        get graph-degree of coord (i,j)
        \"\"\"
        if grid[i][j] == 0:
            return 0
        deg = 0
        if i > 0 and grid[i-1][j] > 0:
            deg += 1
        if i < len(grid) - 1 and grid[i+1][j] > 0:
            deg += 1  
        if j > 0 and grid[i][j-1] > 0:
            deg += 1
        if j < len(grid[0]) - 1 and grid[i][j+1] > 0:
            deg += 1
        return deg
    
    
    def traverseMaxGoldDfs(self, i, j, grid) -> int:
        \"\"\"
        use dfs (with conditions) to get the max gold from starting coord (i,j)
        \"\"\"
        
        temp = grid[i][j]
        grid[i][j] = 0
        gold = temp
        goldRes = 0
        if i > 0 and grid[i-1][j] > 0:
            goldRes = max(goldRes, self.traverseMaxGoldDfs(i-1, j, grid))
        if i < len(grid) - 1 and grid[i+1][j] > 0:
            goldRes = max(goldRes, self.traverseMaxGoldDfs(i+1, j, grid))
        if j > 0 and grid[i][j-1] > 0:
            goldRes = max(goldRes, self.traverseMaxGoldDfs(i, j-1, grid))
        if j < len(grid[0]) - 1 and grid[i][j+1] > 0:
            goldRes = max(goldRes, self.traverseMaxGoldDfs(i, j+1, grid))
            
        gold = max(gold, temp + goldRes)  
        grid[i][j] = temp
        return gold
    

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                degree = self.getDegree(i, j, grid)
                # don't bother checking degree 2, since it is neither a 'junction' nor a 'leaf'
                # of the search tree
                if grid[i][j] > 0 and (degree <= 1 or degree > 2):
                    # traverse using bfs from here. 
                    gold = self.traverseMaxGoldDfs(i, j, grid)
                    if gold > maxGold:
                        maxGold = gold
        return maxGold
                    
