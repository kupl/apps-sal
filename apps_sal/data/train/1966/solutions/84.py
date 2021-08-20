class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:

        def rectangles_staring_at(i, j):
            res = 0
            max_col = m
            for x in range(i, n):
                for y in range(j, max_col):
                    if mat[x][y] == 1:
                        res += 1
                    else:
                        max_col = y
                        break
            return res
        sums = [list(accumulate(row)) for row in mat]
        print(sums)
        (ans, n, m) = (0, len(mat), len(mat[0]))
        for i in range(n):
            for j in range(m):
                ans += rectangles_staring_at(i, j)
        return ans
