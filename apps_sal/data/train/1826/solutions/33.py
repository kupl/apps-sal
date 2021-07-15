class Solution:
    def prefix(self, d, i, j):
        if i<0 or j<0:
            return 0
        if i>=len(d):
            i = len(d)-1
        if j>=len(d[0]):
            j = len(d[0])-1
        return d[i][j]
            
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        d = mat
        row = len(mat)
        col = len(mat[0])
        for i in range(row):
            for j in range(col):
                d[i][j]+=self.prefix(d, i-1,j) + self.prefix(d, i,j-1) - self.prefix(d, i-1,j-1)
        res = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                res[i][j] = self.prefix(d, i+k, j+k) \\
                            - self.prefix(d, i+k, j-k-1) \\
                            - self.prefix(d, i-k-1, j+k) \\
                            + self.prefix(d, i-k-1, j-k-1)
                            
        return res
        
