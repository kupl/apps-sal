

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        def num_submat_at(a, b):
            c = 0
            bound = m

            i = a
            while i < n:
                j = b
                while j < bound:
                    if mat[i][j]:
                        c += 1
                    else:
                        bound = j

                    j += 1
                i += 1
            return c

        total_c = 0
        for i in range(n):
            for j in range(m):
                total_c += num_submat_at(i, j)

        return total_c
