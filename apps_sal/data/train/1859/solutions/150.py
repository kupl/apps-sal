class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def pref(x,y):
            return 0 if x<0 or y<0 else f[x][y]
        rows,cols = len(matrix),len(matrix[0]) if matrix else 0
        res = 0
        f = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                f[i][j] = 0 if matrix[i][j] == 0 else min(pref(i-1,j),pref(i,j-1),pref(i-1,j-1))+1
                res += f[i][j]
        #print(f)
        return res

