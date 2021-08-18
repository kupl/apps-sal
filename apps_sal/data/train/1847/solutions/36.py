class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.x = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        i = row1
        j = col1
        while i < row2 + 1 and j < col2 + 1:
            self.x[i][j] = newValue
            if j == col2:
                j = col1
                i = i + 1
            else:
                j = j + 1

    def getValue(self, row: int, col: int) -> int:
        return self.x[row][col]
