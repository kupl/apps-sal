import itertools


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.w = len(rectangle[0])
        self.rectangle = list(itertools.chain.from_iterable(rectangle))

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        (start, end) = (col1 + row1 * self.w, col2 + row2 * self.w)
        for i in range(col1, col2 + 1):
            for j in range(row1, row2 + 1):
                self.rectangle[i + j * self.w] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[col + row * self.w]
