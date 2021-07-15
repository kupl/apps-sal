class Solution:
    
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    def __init__(self):
        self.count = 0
    
    @staticmethod
    def _on_board(board, row, col):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])
    
    def _dfs(self, board, row, col, visited) -> bool:
        if (row, col) in visited:
            return True
        
        if not Solution._on_board(board, row, col):
            return False
        
        if board[row][col] == 1:
            return True
        
        visited.add((row, col))
        res = True
        for d in Solution.directions:
            new_row = row + d[0]
            new_col = col + d[1]
            
            if not self._dfs(board, new_row, new_col, visited):
                res = False
        
        return res
            
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''
        DFS
        '''
        if not grid or not grid[0]:
            return 0
        
        cnt = 0
        visited = set()
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 0 and\\
                    (m, n) not in visited and\\
                    self._dfs(grid, m, n, visited):
                    cnt += 1
                    
        return cnt
