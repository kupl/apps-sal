class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        res = 0
        for i in  range(n):
            for j in range(m):
                if mat[i][j]:
                    if j: mat[i][j] += mat[i][j-1]
                    width = mat[i][j]
                    k=i
                    while k>=0 and mat[k][j]>0: 
                        width = min(width, mat[k][j])
                        res += width
                        k -= 1
                    
        return res
