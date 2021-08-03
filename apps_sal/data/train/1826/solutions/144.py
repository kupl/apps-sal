class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for i in range(m)]

        def in_range(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        ans[0][0] = sum([mat[i][j] for i in range(0, K + 1) for j in range(0, K + 1) if in_range(i, j)])

        for r in range(1, m):
            add = sum([mat[r + K][j] for j in range(0, K + 1) if r + K < m and j < n])
            sub = sum([mat[r - K - 1][j] for j in range(0, K + 1) if r - K - 1 >= 0 and j < n])
            ans[r][0] = ans[r - 1][0] + add - sub

        for r in range(0, m):
            for c in range(1, n):
                add = sum([mat[i][c + K] for i in range(r - K, r + K + 1) if i >= 0 and i < m and c + K < n])
                sub = sum([mat[i][c - K - 1] for i in range(r - K, r + K + 1) if i >= 0 and i < m and c - K - 1 >= 0])
                ans[r][c] = ans[r][c - 1] + add - sub

        return ans
