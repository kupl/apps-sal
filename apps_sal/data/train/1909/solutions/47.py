class Solution:

    def checkForSquare(self, grid: List[List[int]], i: int, j: int, squareLen: int) -> bool:
        maxRowBound = i + squareLen - 1
        maxColBound = j + squareLen - 1
        if self.accessGrid(grid, maxRowBound, maxColBound) == 1:
            k = maxColBound
            while k != j and self.accessGrid(grid, maxRowBound, k) == 1:
                k -= 1
            if k != j:
                return False
            s = maxRowBound
            while s != i and self.accessGrid(grid, s, maxColBound) == 1:
                s -= 1
            if s == i:
                return True
        return False

    def accessGrid(self, grid: List[List[int]], i: int, j: int) -> int:
        if i < self.rows and j < self.cols:
            return grid[i][j]
        else:
            return -1

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        i = 0
        j = 0
        largest_square = 0
        while i < self.rows:
            while j < self.cols:
                search_increment = 1
                if grid[i][j] == 1:
                    if largest_square == 0:
                        largest_square = 1
                    if j != self.cols - 1:
                        max_col_bound = j
                        max_row_bound = i
                        while self.accessGrid(grid, i, max_col_bound) == 1:
                            max_col_bound += 1
                        square_len = max_col_bound - j
                        if square_len > 0:
                            while self.accessGrid(grid, max_row_bound, j) == 1:
                                max_row_bound += 1
                        square_len = min(square_len, max_row_bound - i)
                        while square_len ** 2 > largest_square:
                            if self.checkForSquare(grid, i, j, square_len):
                                largest_square = square_len ** 2
                                search_increment = square_len - 1
                            else:
                                square_len -= 1
                remaining_search_space = max((self.rows - i) ** 2, (self.cols - search_increment) ** 2)
                if largest_square >= remaining_search_space:
                    return largest_square
                j += search_increment
            i += 1
            j = 0
        return largest_square
