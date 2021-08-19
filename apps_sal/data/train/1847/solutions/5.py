class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rec = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        rec = self.rec
        col_range = col1 + col2 - col1 + 1
        for i in range(row2 - row1 + 1):
            recrow = rec[row1 + i]
            for j in range(col1, col_range):
                recrow[j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rec[row][col]
