class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        width = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            width[i][0] = mat[i][0]
        for i in range(n):
            for j in range(1, m):
                if mat[i][j] != 0:
                    width[i][j] = width[i][j - 1] + 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    min_width = width[i][j]
                    for new_i in range(i, -1, -1):
                        if mat[new_i][j] == 0:
                            break
                        min_width = min(min_width, width[new_i][j])
                        ans += min_width
        return ans
