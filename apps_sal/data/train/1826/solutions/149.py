class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        cum = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if j == 0:
                    cum[i][j] = mat[i][j]
                else:
                    cum[i][j] = cum[i][j - 1] + mat[i][j]

        ans = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]

        # print(cum)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                summ = 0
                for k in range(max(0, i - K), min(len(mat), i + K + 1)):
                    if(j - K - 1 < 0):
                        summ += cum[k][min(j + K, len(cum[i]) - 1)]
                    else:
                        # print(k, len(cum[k]))
                        summ += cum[k][min(j + K, len(cum[k]) - 1)]
                        summ -= cum[k][j - K - 1]
                ans[i][j] = summ
        print(ans)
        return ans
