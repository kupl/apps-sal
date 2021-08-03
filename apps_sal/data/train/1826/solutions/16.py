class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        acc = [[0] + list(accumulate(m)) for m in mat]
        print(acc)
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(max(i - K, 0), min(i + K, m - 1) + 1):
                    l, r = max(j - K, 0), min(j + K, n - 1)
                    ans[i][j] += acc[k][r + 1] - acc[k][l]
        return ans
