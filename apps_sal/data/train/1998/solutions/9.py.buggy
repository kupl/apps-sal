from collections import deque
 
 class Solution:
     def slidingPuzzle(self, board):
         """
         :type board: List[List[int]]
         :rtype: int
         """
         t = tuple(board[0]), tuple(board[1])
         v,q = set([t]), deque([(t, 0)])
         
         def addNeighbor(i, j, a, b, steps):
             if 0 <= a < 2 and 0 <= b < 3:
                 board[i][j], board[a][b] = board[a][b], board[i][j]
                 t = tuple(board[0]), tuple(board[1])
                 if t not in v:
                     v.add(t)
                     q.append((t, steps + 1))
                 board[i][j], board[a][b] = board[a][b], board[i][j]
         
         while q:
             t, steps = q.popleft()
             if t == ((1, 2, 3), (4, 5, 0)):
                 return steps
             
             board[0], board[1] = list(t[0]), list(t[1])
             for i in range(2):
                 for j in range(3):
                     if board[i][j] == 0:
                         addNeighbor(i, j, i - 1, j, steps)
                         addNeighbor(i, j, i + 1, j, steps)
                         addNeighbor(i, j, i, j - 1, steps)
                         addNeighbor(i, j, i, j + 1, steps)
         
         return -1
