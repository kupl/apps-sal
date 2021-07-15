class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])

        for i in range(r): 
            for j in range(c-2,-1,-1):
                if mat[i][j] == 1:
                    if j < (c-1):
                        mat[i][j] += mat[i][j+1]
        
        res = 0
        print(mat)
        
        for i in range(r):
            for j in range(c):
                m = float('inf')
                for k in range(i,r):
                    m = min(m, mat[k][j])
                    res += m
        
        return res
