class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        a=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==1:
                    if i==0 or j==0:
                        a+=1
                    else:
                        t=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])+matrix[i][j]
                        a+=t
                        matrix[i][j]=t
        return a
                        

