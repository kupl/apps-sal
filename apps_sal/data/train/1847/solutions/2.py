class SubrectangleQueries:
    rectangle = [[]]

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        while(row1 <= row2):
            self.rectangle[row1][col1:col2 + 1] = [newValue] * len(self.rectangle[row1][col1:col2 + 1])
            row1 += 1

    def getValue(self, row: int, col: int) -> int:
        return (self.rectangle[row][col])
