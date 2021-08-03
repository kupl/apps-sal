class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        def checkSquare(i, j, k):

            for ind in range(k + 1):
                if grid[i][j + ind] == 0 or grid[i + ind][j] == 0:
                    return 1

            for ind in range(k + 1):
                if grid[i + ind][k + j] == 0 or grid[i + k][j + ind] == 0:
                    return 2

            return 0

        n = len(grid)
        m = len(grid[0])
        max_ = 0
        min_ = 0

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1:
                    bound = min(n - i, m - j)

                    if max_ > (bound - 1)**2:
                        continue

                    else:
                        min_ = 1

                        for k in range(1, bound):
                            result = checkSquare(i, j, k)
                            if result == 0:
                                max_ = max(max_, (k + 1)**2)
                            elif result == 1:
                                break

        return max(max_, min_)
