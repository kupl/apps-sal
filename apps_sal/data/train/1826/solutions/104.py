class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        height = len(mat)
        width = len(mat[0])
        prefix_sum = [[0] * width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                up = prefix_sum[i - 1][j] if i > 0 else 0
                left = prefix_sum[i][j - 1] if j > 0 else 0
                diag = prefix_sum[i - 1][j - 1] if i > 0 and j > 0 else 0
                prefix_sum[i][j] = up + left - diag + mat[i][j]
        answer = [[0] * width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                lri = min(height - 1, i + K)
                lrj = min(width - 1, j + K)
                uli = i - K - 1
                ulj = j - K - 1
                total = prefix_sum[lri][lrj]
                up = prefix_sum[uli][lrj] if uli >= 0 else 0
                left = prefix_sum[lri][ulj] if ulj >= 0 else 0
                diag = prefix_sum[uli][ulj] if uli >= 0 and ulj >= 0 else 0
                answer[i][j] = total - up - left + diag
        return answer
