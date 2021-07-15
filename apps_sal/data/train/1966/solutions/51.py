class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        n=len(mat)
        m=len(mat[0])

        counts=[[0]*m for j in range(n)]
        
        for i in range(n):
            for j in range(m-1, -1, -1):
                if mat[i][j]==1:
                    counts[i][j]+=1+(counts[i][j+1] if j+1<m else 0)
        res=0            
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    mins=float('inf')
                    for k in range(i, n):
                        mins=min(mins, counts[k][j])
                        res+=mins
                        
        return res
