class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        count = 0
        for i in range(n):
            c = 0
            for j in range(m-1, -1, -1):
                if mat[i][j]:
                    c += 1
                    mat[i][j] = c
                else:
                    c = 0
                
        for j in range(m):
            for i in range(n):
                if mat[i][j]:
                    min_v = mat[i][j]
                    count += mat[i][j]
                    for k in range(i+1,n):
                        if not mat[k][j]: break
                        min_v = min(min_v, mat[k][j])
                        count+= (k-i+1)*min_v - (k-i)*min_v
        return count
                    
                

