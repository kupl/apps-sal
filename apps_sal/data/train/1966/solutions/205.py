class Solution:
#     def numSubmat(self, mat: List[List[int]]) -> int:
#         result = 0
#         for i in range(len(mat)):
#             for j in range(len(mat[i])):
#                 if mat[i][j] == 1:
#                     prev_row_width = -1
#                     for row in range(i, len(mat)):
#                         for col in range(j, len(mat[i])):
#                             if mat[row][col] == 1 and (prev_row_width == -1 or col - j + 1 <= prev_row_width):
#                                 result += 1
#                                 # print(\"Prev Width:\", prev_row_width)
#                                 # print(\"Current Width:\", col - j + 1)
#                                 # print(\"Rectangle with coordinates ({}, {}) and ({}, {})\".format(i, j, row, col))
#                             else:
#                                 prev_row_width = col - j
#                                 break
                                    
                        
#         return result

#     def numSubmat(self, mat: List[List[int]]) -> int:
#         result = 0
#         n = len(mat)
#         m = len(mat[0])
#         consecutive_ones = [[0] * m for _ in range(n)]
        
#         for i in range(n):
#             curr_ones = 0
#             for j in range(m - 1, -1, -1):
#                 if mat[i][j] == 1:
#                     curr_ones += 1
#                 else:
#                     curr_ones = 0
#                 consecutive_ones[i][j] = curr_ones
        
#         # print(consecutive_ones)
        
#         for i in range(n):
#             for j in range(m):
#                 if mat[i][j] == 1:
#                     prev_row_width = float('inf')
#                     for row in range(i, n):
#                         curr_width = consecutive_ones[row][j]
#                         # print(\"Prev Width:\", prev_row_width)
#                         # print(\"Current Width:\",curr_width)

#                         if curr_width == 0:
#                             break
                        
#                         # print(\"Rectangle with coordinates ({}, {}) and ({}, {})\".format(i, j, row, j + curr_width - 1))
#                         result += min(prev_row_width, curr_width)
#                         prev_row_width = min(prev_row_width, curr_width)
                        
#         return result

    def numSubmat(self, mat: List[List[int]]) -> int:
        result = 0
        n = len(mat)
        m = len(mat[0])
        consecutive_ones = [[0]*m for _ in range(n)]
        overall_ones = []
        
        for i in range(n):
            c = 0
            for j in range(m - 1, -1, -1):
                if mat[i][j] == 1:
                    c += 1
                    overall_ones.append((i, j))
                else:
                    c = 0
                consecutive_ones[i][j] = c
                
        while len(overall_ones) != 0:
            leftmost_point = overall_ones.pop()
            i = leftmost_point[0]
            j = leftmost_point[1]
            
            prev_row_width = float('inf')
            for row in range(i, n):
                curr_width = consecutive_ones[row][j]
                
                if curr_width == 0:
                    break
                
                result += min(prev_row_width, curr_width)
                prev_row_width = min(prev_row_width, curr_width)
        
                    
        return result
                
                
        
        
        

