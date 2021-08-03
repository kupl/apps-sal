class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        def checkSquare(i, j, k):

            for ind in range(k + 1):
                if grid[i][j + ind] == 0 or grid[i + ind][j] == 0 or grid[i + ind][k + j] == 0 or grid[i + k][j + ind] == 0:
                    return False

            return True

        n = len(grid)
        m = len(grid[0])
        max_ = 0
        min_ = 0

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1:
                    min_ = 1

                    bound = min(n - i, m - j)

                    for k in range(1, bound):
                        if checkSquare(i, j, k):
                            max_ = max(max_, (k + 1)**2)

        return max(max_, min_)
