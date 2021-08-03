class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
        k = K
        row = [[0 for _ in range(n)] for _ in range(m)]
        ans = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for r in range(max(0, i - k), min(m, i + k + 1)):
                    row[i][j] += mat[r][j]

        for i in range(m):
            for j in range(n):
                for c in range(max(0, j - k), min(n, j + k + 1)):
                    ans[i][j] += row[i][c]

        return ans
