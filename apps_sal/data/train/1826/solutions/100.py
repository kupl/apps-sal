class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        pre = [[0] * len(mat[0]) for i in range(len(mat))]
        pre2 = [[0] * len(mat[0]) for i in range(len(mat))]
        res = [[0] * len(mat[0]) for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                pre[i][j] = sum(mat[i][y] for y in range(0, j+1))
        for i in range(len(mat)): 
            for j in range(len(mat[0])):
                pre2[i][j] = sum(pre[x][j] for x in range(0, i+1))
        \"\"\"
        [[1,2,3], 1 3 6     1   3   6
         [4,5,6], 4 9 15    5   12  21
         [7,8,9]] 7 15 24   12  27  45
        \"\"\"
        for i in range(len(mat)):
            ru = max(i-K, 0)
            rd = min(i+K, len(mat)-1)
            for j in range(len(mat[0])):
                cl = max(0, j-K)
                cr = min(len(mat[0])-1, j + K)
                v = pre2[rd][cr]
                if ru - 1 >= 0:
                    v -= pre2[ru-1][cr]
                if cl - 1 >= 0:
                    v -= pre2[rd][cl-1]
                if ru - 1 >= 0 and cl - 1 >= 0:
                    v += pre2[ru-1][cl-1]
                res[i][j] = v
        return res
