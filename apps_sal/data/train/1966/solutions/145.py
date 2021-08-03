class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        for i in range(1, M):
            for j in range(N):
                if mat[i][j]:
                    mat[i][j] += mat[i - 1][j]

        # 3, 5, 2, 1, 0, 4
        # count[0] = 3 * (0 + 1)
        # count[1] = 5 * (1 - 0) + count[0]
        # count[2] = 2 * (2 + 1)
        # count[3] = 1 * (3 + 1)

        result = 0
        for row in mat:
            count = [0] * N
            stk = []
            for i, e in enumerate(row):
                while stk and row[stk[-1]] >= e:
                    stk.pop()

                if stk:
                    count[i] = count[stk[-1]] + e * (i - stk[-1])
                else:
                    count[i] = e * (i + 1)

                stk.append(i)
            result += sum(count)
        return result
