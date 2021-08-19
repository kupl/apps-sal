class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat[0])
        for i in range(n):
            ans = ans + mat[i][i] + mat[i][n - i - 1]
        if n % 2 != 0:
            ans = ans - mat[n // 2][n // 2]
        return ans
