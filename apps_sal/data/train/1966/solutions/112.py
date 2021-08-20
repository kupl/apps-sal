class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        mat = [[0] + row for row in mat]
        (m, n) = (len(mat), len(mat[0]))
        result = 0
        for (i, row) in enumerate(mat):
            stack = []
            count = [0] * n
            for j in range(n):
                if row[j] and i:
                    row[j] += mat[i - 1][j]
                while stack and row[stack[-1]] > row[j]:
                    stack.pop()
                if j and row[j]:
                    count[j] = count[stack[-1]] + row[j] * (j - stack[-1])
                    result += count[j]
                stack.append(j)
        return result
