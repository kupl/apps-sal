class Solution:
    
    def __init__(self): 
        self.moves = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        best = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if self.canMove(i, j, grid, set()):
                    total = self.moveNext(i, j, grid, set(), 0)
                    best = max(best, total)
        return best
        
    def moveNext(self, x, y, grid, visited, total):
        visited.add((x,y))
        total = total+grid[x][y]
        best = total
        for move in self.moves:
            if self.canMove(x+move[0],y+move[1],grid, visited):
                s = self.moveNext(x+move[0],y+move[1], grid, visited.copy(), total)
                if s > best:
                    best = s
        return best
        
        
    def canMove(self, x,y,grid,visited):
        return ( x >= 0 and x < len(grid)) and (y >= 0 and y < len(grid[0])) and (grid[x][y] != 0) and ((x,y) not in visited)
        

