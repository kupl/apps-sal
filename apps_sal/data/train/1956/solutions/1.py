import random
 
 
 class Solution:
 
     def readSudoku(self, board):
         """
         :type board: List[List[str]]
         :rtype: bool
         """
         line = [set(['1', '2', '3', '4', '5', '6', '7', '8', '9']) for _ in range(9)]
         row = [set(['1', '2', '3', '4', '5', '6', '7', '8', '9']) for _ in range(9)]
         box = [set(['1', '2', '3', '4', '5', '6', '7', '8', '9']) for _ in range(9)]
         unfilled = []
         for x in range(9):
             for y in range(9):
                 data = board[x][y]
                 z = x // 3 + 3 * (y // 3)
                 if data != '.':
                     line[x].remove(data)
                     row[y].remove(data)
                     box[z].remove(data)
                 else:
                     unfilled.append((x, y))
         return line, row, box, unfilled
 
     def solveSudoku(self, board):
         """
         :type board: List[List[str]]
         :rtype: void Do not return anything, modify board in-place instead.
         """
         line, row, box, unfilled = self.readSudoku(board)
         possible = {}
         guess = {}
         i = 0
         while 0 <= i < len(unfilled):
             (x, y) = unfilled[i]
             z = x // 3 + 3 * (y // 3)
             if (x, y) not in possible:
                 possible[(x, y)] = line[x] & row[y] & box[z]
             if possible[(x, y)]:
                 guess[(x,y)] = random.choice(list(possible[(x, y)]))
                 board[x][y] = guess[(x,y)]
                 line[x].remove(guess[(x,y)])
                 row[y].remove(guess[(x,y)])
                 box[z].remove(guess[(x,y)])
                 i += 1
             else:
                 del possible[unfilled[i]]
                 i -= 1
                 (x, y) = unfilled[i]
                 z = x // 3 + 3 * (y // 3)
                 possible[(x, y)].remove(guess[(x,y)])
                 line[x].add(guess[(x,y)])
                 row[y].add(guess[(x,y)])
                 box[z].add(guess[(x,y)])
