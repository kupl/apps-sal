class SubrectangleQueries:
    rect = []

    def __init__(self, rectangle: List[List[int]]):
        r = len(rectangle)
        c = len(rectangle[0])
        self.rect = [[0 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                self.rect[i][j] = rectangle[i][j]

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        r = row2 - row1
        c = col2 - col1
        for i in range(row1, row1 + r + 1):
            for j in range(col1, col1 + c + 1):
                self.rect[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
