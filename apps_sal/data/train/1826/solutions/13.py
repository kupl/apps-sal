# class Solution:
#     def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

#         row = len(mat)
#         col = len(mat[0])

#         answer = [[0 for i in range(col)] for j in range(row)]

#         for i in range(row):
#             for j in range(1,col):
#                 # answer[i][j] = self.new_matrix(mat,i,j,K,row,col)
#                 mat[i][j] = mat[i][j-1]+mat[i][j]
#         print(mat)

#         for i in range(row):
#             for j in range(col):
#                 answer[i][j] = self.new_matrix(mat,i,j,K,row,col)
#         return answer

#     def new_matrix(self,mat,i,j,k,row,col):
#         ans = 0
#         new_row_low = i-k
#         new_row_high = i + k
#         new_col_low = j-k
#         new_col_high = j+k


#         while(new_row_low < 0):
#             new_row_low +=1
#         while(new_row_high > row-1):
#             new_row_high -=1
#         while(new_col_low < 0):
#             new_col_low +=1
#         while(new_col_high > col-1):
#             new_col_high-=1


#         for a in range(new_row_low, new_row_high+1):

#             ans+= mat[a][new_col_high]

#             if(new_col_low-1 >= 0):

#                 ans -= mat[a][new_col_low-1]

#         return ans


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        blockSum = [[0] * len(mat[0]) for _ in range(len(mat))]

        accumSum = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                accumSum[x + 1][y + 1] = (accumSum[x][y + 1] if x >= 0 else 0) + (accumSum[x + 1][y] if y >= 0 else 0) - (accumSum[x][y] if x >= 0 and y >= 0 else 0) + mat[x][y]

        for x in range(len(mat)):
            for y in range(len(mat[0])):
                blockSum[x][y] = accumSum[max(x - K, 0)][max(y - K, 0)] + accumSum[min(x + K + 1, len(mat))][min(y + K + 1, len(mat[0]))] - accumSum[max(x - K, 0)][min(y + K + 1, len(mat[0]))] - accumSum[min(x + K + 1, len(mat))][max(y - K, 0)]

        return blockSum
