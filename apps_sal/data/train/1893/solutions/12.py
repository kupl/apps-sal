class Solution:
     def isValidSudoku(self, board):
         """
         :type board: List[List[str]]
         :rtype: bool
         """
         for l in board:
             nums = list(collections.Counter(l).items())
             for term in nums:
                 if term[0] != '.' and term[1] > 1:
                     print(1)
                     return False
 
         for i in range(0, len(board), 3):
             rows = list(zip(*board[i: i + 3]))
             for j in range(0, len(board), 3):
                 nums = list(itertools.chain.from_iterable(rows[j: j + 3]))
                 nums = list(collections.Counter(nums).items())
                 for term in nums:
                     if term[0] != '.' and term[1] > 1:
                         print(3)
                         return False
 
         columns = list(zip(*board))
         for l in columns:
             nums = list(collections.Counter(l).items())
             for term in nums:
                 if term[0] != '.' and term[1] > 1:
                     print(2)
                     return False
 
         return True
