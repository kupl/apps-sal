class Solution:
     def validTicTacToe(self, board):
         """
         :type board: List[str]
         :rtype: bool
         """
         def win(board,w):
             for i in range(3):
                 if board[i] == w*3:
                     return True
             for i in range(3):
                 if board[0][i] == w and board[1][i] == w and board[2][i] == w:
                     return True
             sign = True
             for i in range(3):
                 if board[i][i] != w:
                     sign = False
             if sign:
                 return True
             
             sign = True
             for i in range(3):
                 if board[i][2-i] != w:
                     sign = False
             if sign:
                 return True
         
         Xnum = 0
         Onum = 0
         for ss in board:
             for s in ss:
                 if s == 'X':
                     Xnum += 1
                 if s == 'O':
                     Onum += 1
         if win(board,'X'):
             if Xnum == Onum + 1:
                 return True
             else:
                 return False
         if win(board,"O"):
             if Xnum == Onum:
                 return True
             else:
                 return False
         if Xnum == Onum or Xnum == Onum + 1:
             return True
         else:
             return False

