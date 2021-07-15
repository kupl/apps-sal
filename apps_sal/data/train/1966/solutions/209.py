class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])

        def count_submatrices(a, b):
            count, bound = 0, N

            for i in range(a, M):
                y = b
                while y < bound:
                    if mat[i][y]:
                        count += 1
                    else:
                        bound = y
                    y += 1

                # bound is the boundary of col, if mat[a][b] == 0, means top-left cornor is 0, we won't have any
                # submatrics with all 1's, so return directly
                if bound == b:
                    return count
            return count

        count = 0
        for i in range(M):
            for j in range(N):
                count += count_submatrices(i, j)
        return count



