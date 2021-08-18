class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle
        self.update = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.update.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        ans = None
        for i in range(len(self.update) - 1, -1, -1):
            row1, col1, row2, col2, val = self.update[i]
            if row1 <= row <= row2 and col1 <= col <= col2:
                ans = val
                break
        return ans if ans else self.matrix[row][col]
