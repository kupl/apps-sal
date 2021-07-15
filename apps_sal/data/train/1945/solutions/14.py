class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])
        res = 0
        for i in range(n):
            flip = [1-matrix[i][j] for j in range(m) ]
            
            cnt = 0
            for k in range(n):
                if matrix[i] == matrix[k] or flip ==  matrix[k]:
                    cnt += 1
                    
            res = max(res, cnt)
        
        return res

