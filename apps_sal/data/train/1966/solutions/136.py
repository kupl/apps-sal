class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        def count_submatrices(r, c):
            count = 0
            bound = n
            for i in range(r, m):
                for j in range(c, bound):
                    if j >= bound:
                        continue
                    elif mat[i][j] == 1:
                        count += 1
                    else:
                        bound = j
            return count

        # return count_submatrices(0, 0)
        total_count = 0
        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                total_count += count_submatrices(r, c)

        return total_count
