class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = 0 
        for i in range(n):
            for j in range(m):
                # count the number of square with left-top corner be res[i][j]
                done = False
                new_i = i
                new_j = j
                
                while 0 <= new_i < n and 0 <= new_j < m and not done:
                    area = 0 
                    for k in range(i,new_i + 1):
                        area += matrix[k][new_j]
                    for k in range(j, new_j + 1):
                        area += matrix[new_i][k]
                    area -= matrix[new_i][new_j]
                        
                    if area == new_j - j + new_i- i + 1:
                        res += 1
                        new_i = new_i + 1
                        new_j = new_j + 1
                    else:
                        done = True
        return res
        

