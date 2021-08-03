class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        g = 0
        # li[i][j] is the largest square whose right-lower conner lands at [i][j]
        li = [[0 for a in x] for x in matrix]

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                c = int(matrix[i][j])
                if c == 0:
                    li[i][j] = 0
                    continue
                if i == 0 or j == 0:
                    li[i][j] = c
                    if c > g:
                        g = c
                    continue

                m = min(li[i - 1][j], li[i][j - 1])
                if li[i - 1][j - 1] <= m:
                    li[i][j] = 1 + li[i - 1][j - 1]
                else:
                    li[i][j] = 1 + m

                if li[i][j] > g:
                    g = li[i][j]

        return g**2
