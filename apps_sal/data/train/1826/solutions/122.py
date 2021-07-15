class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        rsums = [[0] for i in range(r)]
        for i in range(r):
            for j in range(c):
                rsums[i].append(rsums[i][-1]+mat[i][j])
        for i in range(r):
            for j in range(c):
                mat[i][j] = 0
                lr = 0 if i-k < 0 else i-k
                rr = r-1 if i+k >= r else i+k
                lc = 0 if j-k < 0 else j-k
                rc = c-1 if j+k >= c else j+k
                rc += 1
                for x in range(lr, rr+1):
                    mat[i][j] += (rsums[x][rc] - rsums[x][lc])
        return mat
