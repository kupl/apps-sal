class Solution:
     def solveNQueens(self, n):
         """
         :type n: int
         :rtype: List[List[str]]
         """
         queens = []
         res = []
         def backtracking(n, k, queens):
             if k > n:
                 return
             elif len(queens) == n and k < n:
                 return
             elif len(queens) == n and k == n:
                 temp = queens[:]                
                 res.append(temp)
             else:
                 row =[0] * n
                 temp_q = queens[:]
                 for each in  temp_q:
                     x, y = each[0], each[1]
                     
                     row[y] = 1
                     if y + k - x < n:
                         row[y + k - x] = 1
                     if y - k + x >= 0:
                         row[y - k + x] = 1
                 
                 for i in range(n):
                     if row[i] == 0:
                         temp_q.append((k,i))
                         # print(temp_q)
                         backtracking(n, k + 1, temp_q)
                         temp_q.pop()
                 
                 
                 
         backtracking(n, 0, queens)
         
         layout = []
         for q in res:
             temp = []
             for each in q:
                 _row = "." * each[1] + "Q" + "." * (n - each[1] - 1)
                 temp.append(_row)
             layout.append(temp)
         return layout
