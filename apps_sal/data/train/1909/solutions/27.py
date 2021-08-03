class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        top = Solution.fill_top(grid, n, m)
        left = Solution.fill_left(grid, n, m)
        bottom = Solution.fill_bottom(grid, n, m)
        right = Solution.fill_right(grid, n, m)

        def top_left(i, j):
            return min(top[i][j], left[i][j])

        def bottom_right(i, j):
            return min(bottom[i][j], right[i][j])

        square = 0

        for i in range(n):
            for j in range(m):
                sliding = top_left(i, j)

                for s in range(sliding - 1, -1, -1):
                    k = i - s
                    l = j - s
                    if bottom_right(k, l) >= (s + 1):
                        square = max(square, s + 1)

        return square ** 2

    @staticmethod
    def empty(n, m):
        return [[0] * m for _ in range(n)]

    @staticmethod
    def fill_top(grid, n, m):
        top = Solution.empty(n, m)

        for i in range(n):
            if i == 0:
                for j in range(m):
                    top[0][j] = grid[0][j]
            else:
                for j in range(m):
                    top[i][j] = top[i - 1][j] + 1 if grid[i][j] == 1 else 0
        return top

    @staticmethod
    def fill_left(grid, n, m):
        left = Solution.empty(n, m)

        for j in range(m):
            if j == 0:
                for i in range(n):
                    left[i][0] = grid[i][0]
            else:
                for i in range(n):
                    left[i][j] = left[i][j - 1] + 1 if grid[i][j] == 1 else 0
        return left

    @staticmethod
    def fill_bottom(grid, n, m):
        bottom = Solution.empty(n, m)

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                for j in range(m):
                    bottom[n - 1][j] = grid[n - 1][j]
            else:
                for j in range(m):
                    bottom[i][j] = bottom[i + 1][j] + 1 if grid[i][j] == 1 else 0
        return bottom

    @staticmethod
    def fill_right(grid, n, m):
        right = Solution.empty(n, m)

        for j in range(m - 1, -1, -1):
            if j == m - 1:
                for i in range(n):
                    right[i][m - 1] = grid[i][m - 1]
            else:
                for i in range(n):
                    right[i][j] = right[i][j + 1] + 1 if grid[i][j] == 1 else 0
        return right
