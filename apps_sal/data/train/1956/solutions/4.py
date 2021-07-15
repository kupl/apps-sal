class Solution:
     def reduceSingleOption(self, board, emptyGrid, valid):
         m = 1
         while m == 1:
             m = 10
             for k in range(len(emptyGrid) - 1, -1, -1):
                 i, j = emptyGrid[k]
                 option = set.intersection(valid[i],
                                           valid[j + 9],
                                           valid[(i // 3) * 3 + j // 3 + 18])
                 if not option:
                     return
                 if len(option) < m:
                     m = len(option)
                 if len(option) == 1:
                     option = option.pop()
                     board[i][j] = str(option)
                     emptyGrid.pop(k)
                     valid[i].remove(option)
                     valid[j + 9].remove(option)
                     valid[(i // 3) * 3 + j // 3 + 18].remove(option)
 
     def dfs(self, board, emptyGrid, valid, ans):
         if len(ans) == len(emptyGrid):
             return
         i, j = emptyGrid[len(ans)]
         options = set.intersection(valid[i],
                                    valid[j + 9],
                                    valid[(i // 3) * 3 + j // 3 + 18])
         if len(options) == 0:
             return
         else:
             for temp in options:
                 print(i, j, temp)
                 ans.append(temp)
                 valid[i].remove(temp)
                 valid[j + 9].remove(temp)
                 valid[(i // 3) * 3 + j // 3 + 18].remove(temp)
                 self.dfs(board, emptyGrid, valid, ans)
                 if len(ans) == len(emptyGrid):
                     break
                 temp = ans.pop()
                 valid[i].add(temp)
                 valid[j + 9].add(temp)
                 valid[(i // 3) * 3 + j // 3 + 18].add(temp)
 
 
     def solveSudoku(self, board):
         """
         :type board: List[List[str]]
         :rtype: void Do not return anything, modify board in-place instead.
         """
         valid = [set(range(1, 10)) for _ in range(27)]
         emptyGrid = []
         for i in range(9):
             for j in range(9):
                 c = board[i][j]
                 if c != '.':
                     n = int(c)
                     valid[i].remove(n)
                     valid[j + 9].remove(n)
                     valid[(i // 3) * 3 + j // 3 + 18].remove(n)
                 else:
                     emptyGrid.append((i, j))
         self.reduceSingleOption(board, emptyGrid, valid)
         ans = []
         self.dfs(board, emptyGrid, valid, ans)
         print(ans)
         for k in range(len(emptyGrid)):
             i, j = emptyGrid[k]
             board[i][j] = str(ans[k])
