class Solution:
    '''
    Leetcode1219
    核心思想：backtrack，和之前的题的解题是一模一样的
    '''
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j , gold_so_far):
            self.max_gold = max(self.max_gold, gold_so_far)
            if 0 <= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j] != 0:
                gold_amt = grid[i][j]
                grid[i][j]  = 0
                neigbors = [[i+1, j], [i-1,j], [i, j+1],[i, j-1]]
                for x, y in  neigbors:
                    dfs(x, y, gold_so_far + gold_amt)
                grid[i][j] = gold_amt
            
        
        self.max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    dfs(i, j , 0)
        return self.max_gold
        
#         def search(i, j , gold_so_far):
#             self.max_gold = max(self.max_gold, gold_so_far)
#             if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 0:
#                 gold_amnt = grid[i][j]
#                 grid[i][j] = 0
#                 neigbors = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
#                 for x, y in neigbors:
#                     search(x, y, gold_so_far + gold_amnt)
#                 grid[i][j] = gold_amnt
        
#         self.max_gold = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] > 0:
#                     search(i, j , 0)
#         return self.max_gold
        

