class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.columns = len(rectangle[0])
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        initial = col1
        while row1 <= row2 and col1 <= col2:
            self.rectangle[row1][col1] = newValue
            col1 += 1

            if not col1 < self.columns or not col1 <= col2:
                col1 = initial
                row1 += 1

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
    

