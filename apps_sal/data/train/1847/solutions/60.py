class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        self.height = len(self.rect)
        self.width = len(self.rect[0])

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            self.rect[row][col1:col2+1] = [newValue] * (col2 - col1 + 1)
        

    def getValue(self, row: int, col: int) -> int:
        if row > self.height - 1 or col > self.width - 1:
            return None
        return self.rect[row][col]
        
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

