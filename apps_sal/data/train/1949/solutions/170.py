class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        #2D array 
        #0 means no gold 
        #some_num > 0 means there is gold 
        #Return the max gold you can collect with these conditions
        
        #1) IN w.e cell you are collect ALL the gold in that cell 
        #From you position move U D L R 
        #You can't VISIT the same cell more than once. 
        #You can start and stop collecting gold from ANY position in the grid that has some gold.
        visited = set()
        max_path = [0]
        row_len = len(grid)
        col_len = len(grid[0])
        
        def gold_finder(cur_row, cur_col, visited, path_so_far):
            #Can't visit area that is zero. 

            #Out of boundary check 
            if cur_row < 0 or cur_row >= row_len or cur_col < 0 or cur_col >= col_len or grid[cur_row][cur_col] == 0: 
                max_path[0] = max(max_path[0], sum(path_so_far))
                return 
            # if grid[cur_row][cur_col] == 0: 
            #     return 
                
            #If visited we can't visit you again. 
            if (cur_row, cur_col) in visited: 
                return 
            
            visited.add((cur_row,cur_col))
            gold_finder(cur_row + 1, cur_col, visited, path_so_far + [grid[cur_row][cur_col]])
            gold_finder(cur_row - 1, cur_col, visited, path_so_far + [grid[cur_row][cur_col]])
            gold_finder(cur_row , cur_col + 1, visited, path_so_far + [grid[cur_row][cur_col]])
            gold_finder(cur_row, cur_col - 1, visited, path_so_far + [grid[cur_row][cur_col]])
            visited.remove((cur_row,cur_col))
            
            return 
 
        for row in range(row_len):
            for col in range(col_len): 
                gold_finder(row, col, visited, [])
                
                
        # print('before', max_path)
        # max_path = max(max_path)
        # print('after', max_path)
        return max_path[0]
