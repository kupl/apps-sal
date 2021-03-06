class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.grid = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        start = (row1, col1)
        end = (row2, col2)
        diffr = row2 - row1
        diffc = col2 - col1
        for r in range(diffr + 1):
            for c in range(diffc + 1):
                self.grid[row1 + r][col1 + c] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.grid[row][col]
