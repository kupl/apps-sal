class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        one_counts = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 1:
                    if j < n - 1:
                        one_counts[i][j] += 1 + one_counts[i][j + 1]
                    else:
                        one_counts[i][j] = 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 1:
                    continue
                min_width = sys.maxsize
                for k in range(i, m):
                    min_width = min(min_width, one_counts[k][j])
                    ans += min_width

        return ans
