
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]

        for i in range(m):
            for j in range(n):
                res = 0
                for block_row in range(max(0, i - K), min(m, i + K + 1)):
                    res += mat[block_row][min(n - 1, j + K)]
                    if j - K - 1 >= 0:
                        res -= mat[block_row][j - K - 1]
                ans[i][j] = res
        return ans
