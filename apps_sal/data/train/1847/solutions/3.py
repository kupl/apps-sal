class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in self.rectangle[row1:row2 + 1]:
            for i in range(col1, col2 + 1):
                row[i] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
