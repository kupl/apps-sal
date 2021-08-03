class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def is_ones(lst, n, i, j):
            ones = 0
            for ix in range(i, i + n):
                for jy in range(j, j + n):
                    if lst[ix][jy] == 1:
                        ones += 1
            return ones == n * n

        n = len(matrix)
        m = len(matrix[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    tmp = 1
                    while (i + tmp <= n) and (j + tmp <= m):
                        if is_ones(matrix, tmp, i, j):
                            ans += 1
                            tmp += 1
                        else:
                            break
        return ans
