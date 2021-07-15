import collections
 
 solved_boards = {((1,2,3),(4,5,0)): 0}
 class Solution:
     def slidingPuzzle(self, board):
         """
         :type board: List[List[int]]
         :rtype: int
         """
         asked = tuple(tuple(row) for row in board)
         queue = collections.deque([((1,2,3),(4,5,0))])
         while queue:
             tboard = queue.popleft()
             for next_board in next_boards(tboard):
                 if next_board in solved_boards:
                     continue
                 solved_boards[next_board] = solved_boards[tboard] + 1
                 queue.append(next_board)
         return solved_boards.get(asked, -1)
     
 def next_boards(board):
     board = [list(row) for row in board]
     zy, zx = find_zero(board)
     for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
         nzy, nzx = zy + dy, zx +dx
         if nzy in range(2) and nzx in range(3):
             board[zy][zx],board[nzy][nzx] = board[nzy][nzx],board[zy][zx]
             yield tuple(tuple(row) for row in board)
             board[zy][zx],board[nzy][nzx] = board[nzy][nzx],board[zy][zx]
 
 def find_zero(board):
     for y, row in enumerate(board):
         for x, e in enumerate(row):
             if e == 0:
                 return y,x
