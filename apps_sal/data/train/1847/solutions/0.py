class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.initial_rectangle = rectangle
        self.rectangles = []
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.rectangles.append((row1, col1, row2, col2, newValue))
        

    def getValue(self, row: int, col: int) -> int:
        for row1, col1, row2, col2, value in reversed(self.rectangles):
            if row1 <= row <= row2 and col1 <= col <= col2:
                return value
        return self.initial_rectangle[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

