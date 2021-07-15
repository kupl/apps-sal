class Solution:
     def validTicTacToe(self, board):
         """
         :type board: List[str]
         :rtype: bool
         """
         cross = 0
         circle = 0
         for i in range(3):
             for j in range(3):
                 if board[i][j] == 'X':
                     cross += 1
                 if board[i][j] == 'O':
                     circle += 1
         if cross < circle or cross - circle > 1:
             return False
         cross_winning = 0
         circle_winning = 0
         for i in range(3):
             if board[i][0] == board[i][1] == board[i][2]:
                 if board[i][0] == 'X':
                     cross_winning += 1
                 elif board[i][0] == 'O':
                     circle_winning += 1
             if board[0][i] == board[1][i] == board[2][i]:
                 if board[0][i] == 'X':
                     cross_winning += 1
                 elif board[0][i] == 'O':
                     circle_winning += 1
         if board[0][0] == board[1][1] == board[2][2]:
             if board[0][0] == 'X':
                 cross_winning += 1
             elif board[0][0] == 'O':
                 circle_winning += 1
         if board[0][2] == board[1][1] == board[2][0]:
             if board[0][2] == 'X':
                 cross_winning += 1
             elif board[0][2] == 'O':
                 circle_winning += 1
                 
         if cross_winning > 0 and circle_winning > 0:
             return False
         if cross_winning > 0 and cross <= circle:
             return False
         if circle_winning > 0 and circle < cross:
             return False
         return True
