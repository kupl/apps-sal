class Solution:
     def isValidSudoku(self, board):
         """
         :type board: List[List[str]]
         :rtype: bool
         """
         if not board:return False
         checkRow=[[0 for i in range(9)]for j in range(9)]
         checkCol=[[0 for i in range(9)]for j in range(9)]
         checkSq=[[0 for i in range(9)] for j in range(9)]
         for i in range(9):
             for j in range(9):
                 k=i//3*3+j//3
                 if board[i][j]!='.':
                     num=int(board[i][j])-int('0')-1#from 1-9 to 0-8
                     if checkRow[i][num] or checkCol[j][num] or checkSq[k][num]:return False
                     else:checkRow[i][num]=checkCol[j][num]=checkSq[k][num]=1
         return True
