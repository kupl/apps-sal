class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if not mat[i][j]:
                    continue
                mat[i][j] += mat[i - 1][j] if i - 1 >= 0 else 0
        ret = 0
        for i in range(len(mat)):
            row = mat[i]
            stack = []
            tot = 0
            for j in range(len(row)):
                ths = 1
                while stack and stack[-1][0] >= row[j]:
                    popped = stack.pop()
                    tot -= popped[0] * popped[1]
                    ths += popped[1]
                stack.append([row[j], ths])
                tot += ths * row[j]
                ret += tot
        return ret
