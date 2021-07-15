class Solution:
     def isValidSudoku(self, board):
         """
         :type board: List[List[str]]
         :rtype: bool
         """
         seen = sum(([(c, i), (j, c), (i//3, j//3, c)]
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)
                 if c != '.'), [])
         print(seen)
         return len(seen) == len(set(seen))

