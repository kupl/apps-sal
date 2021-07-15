class Solution:
     def validTicTacToe(self, board):
         """
         :type board: List[str]
         :rtype: bool
         """
         xoDict = {"X":[],"O":[]," ":[]}
         
         for i in range(0, 3):
             for j in range(0,3):
                 if board[i][j] == "X":
                     xoDict["X"] += [i,j],
                 elif board[i][j] == "O":
                     xoDict["O"] += [i,j],
                 elif board[i][j] == " ":
                     xoDict[" "] += [i,j],
                     
         if len(xoDict["O"])>len(xoDict["X"]):
             return False
         
         if len(xoDict["X"]) - len(xoDict["O"]) >1:
             return False
         
         xwin = self.check(board, "X")
         owin = self.check(board, "O")
         
         if xwin and owin:
             return False
         
         if xwin and len(xoDict["X"]) == len(xoDict["O"]):
             return False
         if owin and len(xoDict["X"]) > len(xoDict["O"]):
             return False
         
         return True
     
     def check(self, board, char):
         for i in range(0,3):
             if board[i][0] == char and board[i][1] ==char and board[i][2] == char:
                 return True
             
         for i in range(0,3):
             if board[0][i] == char and board[1][i] ==char and board[2][i] == char:
                 return True
             
         if board[0][0] == char and board[1][1] ==char and board[2][2] == char:
             return True
         
         if board[0][2] == char and board[1][1] ==char and board[2][0] == char:
             return True
         
         return False
         
     
     
                     
         

