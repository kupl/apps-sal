class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
\t\t# make a new dictionary
        self.rec = {}
\t\t# with enumerate we can iterate through the list rectangle, 
\t\t# taking each row and its index
        for i, row in enumerate(rectangle):
\t\t\t# we map each row to its index as it`s more space-efficent
            self.rec[i] = row
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
\t\t# we want to put new value from row1 to row2, so we iterate through them
        for i in range(row1, row2+1):
\t\t\t# we put new value only from col1 to col2, but we leave other columns as is
            self.rec[i] = self.rec[i][:col1] + [newValue]*(col2-col1+1) + self.rec[i][col2+1:]

    def getValue(self, row: int, col: int) -> int:
\t\t# take row (of type list) from dictionary rec, take specified col from row
        return self.rec[row][col]
