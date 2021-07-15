class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        answer = [[0 for j in i] for i in mat]
        def calc(mat,a,b,c,d):
            return sum([sum(row[b:d+1])for row in mat[a:c+1]])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                a = i-K if i-K>=0 else 0
                b = j-K if j-K>=0 else 0
                c = i+K if i+K<=len(mat) else len(mat)
                d = j+K if j+K<=len(mat[0]) else len(mat[0])
                answer[i][j]=calc(mat,a,b,c,d)
        return answer
