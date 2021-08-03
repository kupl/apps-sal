class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        res = []
        for i in range(len(mat)):
            row = []
            for j in range(len(mat[0])):
                # print(mat[i][j])
                # find the index limits of sub matrix
                up = max(i - K, 0)
                bottom = min(i + K, len(mat) - 1)
                left = max(j - K, 0)
                right = min(j + K, len(mat[0]) - 1)
                sum = 0
                for x in range(up, bottom + 1):
                    for y in range(left, right + 1):
                        sum += mat[x][y]
                row.append(sum)
            res.append(row)
        return res
