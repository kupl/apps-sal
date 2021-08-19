import numpy as np


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = np.array(rectangle)

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.matrix[row1:row2 + 1, col1:col2 + 1] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row, col]
