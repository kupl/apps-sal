class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        iMax = len(mat)
        jMax = len(mat[0])
        ans = [[0 for j in range(jMax)] for i in range(iMax)]

        i = 0
        j = 0
        ans[i][j] = sum([sum([mat[i0][j0] for j0 in range(j, min(jMax, j + K + 1))]) for i0 in range(i, min(iMax, i + K + 1))])
        # print(ans)

        i = 0
        for j in range(1, jMax):
            ans[i][j] = ans[i][j - 1]
            if j + K < jMax:
                ans[i][j] += sum([mat[i0][j + K] for i0 in range(max(0, i - K), min(iMax, i + K + 1))])
            if j - K - 1 >= 0:
                ans[i][j] -= sum([mat[i0][j - K - 1] for i0 in range(max(0, i - K), min(iMax, i + K + 1))])
        # print(ans)

        j = 0
        for i in range(1, iMax):
            ans[i][j] = ans[i - 1][j]
            if i + K < iMax:
                ans[i][j] += sum([mat[i + K][j0] for j0 in range(max(0, j - K), min(jMax, j + K + 1))])
            if i - K - 1 >= 0:
                ans[i][j] -= sum([mat[i - K - 1][j0] for j0 in range(max(0, j - K), min(jMax, j + K + 1))])

        for i in range(1, iMax):
            for j in range(1, jMax):
                ans[i][j] = ans[i][j - 1]
                if j + K < jMax:
                    ans[i][j] += sum([mat[i0][j + K] for i0 in range(max(0, i - K), min(iMax, i + K + 1))])
                if j - K - 1 >= 0:
                    ans[i][j] -= sum([mat[i0][j - K - 1] for i0 in range(max(0, i - K), min(iMax, i + K + 1))])

        # print(ans)
        return ans
#         for i in range(iMax):
#             for j in range(jMax):
#                 if i == 0 and j== 0:
#                     continue
