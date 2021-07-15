class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        
        padded_mat = []
        for i in range(K):
            padded_mat.append([0]*(n+2*K))
            
        for i in range(m):
            padded_mat.append([0]*K+mat[i]+[0]*K)
            
        for i in range(K):
            padded_mat.append([0]*(n+2*K))
        
        sum_mat = []
        for i in range(m):
            sum_mat.append([0]*n)

        for i in range(m):
            for j in range(n):
                sum_mat[i][j] = sum([sum(row[j:j+2*K+1]) for row in padded_mat[i:i+2*K+1]])
            
        return sum_mat
