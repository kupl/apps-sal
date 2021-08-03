# observation:
 #1) row swapping resolves adjacent vertical 1s and 0s.
 #   col swapping resolves adjacent horizontal 1s and 0s.
 #2) if mask = all 1s with len of n. then the rows/cols must be
 #   x, x^mask, x, x^mask, ...
 class Solution:
     def movesToChessboard(self, board):
         """
         :type board: List[List[int]]
         :rtype: int
         """
         n = len(board)
         all1s = 2**n - 1
         def countSwap(lines):
             lines = [int(l, base=2) for l in lines]
             x, y = lines.count(lines[0]), lines.count(lines[0] ^ all1s)
             if x + y < n or abs(x - y) > 1:
                 return -1
             nums = [lines[0], lines[0] ^ all1s]
             if x == y:
                 return min(sum(nums[i % 2] != lines[i] for i in range(n)), sum(nums[1 - i % 2] != lines[i] for i in range(n))) // 2
             else:
                 if x < y:
                     nums = [lines[0] ^ all1s, lines[0]]
                 return sum(nums[i % 2] != lines[i] for i in range(n)) // 2
         
         cnt1 = countSwap([''.join(map(str, r)) for r in board])
         cnt2 = countSwap([''.join(str(board[i][j]) for i in range(n)) for j in range(n)])
         if cnt1 < 0 or cnt2 < 0:
             return -1
         return cnt1 + cnt2
         
