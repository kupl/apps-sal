class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        res = [[0 for _ in range(1 + len(matrix[0]))] for _ in range(1 + len(matrix))]
        s = 0
        m = 0
        for i in range(1, len(res)):
            for j in range(1, len(res[i])):

                if matrix[i - 1][j - 1] == 1:
                    res[i][j] = 1 + min(res[i - 1][j], res[i][j - 1], res[i - 1][j - 1])
                else:
                    res[i][j] = 0

                s += res[i][j]
                m = res[i][j] if res[i][j] > m else m

        # for x in res:
        #     print(x)

        # ########### To Find Max Square Matrix size ###################
        # print(m)
        # return m

        return s
