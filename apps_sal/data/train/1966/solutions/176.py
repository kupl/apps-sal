class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        for j in range(len(mat[0])):
            for i in range(1, len(mat)):
                if mat[i][j] != 0:
                    if mat[i - 1][j] != 0:
                        mat[i][j] = mat[i - 1][j] + 1
        cnt = 0
        for i in range(0, len(mat)):
            for j in range(len(mat[0])):
                min_height = len(mat)
                for k in range(j, -1, -1):
                    if mat[i][k] == 0:
                        break
                    min_height = min(min_height, mat[i][k])
                    cnt += min_height
        return cnt
