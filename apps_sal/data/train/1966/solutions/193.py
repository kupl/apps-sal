class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0

        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                mat[i][j] = 1 + mat[i][j - 1] if mat[i][j] != 0 else 0

        for j in range(len(mat[0])):

            stack = [(-1, -1)]
            for i in range(len(mat)):
                while stack and mat[i][j] < stack[-1][1]:
                    stack.pop()
                stack.append((i, mat[i][j]))
                mat[i][j] = mat[i][j] * (i - stack[-2][0]) + (mat[stack[-2][0]][j] if stack[-2][0] != -1 else 0)

        return sum([sum(arr) for arr in mat])
