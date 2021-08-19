class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.changes = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.changes.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for (row1, col1, row2, col2, newValue) in reversed(self.changes):
            if row1 <= row <= row2 and col1 <= col <= col2:
                return newValue
        return self.rectangle[row][col]
