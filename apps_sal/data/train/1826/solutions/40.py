class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n= len(mat)
        m = len(mat[0])
        matx = []
        for i in range (n):
            row = []
            for j in range (m):
                summ = 0
                for y in range (max(0,i-K),min(n,i+K+1)):
                    summ = summ + sum(mat[y][max(0,j-K):min(m,j+K+1)])
                row.append(summ)
            print (row)
            matx.append(row)
        return(matx)
