class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(row, col, visited):
            if (row, col) in visited or grid[row][col] == 0:
                return 0
            
            next_visited = visited | set([(row, col)])
            next_pos = [
                (row-1, col),
                (row+1, col),
                (row, col-1),
                (row, col+1),
            ]

            max_child = 0
            for (next_row, next_col) in next_pos:
                if -1 < next_row < n and -1 < next_col < m:
                    max_child = max(max_child, dfs(next_row, next_col, next_visited))
            
            return grid[row][col] + max_child
        
        n = len(grid)
        m = len(grid[0])
        
        max_gold = 0
        for i in range(n):
            for j in range(m):
                max_gold = max(max_gold, dfs(i, j, set()))
                
        return max_gold
