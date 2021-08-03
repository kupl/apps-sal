from copy import deepcopy
 from collections import deque
 
 class Solution:
     def slidingPuzzle(self, board):
         """
         :type board: List[List[int]]
         :rtype: int
         """
         
         n, m = len(board), len(board[0])
 
         def isValid():
             def getNumberOfInversions():
                 boardInOneLine = []
                 for line in board:
                     for el in line:
                         if el != 0:
                             boardInOneLine.append(el)
 
                 inversions = 0
                 for i, l in enumerate(boardInOneLine):
                     for r in boardInOneLine[i+1:]:
                         inversions += (l > r)
                 return inversions
 
             inversions = getNumberOfInversions()
             if m%2 == 1:
                 return inversions%2 == 0
 
             def getBlankRow():
                 for i, line in enumerate(board):
                     if 0 in line:
                         return i
 
             blankRow = getBlankRow
             if inversions%2 == 0 and blankRow%2 == 1:
                 return True
             if inversions%2 == 1 and blankRow%2 == 0:
                 return True
             return False
         
         if not isValid():
             return -1
 
         def toTuple(mat):
             return tuple(tuple(line) for line in mat)
 
         def toList(mat):
             return list(list(line) for line in mat)
 
         
         def getSolution():
             sol = []
             for line in range(n):
                 sol.append([])
                 for column in range(1,m+1):
                     sol[-1].append(column+line*m)
             sol[-1][-1] = 0
             return toTuple(sol)
         
         sol = getSolution()
         h = deque([(toTuple(board),0)])
         visited = set()
         while True:
             board, count = h.popleft()
             if board == sol:
                 return count
             elif board in visited:
                 continue
             visited.add(board)
             board = toList(board)
             
             def findBlack():
                 for i, line in enumerate(board):
                     for j, el in enumerate(line):
                         if el == 0:
                             return (i,j)
 
             bx, by = findBlack()
 
             def isValidPosition(x,y):
                 return 0 <= x < n and 0 <= y < m
 
             for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                 if isValidPosition(dx+bx,dy+by):
                     nboard = toList(deepcopy(board))
                     nboard[bx][by], nboard[bx+dx][by+dy] = nboard[bx+dx][by+dy], nboard[bx][by]
                     h.append((toTuple(nboard),count+1))
 
 
         return -1
 

