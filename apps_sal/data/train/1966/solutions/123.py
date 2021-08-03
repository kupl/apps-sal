class Solution:
    def numSubmat(self, mat):
        if not mat:
            return 0
        row, col = len(mat), len(mat[0])
        for r in range(row):
            for c in range(col):
                if mat[r][c] >= 1 and r:
                    mat[r][c] += mat[r - 1][c]
        answer = 0
        for row in mat:
            stack = [-1]
            num_submatrices = 0
            for i, num in enumerate(row):
                while stack[-1] != -1 and num <= row[stack[-1]]:
                    larger_num_idx = stack.pop()
                    num_submatrices -= row[larger_num_idx] * (larger_num_idx - stack[-1])
                num_submatrices += num * (i - stack[-1])
                answer += num_submatrices
                stack.append(i)
        return answer
