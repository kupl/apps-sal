class Solution:
     def isValidSudoku(self, board):
         """
         :type board: List[List[str]]
         :rtype: bool
         """
         check = set()
         for i in range(0, 9):
             for j in range(0, 9):
                 if (board[i][j] == '.'):
                     continue
                 if (board[i][j] in check):
                     return False
                 check.add(board[i][j])
             check.clear()
         
         for j in range(0,9):
             for i in range(0,9):
                 if (board[i][j] == "."):
                     continue
                 if (board[i][j] in check):
                     return False
                 check.add(board[i][j])
             check.clear()
             
         for k in range(0, 9):
             for i in range(int(k / 3) * 3, int(k / 3) * 3 + 3):
                 for j in range((k % 3) * 3, (k % 3) * 3 + 3):
                     if (board[i][j] == '.'):
                         continue
                     if (board[i][j] in check):
                         return False
                     check.add(board[i][j])
             check.clear()
     
         return True
