class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        (N, M) = (len(mat), len(mat[0]))
        ans = [[0] * M for i in range(N)]

        def getBlockSum(i, j):
            rows = mat[max(0, i - K):i + K + 1]
            block = list(zip(*rows))[max(0, j - K):j + K + 1]
            return sum((sum(blockrow) for blockrow in block))
        for i in range(N):
            for j in range(M):
                ans[i][j] = getBlockSum(i, j)
        return ans
