class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dic = {}
        for i, row in enumerate(mat):
            prefix_sum = [0] * (cols + 1)
            for j, num in enumerate(row):
                prefix_sum[j] = prefix_sum[j - 1] + num
            dic[i] = prefix_sum

        for i in range(rows):
            for j in range(cols):
                start_col, end_col = max(j - K, 0), min(j + K, cols - 1)
                start_row, end_row = max(i - K, 0), min(i + K, rows - 1)
                res = 0
                for idx in range(start_row, end_row + 1):
                    res += dic[idx][end_col] - dic[idx][start_col - 1]
                mat[i][j] = res
        return mat
