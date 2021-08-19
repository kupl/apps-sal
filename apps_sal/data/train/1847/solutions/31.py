class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.orig = rectangle
        self.updates = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for (a, b, c, d, v) in reversed(self.updates):
            if a <= row <= c and b <= col <= d:
                return v
        return self.orig[row][col]
