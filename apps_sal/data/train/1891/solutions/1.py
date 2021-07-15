class Solution:
     def helper(self, n, currentIndex, aux, rowsWithQueen, alll):
         for i in range(n):
             if i not in rowsWithQueen:
                 # Verify first diagonal
                 x, y = currentIndex - 1, i - 1
                 while aux[x][y] != 'Q' and x >= 0 and y >= 0:
                     x -= 1
                     y -= 1
                 if x != -1 and y != -1:
                     continue
                 
                 # Verify second diagonal
                 x, y = currentIndex - 1, i + 1
                 while x >= 0 and y < n and aux[x][y] != 'Q':
                     x -= 1
                     y += 1
                 if x != -1 and y != n:
                     continue
                 
                 aux[currentIndex][i] = 'Q'
                 rowsWithQueen.append(i)
 
                 if currentIndex == (n - 1):
                     aw = [[0 for i in range(n)] for j in range(n)]
                     for a in range(n):
                         for b in range(n):
                             aw[a][b] = aux[a][b]
                     alll.append(aw)
                 else:
                     self.helper(n, currentIndex + 1, aux, rowsWithQueen, alll)
 
                 aux[currentIndex][i] = '.'
                 rowsWithQueen.pop()
     def solveNQueens(self, n):
         """
         :type n: int
         :rtype: List[List[str]]
         """
         aux = [['.' for i in range(n)] for j in range(n)]
         rowsWithQueen = []
         alll = []
         
         self.helper(n, 0, aux, rowsWithQueen, alll)
         
         aux = []
         
         for sol in alll:
             ax = []
             for i in sol:
                 i = "".join(i)
                 ax.append(i)
             aux.append(ax)
         return aux

