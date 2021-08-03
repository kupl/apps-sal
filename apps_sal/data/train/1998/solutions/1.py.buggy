import heapq
 class Solution:
     def tupletize(self, board):
         return  tuple(tuple(row) for row in board)
     
     def slidingPuzzle(self, board):
         """
         :type board: List[List[int]]
         :rtype: int
         """
         heap = [(0, self.tupletize(board))]
         visited = set()
         target = ((1,2,3), (4,5,0))
         while heap:
             new_q = []
             for dist, b in heap:
                 if b in visited:
                     continue
                 visited.add(b)
                     
                 if b == target:
                     return dist
                 
                 x = None
                 y = None
                 for i in range(len(b)):
                     if x is not None: break
                     for j in range(len(b[i])):
                         if b[i][j] == 0:
                             x = i
                             y = j
                             break
                             
                 for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                     if dx >= 0 and dy >= 0 and dx < len(board) and dy < len(board[dx]):
                         newboard = list(list(row) for row in b)
                         newboard[dx][dy], newboard[x][y] = newboard[x][y], newboard[dx][dy]
                         heapq.heappush(new_q, (dist + 1, self.tupletize(newboard)))
                 
             heap = new_q
         
         return -1
