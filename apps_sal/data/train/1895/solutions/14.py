class Solution:
     def playerWon(self, board, player):
         for i in range(3):
             if board[0][i] == board[1][i] == board[2][i] == player:
                 return True
         for i in range(3):
             if board[i][0] == board[i][1] == board[i][2] == player:
                 return True
         if board[0][0] == board[1][1] == board [2][2] == player or\
         board[0][2] == board[1][1] == board[2][0] == player:
             return True
         return False
 
     def validTicTacToe(self, board):
         """
         :type board: List[str]
         :rtype: bool
         """
         count_x = sum(b.count("X") for b in board)
         count_o = sum(b.count("O") for b in board)
         if count_x - count_o > 1 or count_x - count_o < 0:
             return False
         if self.playerWon(board, "X") and count_x - count_o != 1:
             return False
         if self.playerWon(board, "O") and count_x - count_o != 0:
             return False
         return True
