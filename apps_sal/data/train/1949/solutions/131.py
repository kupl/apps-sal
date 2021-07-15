class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        #want max gold with conditions
        # collect all gold in cell
        # up right left down
        # cant visit more than 1
        # never visit 0 cell
        # start and stop at any position
        
        max_gold = []
        def dfs(curr_row, curr_col, seen, curr_gold):
            if curr_row < 0 or curr_row >= row_len \\
                or curr_col < 0 or curr_col >= col_len \\
                or grid[curr_row][curr_col] == 0:
                return curr_gold
            
            if (curr_row, curr_col) in seen:
                return curr_gold
            
            seen.add((curr_row, curr_col))
            for nxt_row, nxt_col in [(curr_row+1, curr_col), \\
                                     (curr_row-1, curr_col), \\
                                     (curr_row, curr_col+1), \\
                                     (curr_row, curr_col-1)]:
            
                max_gold.append(dfs(nxt_row, nxt_col, seen, curr_gold + grid[curr_row][curr_col]))
            
            seen.discard((curr_row, curr_col))
            return curr_gold
        
        
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        for row in range(row_len):
            for col in range(col_len):
                dfs(row, col, set(), 0)
        return max(max_gold)
