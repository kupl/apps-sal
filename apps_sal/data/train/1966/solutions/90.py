class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        
        for j in range(col-2,-1,-1):
            for i in range(row):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i][j+1]
        
        res = 0
        for i in range(row):
            for j in range(col):
                MIN = float(\"inf\")
                for k in range(i, row):
                    MIN = min(MIN, mat[k][j])
                    res += MIN
        return res
        
