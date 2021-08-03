class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        # 1

        rows = len(mat) - 1
        cols = len(mat[0]) - 1
        total = 0

        def find_rects(i, j):
            local = 0
            imax = rows + 1
            j_cur = j
            while j_cur <= cols:
                if mat[i][j_cur] == 0:
                    break
                i_cur = i
                while i_cur < imax:
                    if mat[i_cur][j_cur] == 1:
                        i_cur += 1
                    else:
                        break
                imax = min(i_cur, imax)
                local += (imax - i)
                j_cur += 1

            return local

        for i in range(rows + 1):
            for j in range(cols + 1):
                if mat[i][j] == 1:
                    total += find_rects(i, j)
        return total
