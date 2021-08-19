class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.R = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            self.R[row][col1:col2 + 1] = [newValue] * (col2 - col1 + 1)
        return None

    def getValue(self, row: int, col: int) -> int:
        return self.R[row][col]
