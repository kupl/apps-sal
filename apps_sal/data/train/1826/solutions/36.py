class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        out = [[0 for x in range(0, n)] for y in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                r_low = max(0, i - K)
                r_high = min(i + K, m)
                c_low = max(0, j - K)
                c_high = min(j + K, n)
                s = 0
                for i2 in range(r_low, min(r_high + 1, m)):
                    s += sum(mat[i2][c_low:c_high + 1])
                print((i, j, n, m))
                out[i][j] = s
        return out
