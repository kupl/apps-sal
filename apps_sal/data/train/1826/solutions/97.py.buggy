class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        k = K
\t\t
        cumsum = [[0]*n for _ in range(m)]
        answer = [[0]*n for _ in range(m)]

        cumsum[0][0]=mat[0][0]
        for j in range(1,n):
            cumsum[0][j] = cumsum[0][j-1] + mat[0][j]
        for i in range(1,m):
            cumsum[i][0] = cumsum[i-1][0] + mat[i][0]
        for j in range(1,n):
            for i in range(1,m):
                cumsum[i][j] = cumsum[i][j-1] + cumsum[i-1][j] - cumsum[i-1][j-1] + mat[i][j]
        
        def getcumsum(i,j):
            if i >=0 and j>=0:
                return cumsum[min(max(0,i), m-1)][min(max(0,j), n-1)]
            else: return 0
            
        for r in range(m):
            for c in range(n):
                answer[r][c] = getcumsum(r+k,c+k) - getcumsum(r+k,c-(k+1)) - getcumsum(r-(k+1),c+k) + getcumsum(r-(k+1),c-(k+1))
        return answer
