class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        for i in rectangle:
            print(i)
        print(\"\
\")
        self.rectangle = rectangle
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        rec =self.rectangle
        
        for i in range(row1, row2 + 1):
            row = []
            for j in range(col1, col2 + 1):
                rec[i][j] = newValue
                row.append(rec[i][j])
            

            
        
        

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
