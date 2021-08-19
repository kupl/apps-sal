class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self._rect = rectangle
        self._instrs = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self._instrs.append([row1, row2, col1, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for (row1, row2, col1, col2, val) in self._instrs[::-1]:
            if row1 <= row and row <= row2 and (col1 <= col) and (col <= col2):
                return val
        return self._rect[row][col]
