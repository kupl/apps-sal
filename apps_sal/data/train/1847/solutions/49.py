class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # index into rectangle and change all values in subrectangle
        # gonna have to loop through it
        for row in range(len(self.rectangle)):
            if row >= row1 and row <= row2:
                for col in range(len(self.rectangle[0])):
                    if col >= col1 and col <= col2:
                        self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

