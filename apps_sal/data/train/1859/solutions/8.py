class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: continue
                if i == 0 or j == 0:
                    res += matrix[i][j]
                else:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])+1
                    res += matrix[i][j]
        return res
        
\"\"\"
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0: continue
                if i == 0 or j == 0:
                    res += matrix[i][j]
                    continue
                matrix[i][j] = min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j]) + 1
                #maxS = max(maxS, matrix[i][j])
                res += matrix[i][j]
                #print('res:',res)
        '''
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for z in range(maxS):
                    if matrix[i][j] > z: res += 1
        '''
        print(matrix)
        return res
\"\"\"
                
        
