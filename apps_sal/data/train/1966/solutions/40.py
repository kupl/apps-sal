# class Solution:
#     def numSubmat(self, mat: List[List[int]]) -> int:
#         n, m = len(mat), len(mat[0])
#         cache = {}
        
#         for rows in range(1, n + 1):
#             for cols in range(1, m + 1):
#                 for i in range(n):
#                     for j in range(m):
                        
#                         if i + rows <= n and j + cols <= m:
#                             if rows == 1 and cols == 1:
#                                 if mat[i][j] == 1:
#                                     cache[(i, j, rows, cols)] = 1
#                             else:
#                                 if rows > 1 and (i, j, rows - 1, cols) in cache and (i + rows - 1, j, 1, cols) in cache:
#                                     cache[(i, j, rows, cols)] = 1

#                                 elif cols > 1 and (i, j, rows, cols - 1) in cache and (i, j + cols - 1, rows, 1) in cache:
#                                     cache[(i, j, rows, cols)] = 1
        
#         return len(cache)

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        
        def num_submat_at(a, b):
            c = 0
            bound = m
            
            i = a
            while i < n:
                j = b
                while j < bound:
                    if mat[i][j]:
                        c += 1
                    else:
                        bound = j
                    
                    j += 1
                i += 1
            return c
    
        total_c = 0
        for i in range(n):
            for j in range(m):
                total_c += num_submat_at(i, j)

        return total_c
