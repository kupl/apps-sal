class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res, lr, lc = 0, len(mat), len(mat[0]) if mat else 0
        for i in range(lr):
            for j in range(lc):
                if mat[i][j]:
                    cur, x, limit = 0, i, lc
                    while x < lr:
                        y = j
                        if not mat[x][y]:
                            break
                        while y < limit:
                            if not mat[x][y]:
                                limit = y
                                break
                            cur, y = cur + 1, y + 1
                        x += 1
                    res += cur
        return res
