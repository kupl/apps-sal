class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        table = [[(0, 0) for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    hor = 1 if j == 0 else table[i][j-1][0] + 1
                    ver = 1 if i == 0 else table[i-1][j][1] + 1

                    table[i][j] = (hor, ver)

        # for i in table:
        #     print(i)

        ans = float('-inf')

        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if table[i][j] != (0, 0):
                    min_ = min(table[i][j])
                    while min_ > ans:
                        up = i - min_ + 1
                        left = j - min_ + 1
                        if table[i][left][1] >= min_ and table[up][j][0] >= min_ and min_ > ans:
                            ans = min_
                        min_ -= 1

        return ans * ans if ans != float('-inf') else 0
