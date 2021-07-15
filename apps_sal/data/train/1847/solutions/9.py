class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.q = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.q[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.q[row][col] 
