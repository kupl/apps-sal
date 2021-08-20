class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(len(self.rectangle)):
            if not row1 <= row <= row2:
                continue
            for col in range(len(self.rectangle[row])):
                if not col1 <= col <= col2:
                    continue
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
