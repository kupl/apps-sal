class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        n = len(matrix)
        m = len(matrix[0])
        pre = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == 1:
                    ans += 1
                pre[i][j] = matrix[i - 1][j - 1]
                if i - 1 >= 0:
                    pre[i][j] += pre[i - 1][j]
                if j - 1 >= 0:
                    pre[i][j] += pre[i][j - 1]
                if i - 1 >= 0 and j - 1 >= 0:
                    pre[i][j] -= pre[i - 1][j - 1]
                c = 2
                while i - c >= 0 and j - c >= 0:
                    if pre[i][j] - pre[i][j - c] - pre[i - c][j] + pre[i - c][j - c] == c**2:
                        ans += 1
                    else:
                        break
                    c += 1
        return ans
