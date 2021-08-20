class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        answer = [[None for _ in range(len(mat[0]))] for __ in range(len(mat))]
        prefix_sum = [[0 for _ in range(len(mat[0]))] for __ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                prefix_sum[i][j] += mat[i][j]
                prefix_sum[i][j] += prefix_sum[i - 1][j] if 0 <= i - 1 else 0
                prefix_sum[i][j] += prefix_sum[i][j - 1] if 0 <= j - 1 else 0
                prefix_sum[i][j] -= prefix_sum[i - 1][j - 1] if 0 <= i - 1 and 0 <= j - 1 else 0
        print(prefix_sum)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                bottom_right = prefix_sum[min(i + K, len(mat) - 1)][min(j + K, len(mat[0]) - 1)]
                bottom_left = prefix_sum[min(i + K, len(mat) - 1)][j - K - 1] if j - K - 1 >= 0 else 0
                top_left = prefix_sum[i - K - 1][j - K - 1] if 0 <= i - K - 1 and 0 <= j - K - 1 else 0
                top_right = prefix_sum[i - K - 1][min(j + K, len(mat[0]) - 1)] if 0 <= i - K - 1 else 0
                answer[i][j] = bottom_right - bottom_left - top_right + top_left
        return answer
