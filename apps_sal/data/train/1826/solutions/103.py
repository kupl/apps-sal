class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        res = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
        
        for i in range(0, min(len(mat), K + 1)):
            for j in range(0, min(len(mat[0]), K + 1)):
                res[0][0] += mat[i][j]
        
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                
                if i == 0 and j == 0:
                    continue
                
                
                if j == 0:
                    
                    res[i][j] = res[i - 1][j]
                    
                    old_i = i - K - 1
                    
                    if old_i >= 0:
                        for curr_j in range(max(0, j - K), min(len(mat[0]), j + K + 1)):
                            res[i][j] -= mat[old_i][curr_j]
                                           
                    
                    new_i = i + K
                    
                    if new_i < len(mat):
                        for curr_j in range(max(0, j - K), min(len(mat[0]), j + K + 1)):
                            res[i][j] += mat[new_i][curr_j]
                else:
                    res[i][j] = res[i][j - 1]
                
                    old_j = j - K - 1
                    
                    if old_j >= 0:
                        for curr_i in range(max(0, i - K), min(len(mat), i + K + 1)):
                            res[i][j] -= mat[curr_i][old_j]

                    new_j = j + K

                    if new_j < len(mat[0]):
                        for curr_i in range(max(0, i - K), min(len(mat), i + K + 1)):
                            res[i][j] += mat[curr_i][new_j]
                        
        return res
                

