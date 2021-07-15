class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        mx=1
        for i in range(n):
            c=[0 for i in range(m)]
            for j in range(m):
                if(matrix[i][j]==0):
                    c[j]=1
                else:
                    c[j]=0
            count=1
            for j in range(n):
                if(i!=j)and(c==matrix[j])or(matrix[i]==matrix[j]):
                    count+=1
            mx=max(mx,count)
        return mx-1

