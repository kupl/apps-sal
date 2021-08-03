class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.grid = rectangle
        # make a new dictionary
        self.rec = {}
\t\t# with enumerate we can iterate through the list rectangle, 
\t\t# taking each row and its index
        for i, row in enumerate(rectangle):
\t\t\t# we map each row to its index as it`s more space-efficent
            self.rec[i] = row
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # start = (row1, col1)
        # end = (row2, col2)
        # diffr = row2 - row1
        # diffc = col2 - col1
        
        # self.grid[row1][col1] = newValue
        
        # for r in range(diffr+1):
        #     for c in range(diffc+1):
        #         self.grid[row1+r][col1+c] = newValue
        # for i in range(row1, row2+1):
        #     self.grid[i] = self.grid[i][:col1] + [newValue]*(col2-col1+1) + self.grid[col2+1:]
        for i in range(row1, row2+1):
\t\t\t# we put new value only from col1 to col2, but we leave other columns as is
            self.rec[i] = self.rec[i][:col1] + [newValue]*(col2-col1+1) + self.rec[i][col2+1:]

    def getValue(self, row: int, col: int) -> int:
        # return self.grid[row][col]
        return self.rec[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
