class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        for i in range(1, M):
            for j in range(N):
                if mat[i][j]:
                    mat[i][j] += mat[i - 1][j]

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
