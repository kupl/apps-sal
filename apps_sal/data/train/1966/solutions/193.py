class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
    
        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                mat[i][j] = 1 + mat[i][j-1] if mat[i][j] !=0 else 0

        for j in range(len(mat[0])):
            # keep a mono increasing stack
            # if current num >= prv num-> curr num + prev mat[i-1][j]
            # if current num < prv num -> clean stack

            stack = [(-1, -1)] # index, value
            for i in range(len(mat)):
                while stack and mat[i][j] < stack[-1][1]:
                    stack.pop()
                stack.append((i, mat[i][j]))
                mat[i][j] = mat[i][j] * (i - stack[-2][0]) + (mat[stack[-2][0]][j] if stack[-2][0] != -1 else 0)

        return sum([sum(arr) for arr in mat])
