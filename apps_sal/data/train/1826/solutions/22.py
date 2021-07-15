class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
            m,n = len(mat), len(mat[0])
            ans = [[0]*n for i in range(m)]
            prefix = [[0]*(n+1) for i in range(m)]
            for i in range(m):
                for j in range(n):
                    prefix[i][j] = prefix[i][j-1] + mat[i][j]

            for i in range(m):
                for j in range(n):
                    for s in range(k+1):
                        if i-s < 0: break
                        ans[i][j] += prefix[i-s][min(n-1,j+k)]-prefix[i-s][max(-1,j-k-1)]
                    for s in range(1,k+1):
                        if i+s > m-1: break
                        ans[i][j] += prefix[i+s][min(n-1,j+k)]-prefix[i+s][max(-1,j-k-1)]
            return ans 
