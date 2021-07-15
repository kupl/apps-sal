class Solution:
    
    
    
    def find_square(self, grid, val):
        for i in range(0, len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == val:
                    return (i,j)
        return (-1,-1)
    
    def count_empty_squares(self, grid):
        empty_sq = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    empty_sq += 1
        return empty_sq
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_square = self.find_square(grid, 1)
        end_sq = self.find_square(grid, 2)
        empty_squares = self.count_empty_squares(grid) + 1
        
        
        def unique_paths_backtracking(grid, cur_sq, count):
            if count == empty_squares:
                if cur_sq == end_sq:
                    return 1
                return 0
            elif cur_sq == end_sq or \\
                not (0 <= cur_sq[0] < len(grid)) or \\
                not (0 <= cur_sq[1] < len(grid[0])) or \\
                grid[cur_sq[0]][cur_sq[1]] < 0:
                return 0

            grid[cur_sq[0]][cur_sq[1]] = -2
            u = unique_paths_backtracking(grid, (cur_sq[0]-1,cur_sq[1]), count+1)
            grid[cur_sq[0]][cur_sq[1]] = 0
            
            grid[cur_sq[0]][cur_sq[1]] = -2
            d = unique_paths_backtracking(grid, (cur_sq[0]+1,cur_sq[1]), count+1)
            grid[cur_sq[0]][cur_sq[1]] = 0
            
            grid[cur_sq[0]][cur_sq[1]] = -2
            l = unique_paths_backtracking(grid, (cur_sq[0],cur_sq[1]-1), count+1)
            grid[cur_sq[0]][cur_sq[1]] = 0
            
            grid[cur_sq[0]][cur_sq[1]] = -2
            r = unique_paths_backtracking(grid, (cur_sq[0],cur_sq[1]+1), count+1)
            grid[cur_sq[0]][cur_sq[1]] = 0
            
            return u + d + l + r
        
        
        return unique_paths_backtracking(grid, start_square, 0)
    
\"\"\"
1) Find starting square and ending square (write fn to do this)
2) Count number of empty squares
2) Fail conditions: 
    - we cannot travel any direction since we already visited them
    - we reach ending square but haven't stepped on every empty square
    - we reach an obstacle so terminate that path
3) Success:
    - squares explored == empty_squares and cur location is end_square idx
4) Increment a unique path counter every time we hit success condition

Runtime: O(4^(N*M))
Space: O(N*M)
\"\"\"
