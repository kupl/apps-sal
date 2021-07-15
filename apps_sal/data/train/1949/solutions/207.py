class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        for line in grid:
            print(line)
        
        def rec(visited, currgold, i ,j, path):
        
            if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0:
                return currgold

            gold = grid[i][j]
            if tuple([i,j]) in visited or gold == 0:
                return currgold
            else:
                visited = visited.copy()
                visited.add(tuple([i,j]))
                path = path.copy()
                path.append([i,j])
                currgold += gold

                return max(
                            rec(visited, currgold, i+1,j,path),
                            rec(visited, currgold, i-1,j,path),
                            rec(visited, currgold, i,j+1,path),
                            rec(visited, currgold, i,j-1,path)
                        )
                        
                
        maxgold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                visited = set()
                path = list()
                g = rec(visited, 0, i, j, path)
                
                if maxgold < g:
                    maxgold = g
        
        return maxgold
    
    
    
    
    \"\"\"
    [1, 0, 7, 0, 0, 0]
    [2, 0, 6, 0, 1, 0]
    [3, 5, 6, 7, 4, 2]
    [4, 3, 1, 0, 2, 0]
    [3, 0, 5, 0, 20,0]

    
    \"\"\"
