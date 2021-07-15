class Solution:
     def isValidSudoku(self, board):
         """
         :type board: List[List[str]]
         :rtype: bool
         """
         for row in board:
             seen = 0
             for col in row:
                 if col.isdigit():
                     if seen >> int(col) & 1:
                         return False
                     else:
                         seen |= 1<<int(col)
         max = 9
         for col in range(max):
             seen = 0
             for row in range(max):
                 val = board[row][col]
                 if val.isdigit():
                     if seen >> int(val) & 1:
                         return False
                     else:
                         seen |= 1<<int(val)
         for row_st in range(0, max, 3):
             for col_st in range(0, max, 3):
                 seen = 0
                 for row in range(3):
                     for col in range(3):
                         val = board[row_st + row][col_st+ col]
                         print(val)
                         if val.isdigit():
                             if seen >> int(val) & 1:
                                 return False
                             else:
                                 seen |= 1<<int(val)
         
         return True
