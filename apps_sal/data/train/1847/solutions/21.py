class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        self.patches = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.patches.append((row1,col1,row2,col2,newValue))
        
    def matchesPatch(self, row, col, patch):
        return patch[0] <= row and row <= patch[2] and patch[1] <= col and col <= patch[3]

    def getValue(self, row: int, col: int) -> int:
        for patch in reversed(self.patches):
            if self.matchesPatch(row, col, patch):
                return patch[-1]
        return self.rect[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

