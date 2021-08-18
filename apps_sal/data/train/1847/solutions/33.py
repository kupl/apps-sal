import numpy as np


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row2 + 1 - row1):
            for j in range(col2 + 1 - col1):
                self.rectangle[row1 + i][col1 + j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
