class Solution:    
     def repeat(self, val, seen):
             print((val, seen))
             return seen >> int(val) & 1
 
     def isValidSudoku(self, board):
         """
         :type board: List[List[str]]
         :rtype: bool
         """
         seen = set()
         for i in range(9):
             for j in range(9):
                 if board[i][j].isdigit():
                     val = board[i][j]
                     row = (i, val)
                     col = (val, j)
                     box = (i//3, j//3, val)
                     if row in seen or col in seen or box in seen:
                         return False
                     seen.add(row)
                     seen.add(col)
                     seen.add(box)
                     
         return True
         # for row in board:
         #     seen = 0
         #     for col in row:
         #         if col.isdigit():
         #             if seen >> int(col) & 1:
         #                 return False
         #             else:
         #                 seen |= 1<<int(col)
         # max = 9
         # for col in range(max):
         #     seen = 0
         #     for row in range(max):
         #         val = board[row][col]
         #         if val.isdigit():
         #             if seen >> int(val) & 1:
         #                 return False
         #             else:
         #                 seen |= 1<<int(val)
         # for row_st in range(0, max, 3):
         #     for col_st in range(0, max, 3):
         #         seen = 0
         #         for row in range(3):
         #             for col in range(3):
         #                 val = board[row_st + row][col_st+ col]
         #                 print(val)
         #                 if val.isdigit():
         #                     if seen >> int(val) & 1:
         #                         return False
         #                     else:
         #                         seen |= 1<<int(val)

