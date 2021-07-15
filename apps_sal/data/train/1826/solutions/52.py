class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        ans=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                for l in range(max(0,i-K),min(i+K+1,m)):
                    ans[i][j]+=sum(mat[l][max(0,j-K):min(j+K+1,n)])
                    
        return ans
