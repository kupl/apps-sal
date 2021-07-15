class Solution:
     def validTicTacToe(self, board):
         """
         :type board: List[str]
         :rtype: bool
         """
         x = 0
         o = 0
         win_o = 0
         win_x = 0
         for i in range(3):
             for j in range(3):
                 if board[i][j] == 'X':
                     x += 1
                 elif board[i][j] == 'O':
                     o += 1
             if board[i] == 'XXX': 
                 win_x += 1 
             elif board[i] == 'OOO': 
                 win_o += 1
             if board[0][i] == board[1][i] == board[2][i]:
                 if board[0][i] == 'X':
                     win_x += 1
                 elif board[0][i] == 'O':
                     win_o += 1
 
         if board[0][0] == board[1][1] == board[2][2]:
             if board[0][0] == 'O':
                 win_o += 1
             elif board[0][0] == 'X':
                 win_x += 1
         if board[2][0] == board[1][1] == board[0][2]:
             if board[2][0] == 'O':
                 win_o += 1
             elif board[2][0] == 'X':
                 win_x += 1
 
         if x > (o + 1) or x < o or (win_o > 0 and win_x > 0):
             return False
         
         if win_x > 0 and x == o:
             return False
         
         if win_o > 0 and x > o:
             return False
 
         return True
                     

