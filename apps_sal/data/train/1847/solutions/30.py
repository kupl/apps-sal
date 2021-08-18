class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.r = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for x in range(row1, row2 + 1):
            for y in range(col1, col2 + 1):
                self.r[x][y] = newValue

        return None

    def getValue(self, row: int, col: int) -> int:
        return self.r[row][col]
