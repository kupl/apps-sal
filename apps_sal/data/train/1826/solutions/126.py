class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        ans = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(1, cols):
                mat[i][j] += mat[i][j - 1]
                if i > 0:
                    mat[i][j - 1] += mat[i - 1][j - 1]
            if i > 0:
                mat[i][cols - 1] += mat[i - 1][cols - 1]

        for i in range(rows):
            for j in range(cols):
                top, bottom, left, right = i, i, j, j

                countT = k
                while top > 0 and countT > 0:
                    top -= 1
                    countT -= 1

                countB = k
                while bottom < rows - 1 and countB > 0:
                    bottom += 1
                    countB -= 1

                countL = k
                while left > 0 and countL > 0:
                    left -= 1
                    countL -= 1

                countR = k
                while right < cols - 1 and countR > 0:
                    right += 1
                    countR -= 1

                ans[i][j] += mat[bottom][right]

                if top - 1 >= 0 and countT == 0:
                    ans[i][j] -= mat[top - 1][right]
                if left - 1 >= 0 and countL == 0:
                    ans[i][j] -= mat[bottom][left - 1]
                if top - 1 >= 0 and left - 1 >= 0 and countT == 0 and countL == 0:
                    ans[i][j] += mat[top - 1][left - 1]

        return ans
