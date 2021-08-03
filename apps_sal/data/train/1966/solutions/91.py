class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        for r in range(R):
            for c in range(1, C):
                if mat[r][c]:
                    mat[r][c] = mat[r][c - 1] + 1
        ans = 0
        for r in range(R):
            for c in range(C):
                if mat[r][c]:
                    minWidth = mat[r][c]
                    row = r
                    while row < R:
                        minWidth = min(minWidth, mat[row][c])
                        ans += minWidth
                        row += 1
        return ans
